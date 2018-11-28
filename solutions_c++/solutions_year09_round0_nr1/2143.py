#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define S(n) scanf("%d",&n)
#define REP(i,n) for(i=0; i<n; i++)
#define REPA(i,a,n) for(i=a; i<n; i++)
#define SOR(x) sort(x.begin(), x.end())
#define REV(x) reverse(x.begin(), x.end())
#define FOREACH(iter,var) for(__typeof((var).begin()) iter=(var).begin(); iter!=(var).end(); iter++)
#define PB push_back
#define VI vector<int>
#define SZ size()
#define VS vector<string>

#define MP make_pair
#define VVI vector< vector<int> >
#define INF 2000000000

int main()
{
	freopen("input.in", "r", stdin);
	freopen("ouput.out", "w", stdout);
	
	int l, d, n, i, j, k, m;
	bool valid[6000];
	S(l); S(d); S(n);
	
	vector<string> dict;
	REP(i, d)
	{
			string s; 
			cin >> s;
			dict.PB(s);
	}
	
	REP(m, n)
	{
		vector<char> vc[6000];
		int ans = 0;
		memset(valid,1,sizeof(valid));
		string s;
		cin >> s;
		int c = 0, mode = 1;
		REP(j, s.SZ)
		{
			if(s[j] == '(') { mode = 0; continue; }
			if(s[j] == ')') { mode = 1; c += mode; continue; }
			
			vc[c].PB(s[j]);
			c += mode;
		}
		
		REP(j, c)
		{
			REP(i, d)
			{
				if(!valid[i]) continue;
				valid[i] = false;
				REP(k, vc[j].SZ)
					if(vc[j][k] == dict[i][j]) 
					{ 
						if(j == c - 1) ans++;
						valid[i] = true;
						break; 
					}
			}
		}
		
		cout << "Case #" << m+1<< ": "<< ans << endl;
	}
	
	
	return 0;
}
