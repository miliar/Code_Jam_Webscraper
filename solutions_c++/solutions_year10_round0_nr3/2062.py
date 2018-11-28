#include <iostream>
#include <vector>
#include <set>

using namespace std;

struct aggregate	{
	long index;
	long long value;
};

vector<aggregate> groups;
set<long> indexes;
long repIndex;
vector<long long> groupList;
long long rotations;
long long load;

void fillGroups()	{
	
	aggregate blah;
	blah.index = 0;
	blah.value = groupList[0];
	indexes.insert(0);

	long index = 1;
	index = index % groupList.size();
	
	while (blah.value + groupList[index] <= load && index != blah.index)	{
		blah.value += groupList[index];
		index++;
		index = index % groupList.size();
	}

// 	cout << blah.value << " index " << index << " load " << load << endl;
	groups.push_back(blah);
	blah.index = index;
	blah.value = groupList[index];
	index++;
	index = index % groupList.size();

	while (indexes.count(blah.index) == 0)	{

		while (blah.value + groupList[index] <= load && index != blah.index)	{
			blah.value += groupList[index];
			index++;
			index = index % groupList.size();
		}

		groups.push_back(blah);
		indexes.insert(blah.index);
// 		cout << blah.value << " index " << blah.index << endl;
		blah.index = index;
		blah.value = groupList[index];
		index++;
		index = index % groupList.size();
	}

	repIndex = (index - 1 + groupList.size()) % groupList.size();
}

void printGroups()	{

	for (int i = 0; i < groups.size(); i++)	{
		cout << "index " << groups[i].index << " value " << groups[i].value << endl;
	}
	
	cout.flush();
}

void solve(int casenum)	{
	
	fillGroups();
//  	printGroups();

	int debugVal = 39;
	
	long long totalInGroup = 0;
	long index = 0;
	
	for (int i = 0; i < groups.size(); i++)	{
		if (groups[i].index == repIndex)	{
			index = i;
			break;
		}
	}
	
	for (int i = index; i < groups.size(); i++)	{
		totalInGroup += groups[i].value;
	}

	long long result = 0;

	for (int i = 0; i < index && rotations > 0; i++)	{
		result += groups[i].value;
		rotations--;
	}

	long multiple = rotations / (groups.size() - index);
	
	result += totalInGroup * multiple;
	long limBoundary = rotations - ((groups.size() - index) * multiple);
	
	for (int i = index; i < index + limBoundary; i++)	{
		result += groups[i].value;
	}

	cout << "Case #" << casenum << ": " << result << endl;
}

void solveBrute(int casenum)	{

	long long result = 0;
	long index = 0;

	while (rotations > 0)	{

		long carrigeLoad = 0;

		int counter = 0;
		while (carrigeLoad + groupList[index] <= load && counter != groupList.size())	{
			carrigeLoad += groupList[index];
			index++;
			index = index % groupList.size();
			counter++;
		}

		result += carrigeLoad;
// 		if(casenum == 11)
// 			cout << result << " " << carrigeLoad << " " << (rotations -1) << endl;
		rotations--;
	}

	cout << "Case #" << casenum << ": " << result << endl;
}

int main()	{

	int testLim;
	cin >> testLim;

	for (int i = 0; i < testLim; i++)	{

		int totalGroups;
		cin >> rotations >> load >> totalGroups;

		for (int j = 0; j < totalGroups; j++)	{

			groupList.push_back(0);
			cin >> groupList[j];

		}

solve(i + 1);
		groupList.clear();
		groups.clear();
		indexes.clear();
	}
}