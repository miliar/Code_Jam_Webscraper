#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <fstream>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define mp make_pair
#define all(x) (x).begin(),(x).end()


ifstream in("input_a.txt");


map<char, char> alphaMap_;
map<char, char> alphaMapRev_;

void mapper()
{
	vector<string> orginal;
	orginal.push_back("ejp mysljylc kd kxveddknmc re jsicpdrysi");
	orginal.push_back("rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd");
	orginal.push_back("de kr kd eoya kw aej tysr re ujdr lkgc jv");

	vector<string> target;
	target.push_back("our language is impossible to understand");
	target.push_back("there are twenty six factorial possibilities");
	target.push_back("so it is okay if you want to just give up");

	REP(i, orginal.size())
	{
		REP(j, orginal[i].size())
		{
			if(orginal[i][j] == ' ')
				continue;

			char from = orginal[i][j];
			char to = target[i][j];

			if(alphaMap_.find(from) != alphaMap_.end())
			{
				if(alphaMap_[from] != to)
				{
					cout << "Error: " << from << ", " << to << endl;
				}
			}

			alphaMap_[from] = to;
		}
	}

	alphaMap_['q'] = 'z';
	alphaMap_['z'] = 'q';
	alphaMap_[' '] = ' ';

	//vector<bool> alphaUsed(1000, false);
	//for(char i = 'a'; i <= 'z'; i++)
	//{
	//	if(alphaMap_[i] == 0)
	//		continue;
	//	
	//	char last = i;
	//	while(alphaUsed[last] == false)
	//	{
	//		alphaUsed[last] = true;
	//		last = alphaMap_[last];
	//	}
	//}

	//for(char i = 'a'; i <= 'z'; i++)
	//	cout << i << ": " << alphaMap_[i] << ", " << alphaUsed[i] << endl;
}

int main(int argc, char **argv)
{
	mapper();

	ofstream out("out_a.txt");
	int T;
	in >> T;
	string text;
	getline(in, text);
	for(int t = 1; t <= T; t++)
	{
		getline(in, text);
		//cout << text << endl;
		string answer;
		REP(i, text.size())
			answer.push_back(alphaMap_[text[i]]);

		cout << "Case #" << t << ": " << answer << endl;
		out << "Case #" << t << ": " << answer << endl;
	}
	return 0;
}
