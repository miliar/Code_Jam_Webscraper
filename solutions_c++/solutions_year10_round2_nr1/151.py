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
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;


vector<string> split(string s,string delims)
{
	vector<string> ret;
	for(int i = 0;i < s.size(); ++i)
		if(delims.find(s[i])!=string::npos) s[i] = ' ';
	stringstream ss(s);
	while(ss>>s) ret.push_back(s);
	return ret;
}

int maxPref(const VS& a,const VS& b)
{
	int ret = 0;
	int n = min(a.size(),b.size());
	FOR(i,0,n)
		if(a[i]!=b[i])
			break;
		else
			++ret;

	return ret;
}



int main()
{
	freopen ("A-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("A-large.out","w",stdout);

	int tt;
	cin>>tt;
	for(int cas = 1;cas<=tt;++cas)
	{
		int n,m;
		cin>>n>>m;
		vector<vector<string> > dir;
		string s;
		FOR(i,0,n)
		{
			cin>>s;
			VS a = split(s,"/");
			dir.push_back(a);
		}
		

		int ans = 0;
		FOR(i,0,m)
		{
			cin>>s;
			VS cur = split(s,"/");
			int max_pref = 0;
			int mj = -1;
			int dirs_create = cur.size();
			REPSZ(j,dir)
			{
				int mx = maxPref(cur,dir[j]);
				if(mx != dir[j].size())
					continue;
				if(mx > max_pref)
				{
					max_pref = mx;
					mj = j;
					dirs_create = min<int>(dirs_create,cur.size() - mx);
				}
			}
			ans+=dirs_create;
			
			
			for(int j = 0; j < dirs_create; ++j)
			{
				dir.push_back(cur);
				cur.pop_back();
			}
		}

		printf("Case #%d: %d\n",cas,ans);
	}

	return 0;
}

