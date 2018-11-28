#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)
#define F(i,n) for (int i=0;i<n;i++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

int mv[4][2]=
{
		{-1,0},
		{0,-1},
		{0,1},
		{1,0}
};

int T,H,W;
int a[128][128];
int r[128][128];
int to[128][128];
vector<PI> from[128][128];

void dfs(int id,int x,int y)
{
	if (r[x][y]>-1) return;
	r[x][y]=id;
	Repi(from[x][y].SZ)
	 dfs(id,from[x][y][i].x,from[x][y][i].y);
}

char mp[29];

int main()
{
    scanf("%d",&T);
    F(xx,T)
     {
			scanf("%d%d",&H,&W);
			Repi(H)
			 Repj(W)
			  {
			  	scanf("%d",&a[i][j]);
			  	from[i][j].clear();
			  }
			memset(r,-1,sizeof(r));
			
			//cout<<"\n\n\ncase "<<xx<<"\n";
			cout<<"Case #"<<xx+1<<":\n";
			Repi(H)
			 Repj(W)
			  {
					to[i][j]=-1;
					int alt=1000000;
					Repk(4)
					 {
							int x=i+mv[k][0],y=j+mv[k][1];
							if (x<0 || x>=H || y<0 || y>=W) continue;
							if (a[x][y]<alt && a[x][y]<a[i][j]) alt=a[x][y],to[i][j]=k;
					 }
					if (to[i][j]>-1)
					 {
							int x=i+mv[to[i][j]][0],y=j+mv[to[i][j]][1];
							from[x][y].PB(MP(i,j));
					//		cout<<"					from "<<i<<" "<<j<<" to "<<x<<" "<<y<<"\n";
					 }
			  }
		
			int cnt=0;
			Repi(H)
			 Repj(W)
			  if (r[i][j]==-1 && to[i][j]==-1)
			   dfs(cnt++,i,j);
			
			//Repi(H)			 {						Repj(W)						 cout<<setw(3)<<r[i][j]; cout<<"\n";				}
			
			memset(mp,-1,sizeof(mp));
			char alph='a';
			Repi(H)
			 Repj(W)
			  if (mp[r[i][j]]==-1)
			   mp[r[i][j]]=alph++;
			
			Repi(H)
			 {
			   Repj(W-1)
			    printf("%c ",mp[r[i][j]]);
			   printf("%c\n",mp[r[i][W-1]]);
			 }
	 }
    return 0;
}
