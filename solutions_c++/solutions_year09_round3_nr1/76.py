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

int digit(char c)
{
	if(isdigit(c)) return c-'0';
	return c-'a'+10;
}

int get_base(char c)
{
	return digit(c)+1;
}

map<char,int> ids;

i64 convert(string s,int base)
{
	i64 ret = 0;
	REPSZ(i,s)
		ret = base*ret + ids[s[i]];
	return ret;
};

int next(int a)
{
	if(a==0)
		return 2;
	if(a==1) return 0;
	return a+1;
}

int main()
{
//freopen ("input.txt","r",stdin);
//freopen ("in.txt","r",stdin);
freopen ("output.txt","w",stdout);

	int tt;
	cin>>tt;
	for(int cas = 1;cas<=tt;++cas)
	{
		string s;
		cin>>s;
		int fr = 1;
		
		ids.clear();
		
		REPSZ(i,s)
			if(ids.find(s[i])==ids.end())
			{
				ids[s[i]] = fr;
				fr = next(fr);
			}
		int base = ids.size();
		base = max(base,2);
		i64 ans = convert(s,base);
		printf("Case #%d: ",cas);
		cout<<ans<<endl;
	}

	return 0;
}

