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
#define SZ(v) ((int)(v.size()))
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
	freopen ("A-large(1).in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif
	int numTests = 0;
	cin>>numTests;
	FORE(testCase,1,numTests)
	{
		int N;
		cin>>N;
		vector<pii> tarz(N);
		FOR(i,0,N)
			cin>>tarz[i].first >> tarz[i].second;

		int D;
		cin>>D;
		sort(ALL(tarz));
		int r = 1;
		VI f(N,0);
		f[0] = tarz[0].first;
		bool canReach = false;
		FOR(i,0,N)
		{
			if(r - 1 < i)
				break;
			f[i] = min(f[i], tarz[i].second);
			while(r < N && tarz[i].first + f[i] >= tarz[r].first)
			{
				f[r] = tarz[r].first - tarz[i].first;
				++r;
			}
			if(tarz[i].first + f[i] >= D)
			{
				canReach = true;
				break;
			}
		}
		printf("Case #%d: %s\n",testCase,canReach ? "YES":"NO");
	}
	
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}
