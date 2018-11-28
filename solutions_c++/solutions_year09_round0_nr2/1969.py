#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	/*}}}*/

int cnt=0;
int cas,h,w;//flag;
int dy[4]={0,-1,1,0};
int dx[4]={-1,0,0,1};

int col[102][102], g[102][102],vis[102][102],px[102][102],py[102][102];

int validmove(int x,int y )
{
	if(x<0 || y<0 || x>=h || y>=w)
	{
		return 0;
	}

	return 1;
}


void bfs(int m,int n)
{
	queue<int> qx,qy;
	int flag=0;
//	vis[m][n]=cnt;
//	d[m][n]=0;
	qx.push(m);
	qy.push(n);
	int x,y,mx,my,tx,ty;
	while(!qx.empty() && !qy.empty())
	{
		flag=0;
		x=qx.front();
		y=qy.front();
		qx.pop();
		qy.pop();
		//vis[x][y]=1;
		int mmin=g[x][y];
		mx=x;my=y;
	
		FOR(k,0,4)
		{
			int i=x+dx[k];
			int j=y+dy[k];
			flag=0;
			if(validmove(i,j))
			{
				if(g[i][j]<mmin)
				{
					mmin=g[i][j];
					mx=i;
					my=j;
				//		c[i][j][0]=tx;
				//		c[i][j][1]=ty;
				}
		
			}
		}
		if(col[mx][my]!=-1)
		{
			col[x][y]=col[mx][my];
			while(px[x][y]!=-1 || py[x][y]!=-1)
				{
					int tx=px[x][y];
					int ty=py[x][y];
					col[tx][ty]=col[x][y];
					x=tx; y=ty;
				}

		}
		else //if(vis[mx][my]==0 )
		{	
			if(mx==x &&my==y )//|| col[mx][my]!=-1)
			{
				col[mx][my]=cnt;
				while(px[mx][my]!=-1 || py[mx][my]!=-1)
				{
					int tx=px[mx][my];
					int ty=py[mx][my];
					col[tx][ty]=col[mx][my];
					mx=tx; my=ty;
				}

				cnt++;

			}
			else
			{
				px[mx][my]=x;
				py[mx][my]=y;
				qx.push(mx);
				qy.push(my);
			}
				
		}
//		c[i][j][0]=mx;
//		c[i][j][1]=my;
/*		
				if(col[mx][my]==-1)
				{
					col[mx][my]=col[i][j];
				}
				else
				{
					if(flag==1 && (mx!=i || my!=j))
					{
						col[i][j]=col[mx][my];
						cnt--;
					}
				}	
						color[i][j]=1;
						d[i][j]=d[x][y]+1;
						pa[i][j][0]=x;
						pa[i][j][1]=y;
						qx.push(i);
						qy.push(j);
						if(i==dm && j==dn)
						{
							flag=1;
							break;
						}
					}
				}
			}
			if(flag==1)
				break;
		}

*/
		vis[x][y]=2;
		}


}
int main()
{
	cin>>cas;
	FOR(t,1,cas+1)
	{
		cin>>h>>w;
		FOR(i,0,h)
			FOR(j,0,w)
			{
				cin>>g[i][j];
				//c[i][j][0]=c[i][j][1]-1;
				col[i][j]=-1;
				px[i][j]=-1;
				py[i][j]=-1;
				vis[i][j]=0;
			}
		cout<<"Case #"<<t<<":\n";
		cnt=0;
		int mx,my;
		FOR(i,0,h)
			FOR(j,0,w)
			{
				//flag=0;
				if(col[i][j]==-1)
				{
			//		flag=1;
				//	col[i][j]=cnt;
					bfs(i,j);
				//	cnt++;
				}
			}

/*				int mmin=g[i][j];
				mx=i;my=j;
				FOR(k,0,4)
				{
					int tx=i+dx[k];
					int ty=j+dy[k];
					if(tx>=0 && tx<h && ty>=0 && ty<w)
					{
					if(g[tx][ty]<mmin)
					{
						mmin=g[tx][ty];
						mx=tx;
						my=ty;
				//		c[i][j][0]=tx;
				//		c[i][j][1]=ty;
					}
					}
				}
				if(col[mx][my]==-1)
				{
					col[mx][my]=col[i][j];
				}
				else
				{
					if(flag==1 && (mx!=i || my!=j))
					{
						col[i][j]=col[mx][my];
						cnt--;
					}
				}	
			}*/
		FOR(i,0,h)
		{
			FOR(j,0,w-1)
			{
		//		if(col[i][j]!=-1)
		//		{
		//			FOR(

				printf("%c ",'a'+col[i][j]);
	//			cout<<('a'+col[i][j])<<" ";
			}
			printf("%c\n",'a'+col[i][w-1]);
		//	cout<<col[i][w-1]<<endl;
		}
	}
	return 0;
}
