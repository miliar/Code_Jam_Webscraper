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

const int MAXN = 600;

char a[MAXN][MAXN];
int ps[MAXN][MAXN];


const int UPPER_LEFT = 1<<0;
const int UPPER_RIGHT = 1<<1;
const int LOWER_LEFT = 1<<2;
const int LOWER_RIGHT = 1<<3;

const int UP = UPPER_LEFT | UPPER_RIGHT;
const int DOWN = LOWER_LEFT | LOWER_RIGHT;
const int RIGHT = UPPER_RIGHT | LOWER_RIGHT;
const int LEFT = UPPER_LEFT | LOWER_LEFT;


int di[] = {-1,-1,+1,+1};
int dj[] = {-1,+1,-1,+1};

int sum(int i0,int i1,int j0,int j1,int CUT)
{
	if(i0 > i1 || j0 > j1)
		throw 0;
	int ret = ps[i1][j1] - ps[i0-1][j1] - ps[i1][j0-1] + ps[i0-1][j0-1];
	pii corners[] = {pii(i0,j0),pii(i0,j1), pii(i1,j0), pii(i1,j1)};
	FOR(i,0,4)
		if(CUT&(1<<i))
			ret -= (a[corners[i].first-1][corners[i].second-1]-'0');
	return ret;
}


int main()
{
#ifdef HOME_PC
	//freopen ("in.txt","r",stdin);
	freopen ("B-small-attempt2.in","r",stdin);
	freopen ("B-small-attempt2.out","w",stdout);
#else
	//freopen ("input.txt","r",stdin);
	//freopen ("output.txt","w",stdout);
#endif

	int tt;
	scanf("%d",&tt);
	for(int cas = 1;cas<=tt;++cas)
	{
		int R,C,D;
		cin>>R>>C>>D;
		FOR(i,0,R)
			scanf("%s",&a[i]);

		mset(ps,0);
		FORE(i,1,R)
			FORE(j,1,C)
			ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + (a[i-1][j-1] - '0');


		int MAXK = min(R,C);

		int ans = 0;

		//// odd K
		//FORE(i,1,R)
		//	FORE(j,1,C)
		//	{
		//		int dx = 0, dy = 0;

		//		for(int k = 3; k <= MAXK; k+=2)
		//		{
		//			int d = k/2;
		//			if(i - d < 1 || i + d > R || j - d < 1 || j + d > C)
		//				continue;
		//			
		//			if(k == 3)
		//			{
		//				dx = sum(i-d,i+d,j-d,j-1,LEFT) - sum(i-d,i+d,j+1,j+d,RIGHT);
		//				dy = sum(i-d,i-1,j-d,j+d,UP) - sum(i+1,i+d,j-d,j+d,DOWN);
		//			}
		//			else
		//			{

		//			}
		//			
		//			
		//			if(dx == 0 && dy == 0)
		//				ans = max(ans,k);
		//		}
		//	}	


		//	// even K
		//	FORE(i,1,R)
		//		FORE(j,1,C)
		//		for(int k = 4; k <= MAXK; k+=2)
		//		{
		//			int d = k/2;
		//			if(i - (d-1)  < 1 || i + d > R || j - (d-1) < 1 || j + d > C)
		//				continue;
		//			int dx = sum(i-d+1,i+d,j-d+1,j,LEFT) - sum(i-d+1,i+d,j+1,j+d,RIGHT);
		//			int dy = sum(i-d+1,i,j-d+1,j+d,UP) - sum(i+1,i+d,j-d+1,j+d,DOWN);
		//			if(dx == 0 && dy == 0)
		//				ans = max(ans,k);
		//		}



		// odd K
		FORE(i,1,R)
			FORE(j,1,C)
			{


				for(int k = 3; k <= MAXK; k+=2)
				{
					int d = k/2;
					if(i - d < 1 || i + d > R || j - d < 1 || j + d > C)
						continue;
		
					int dx = 0, dy = 0;
					FORE(i0,i-d,i+d)
						FORE(j0,j-d,j+d)
					{
						if((i-d == i0 || i+d == i0) && (j-d == j0 || j+d == j0))
							continue;

						dx+=(j0-j)*(a[i0-1][j0-1]-'0');
						dy+=(i0-i)*(a[i0-1][j0-1]-'0');
					}

				
					if(dx == 0 && dy == 0)
						ans = max(ans,k);
				}
			}	


			// even K
			FORE(i,1,R)
				FORE(j,1,C)
				for(int k = 4; k <= MAXK; k+=2)
				{
					int d = k/2;
					if(i - (d-1)  < 1 || i + d > R || j - (d-1) < 1 || j + d > C)
						continue;
					double dx = 0, dy = 0;
					FORE(i0,i-d+1,i+d)
						FORE(j0,j-d+1,j+d)
					{
						if((i-d +1== i0 || i+d == i0) && (j-d+1 == j0 || j+d == j0))
							continue;

						{
							double x = j0 > j ? j0 -j - .5: -(j-j0+1) + .5;
							dx+=x*(a[i0-1][j0-1]-'0');
						}
						{
							double y = i0 > i ? i0 -i - .5: -(i-i0+1) + .5;
							dy+=y*(a[i0-1][j0-1]-'0');
						}

					}


					if(fabs(dx) < eps && fabs(dy) < eps)
						ans = max(ans,k);
				}
		

		printf("Case #%d: ",cas);
		if(ans)
			printf("%d\n",ans);
		else
			printf("IMPOSSIBLE\n");
		
	}
#ifdef HOME_PC
	cerr<<endl<<"Execution time = "<<clock()<<" ms"<<endl;
#endif
	return 0;
}

