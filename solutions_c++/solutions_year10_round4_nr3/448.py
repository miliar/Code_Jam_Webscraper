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


typedef pair<int,int> pii;
typedef long long i64;
typedef vector<int> VI; typedef vector< vector<int> > VVI;
typedef vector<string> VS;

const int inf = 1<<25;
const double eps = 1e-9;

const int MAXN = 200;
char a[MAXN][MAXN];

const char NONE = '0';
const char DEAD = '2';
const char BORN = '3';
const char ALIVE = '1';

bool was_alive(int i,int j)
{
	return a[i][j] == ALIVE || a[i][j] == DEAD;
}
bool was_dead(int i,int j)
{
	return a[i][j] == BORN ||a[i][j] == NONE;
}

int main()
{
	freopen ("C-small-attempt0.in","r",stdin);
	//freopen ("in.txt","r",stdin);
	freopen ("output.txt","w",stdout);
	
	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		mset(a,NONE);
		int R;
		cin>>R;
		FOR(i,0,R)
		{
			int x1,y1,x2,y2;
			cin>>x1>>y1>>x2>>y2;
			FORE(i,y1,y2)
				FORE(j,x1,x2)
				a[i][j] = ALIVE;
		}

		int t = 0;
		
		for(;;)
		{
			bool has_alive = false;
			FOR(i,1,MAXN)
				FOR(j,1,MAXN)
				if(a[i][j] == NONE && was_alive(i-1,j) && was_alive(i,j-1))
					a[i][j] = BORN;
				else
					if(a[i][j] == ALIVE && was_dead(i-1,j) && was_dead(i,j-1))
						a[i][j] = DEAD;
			FOR(i,1,MAXN)
				FOR(j,1,MAXN)
				if(a[i][j] == BORN)
					a[i][j] = ALIVE;
				else 
					if(a[i][j] == DEAD)
						a[i][j] = NONE;

			FOR(i,1,MAXN) FOR(j,1,MAXN)
				if(a[i][j] == ALIVE)
				{
					has_alive = true;
					goto out;
				}
out:	++t;
		if(!has_alive)
				break;
		}


		printf("Case #%d: %d\n",cas,t);
	}

	return 0;
}

