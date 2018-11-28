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

bool won(const VS& board, char c)
{
	int di[] = {1,0,1,1};
	int dj[] = {0,1,1,-1};

	FOR(i,0,4) FOR(j,0,4) FOR(k,0,4)
	{
		FOR(d,0,4)
		{
			int ni = i + di[k] * d;
			int nj = j + dj[k] * d;
			if(ni < 0 || nj < 0 || ni > 3 || nj > 3 || board[ni][nj] != c && board[ni][nj] != 'T')
				break;
			if(d == 3)
				return true;
		}
	}
	return false;
}

int main()
{
#ifdef HOME_PC
	freopen ("A-large.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("A-large.out","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		VS a(4);
		int spaceCount = 0;
		FOR(i,0,4)
			cin>>a[i], spaceCount += count(ALL(a[i]), '.');

		string ans = "";
		if(won(a,'X'))
		{
			ans = "X won";
		}
		else if(won(a,'O'))
		{
			ans = "O won";
		}
		else
		{
			ans = ((spaceCount > 0) ? "Game has not completed" : "Draw");
		}

		printf("Case #%d: %s\n",cas,ans.c_str());
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

