#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <complex>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <float.h>

#define PB push_back 
#define MP make_pair 
#define SZ(v) ((int)(v).size()) 
#define FOR(i,a,b) for(int i=(a);i<(b);++i) 
#define REP(i,n) FOR(i,0,n) 
#define FORE(i,a,b) for(int i=(a);i<=(b);++i) 
#define REPE(i,n) FORE(i,0,n) 
#define FORSZ(i,a,v) FOR(i,a,SZ(v)) 
#define REPSZ(i,v) REP(i,SZ(v)) 
typedef long long ll; 


using namespace std;

bool getnext(vector<int>& next)
{
	if (next.size() == 0)
		return false;

	int i = 0;
	while (next[i] == 2)
	{
		next[i] = 0;
		i++;
		if (i >= next.size())
			return false;		
	}
	
	next[i]++;
	return true;
}

ll calc(string& line, vector<int>& next, int pos, ll res)
{
	if (pos == line.size() - 1)
		return res * 10 + (line[pos] - '0');

	if (pos >= next.size())
		return 0;

	if (next[pos] == 0)
	{
		return calc(line, next, pos + 1, res * 10 + (line[pos] - '0'));
	}
	if (next[pos] == 1)
	{
		return res * 10 + (line[pos] - '0') + calc(line, next, pos + 1, 0);
	}
	return res * 10 + (line[pos] - '0') - calc(line, next, pos + 1, 0);

}

int main(int argc, char* argv[])
{
	ifstream cin("test.in");
	//ofstream cout("x.out");

	int caseCount;
	cin >> caseCount;

	string line;
	getline(cin, line);

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		set<int> numbers;
		string line;
		getline(cin, line);
		int ans = 0;

		vector<int> next(line.length() - 1);
		ll res;
		do 
		{
			res = calc(line, next, 0, 0);
			//if (numbers.find(res) == numbers.end())
			{
				if (res % 2 == 0 || res % 3 == 0 ||res % 5 == 0 || res % 7 == 0)
				{
					ans++;

				}
				//numbers.insert(res);
			}

		} while(getnext(next));

		printf("Case #%i: %d\n", nCase, ans);
	}


	return 0;
}

