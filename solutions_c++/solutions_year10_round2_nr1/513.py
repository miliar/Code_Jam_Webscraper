#include<iostream>
#include<string.h>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL unsigned long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;

#define VS vector<string>
int N, M;
VS there, crt;
map<string, int> m;
int exist(string path)
{
	if(m.find(path) == m.end())
		return 0;
	return 1;
}
void putinmap(string path)
{
	m[path] = 1;
}
void preproc()
{
	int i, j, k;
	for(i = 0; i < N; i++)
	{
		string tpath;
		tpath.PB(there[i][0]);
		int cur = 1;
		int n = SZ(there[i]);
		string tstr = "";
		string tp = there[i];
		while(cur <= n)
		{
			if(cur == n || tp[cur] == '/')
			{
				putinmap(tpath);
			}
			if(cur != n)
			tpath.PB(tp[cur]);
			cur++;
		}
	}
}
int solve()
{
	int ret = 0;
	int i, j, k;
	for(i = 0; i < M; i++)
	{
		string tpath;
		tpath.PB(crt[i][0]);
		int cur = 1;
		int n = SZ(crt[i]);
		string tstr = "";
		string tp = crt[i];
		while(cur <= n)
		{
			if(cur == n || tp[cur] == '/')
			{
				if(m.find(tpath) == m.end())
				ret++;
				putinmap(tpath);
			}
			if(cur != n)
			tpath.PB(tp[cur]);
			cur++;
		}		
	}
	return ret;
}
		
		
int main()
{
	int tes;
	int tesnum = 0;
	cin >> tes;
	while(tes--)
	{
		tesnum++;
		there.clear();
		crt.clear();
		cin >> N >> M;
		m.clear();
		m["/"] = 1;
		int i, j, k;
		
		for(i = 0; i < N; i++)
		{
			string s;
			cin >> s;
			there.PB(s);
		}
		for(i = 0; i < M; i++)
		{
			string s;
			cin >> s;
			crt.PB(s);
		}
		preproc();
		int ans = solve();
		/*for(map<string, int> :: iterator it=m.begin(); it!=m.end();it++)
		{
			cout << it->first << " " << it -> second << endl;
		}*/
		printf("Case #%d: %d\n", tesnum, ans);
	}
	return 0;
}
		
			
