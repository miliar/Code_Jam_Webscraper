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
#include <fstream>
#include <cassert>
#ifdef HOME_PC
#include <ctime>
#endif
using namespace std;

#pragma comment(linker,"/stack:16000000")
#pragma warning (disable : 4996)

#define ALL(v) v.begin(),v.end()
#define SZ(v) (int)v.size()
#define mset(A,x) memset((A),(x),sizeof(A))
#define FOR(i,start,N) for(int i=(start);i<(N);++i)
#define FORSZ(i,start,v) FOR(i,start,SZ(v))
#define REPSZ(i,v) FORSZ(i,0,v)
#define FORE(i,start,N) FOR(i,start,N+1)
#define make_unique(v) v.resize(unique(ALL(v))-v.begin())
#define debug(x) cout<<#x<<" = "<<x<<endl;
#define adebug(A,N) FOR(i,0,N) cout<<#A<<"["<<i<<"] = "<<A[i]<<endl;
#define adebug2d(a,n,m) FOR(i,0,n) { FOR(j,0,m) { cout<<a[i][j]<<" ";} cout<<endl;}
#define vdebug(v) REPSZ(i,v) cout<<#v<<"["<<i<<"] = "<<v[i]<<endl;
#define selfx(x,f,a) x = f(x,a)
#define sqr(x) ((x)*(x))


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

int main()
{
#ifdef HOME_PC
	//freopen ("input.txt","r",stdin);
	freopen ("A-large.in","r",stdin);
	freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		int ans = 0;
		int left[2] = { 200,200};
		VI targets[2];
		VI q;

		int n;
		cin>>n;
		FOR(i,0,n)
		{
			string who; int t;
			cin>>who>>t;
			int p = who[0] == 'O';
			targets[p].push_back(t);
			q.push_back(p);
			
		}
		FOR(i,0,2)
		{
			targets[i].push_back(200);
			left[i] = targets[i][0] - 1;
			reverse(ALL(targets[i]));
		}

		
		REPSZ(i,q)
		{
			int p = q[i];
			int passed = left[p] + 1;
			ans+=passed;
			left[p] = abs(targets[p].back() - *(++targets[p].rbegin()));
			targets[p].pop_back();
			left[p^1] = max(left[p^1] - passed,0);			
		}

		printf("Case #%d: %d\n",cas,ans);
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

