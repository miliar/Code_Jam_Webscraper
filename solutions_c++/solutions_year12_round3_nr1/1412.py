#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

#define FORI(x,y) for(int x = 0 ; x < y ; ++x)

class Node
{
public:
	vector<int> next;
	int toCount;
	set<int> toHere;

	void Input(ifstream & input, int index)
	{
		toCount = 0;
		input >> toCount;
		FORI(i , toCount)
		{
			int temp;
			input >> temp;
			next.push_back(temp);
		}
		toCount = 0;
		toHere.insert(index);
	}
	bool Unite(Node & child)
	{
		for(auto i = child.toHere.begin() ; i != child.toHere.end() ; ++i)
		{
			if(toHere.insert(*i).second == false)
				return false;
		}

		return true;
	}
};

int main()
{
	char inFilename[] = "G:\\A-large.in";
	char outFilename[] = "G:\\out.txt";
	ifstream inputFile(inFilename);
	ofstream outputFile(outFilename, ios::out);
	if(!inputFile || !outputFile)
	{
		cout << "File Operation Error!" <<endl;
		return 1;
	}

	int numQ = 0;
	inputFile >> numQ;

	for(int i = 0 ; i < numQ ; ++i)
	{
		cout << "Solving #" << i+1 << endl;
		outputFile << "Case #" << i+1 << ": ";
		//begin

		//Input
		int numNode = 0;
		vector<Node> nodeList;
		bool noDiamond = true;
		inputFile >> numNode;
		FORI(j , numNode)
		{
			Node cur;
			cur.Input(inputFile , nodeList.size() + 1 );
			nodeList.push_back(cur);
		}

		//Map toCount
		FORI(j , numNode)
			for_each(nodeList[j].next.begin(), nodeList[j].next.end(), [&](int k){nodeList[k-1].toCount++;});

		FORI(j, numNode)
		{
			//Locate entry
			for(auto it = nodeList.begin() ; it != nodeList.end(); ++it)
			{
				if(it->toCount == 0)
				{
					//Broadcast
					for(auto jt = it->next.begin() ; jt != it->next.end() ; ++ jt)
					{
						if((noDiamond = nodeList[*jt - 1].Unite(*it)) == false)
							goto END; //Easier to use
						nodeList[*jt - 1].toCount--;
					}
					//Abandon
					it->toCount = -1;
				}
			}
		}

END:
		if(noDiamond)
			outputFile << "No" << endl;
		else
			outputFile << "Yes" << endl;
	}


	inputFile.close();
	outputFile.close();
	return 0;
}