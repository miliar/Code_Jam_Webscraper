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
	freopen("i.in", "r", stdin);
	freopen("o1.out", "w", stdout);
	
	
	int t;
	S(t);
	int p = 1;
	while(t--)
	{
		string s, m;
		cin >> s;
		int ss = s.SZ;
		string k = s;
		next_permutation(s.begin(), s.end());
		
		if(k >= s)
		{
			//m = "yes";
			string tp, tpz;
			int j;
			REP(j,s.SZ)
				if(s[j]=='0')
					tpz.PB(s[j]);
				else
					tp.PB(s[j]);
			tpz +="0";
			sort(tp.begin(),tp.end());
			s = "";
			s.PB(tp[0]);
			s += tpz;
			REPA(j,1,tp.SZ)
				s.PB(tp[j]);
			
		}
		
		cout << "Case #"<<p<<": "<< s  << endl;
		p++;	
	}
	return 0;	
}
