#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <map>
#include <queue>
#include <sstream>
#include <numeric>
#include <functional>
#include <set>
#include <cmath>
#include <stack>
using namespace std;

#pragma comment(linker,"/stack:16000000")

#define ALL(v) v.begin(),v.end()
#define SZ(v) v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=start;i<N;++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

int L,D,N;
VS dict;
VS pat;


void parse(string s)
{
	pat.clear();
	REPSZ(i,s)
		if(s[i]=='(')
		{
			int j = s.find(')',i);
			string t = s.substr(i,j-i+1);
			pat.push_back(t);
			i = j;
		}
		else
			pat.push_back(string(1,s[i]));
}

int match(string s)
{
	REPSZ(i,s)
		if(pat[i].find(s[i])==string::npos)
			return 0;
	return 1;
}

int solve()
{
	int ret = 0;
	REPSZ(i,dict)
		ret+=match(dict[i]);

	return ret;
}
int main()
{
freopen ("A-large.in.txt","r",stdin);
//freopen ("in.txt","r",stdin);
freopen ("output.txt","w",stdout);

	cin>>L>>D>>N;
	dict.resize(D);
	

	FOR(i,0,D) cin>>dict[i];

	for(int cas = 1;cas<=N;++cas)
	{
		string p;
		cin>>p;
		parse(p);
		int ans = solve();
		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

