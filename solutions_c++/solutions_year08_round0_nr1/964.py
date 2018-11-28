#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

int main(int argc, char* argv[])
{
	int scount, qcount, count;
	string s, r, t;
	string line;
	int i, k, j;

	vector<string> engines, queries;
	map<int, int> mp;

	cin >> count;
	for(i=0;i<count;i++)
	{
	//clear
	engines.clear();
	queries.clear();
	mp.clear();

	//input
	cin >> scount;
	getline(cin, line);
	for(j=0;j<scount;j++)
	{
		getline(cin, line);
		engines.push_back(line);
	}

	cin >> qcount;
	getline(cin, line);
	for(j=0;j<qcount;j++)
	{
		getline(cin, line);
		if(j==0 || line!=queries[queries.size()-1])
			queries.push_back(line);
	}
	qcount = queries.size();

	int switchescount = 0;
	for(j=0;j<qcount;j++)
	{
		for(k=0;k<scount;k++)
			if(queries[j]==engines[k])
				break;
		mp[k]++;
		if(mp.size()==scount)
		{
			switchescount++;
			mp.clear();
			j--;
		}
	}

	/*int switchescount = scount+1;
	for(j=0;j<scount;j++)
	{
		if(mp[j]<switchescount)
			switchescount = mp[j];
	}*/


	//result
		cout << "Case #" << i+1 << ": ";
		cout << switchescount;
		cout << endl;
	}


	return 0;
}

