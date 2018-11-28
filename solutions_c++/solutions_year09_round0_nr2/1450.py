#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <string>
#include <functional>
#include <sstream>
#include <fstream>
using namespace std;
#define FOR(i,a,b) for (i=(a);i<=(b);i++)
#define fori(it,v) for (it=(v).begin();it!=(v).end();it++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define all(c) c.begin(),c.end()
#define pf push_front
#define popb pop_back
#define popf pop_front
typedef pair<int,int> ii;
FILE *in,*out;
int nr,a[110][110],c[110][110],n,m;
const int inf=1<<30;
const int dx[]={-1,0,0,1};
const int dy[]={0,-1,1,0};
bool ver(int x,int y)
{
	if (x<1||x>n||y<1||y>m)
		return false;
	return true;
}
void sink(int x,int y)
{
	fflush(stdout);
	ii next=mp(inf,inf);
	int i,x2,y2;
	FOR(i,0,3)
	{
		x2=x+dx[i];
		y2=y+dy[i];
		if (ver(x2,y2)&&a[x2][y2]<a[x][y])
		{
			if (next==mp(inf,inf))
				next=mp(x2,y2);
			else
				if(a[next.fi][next.se]>a[x2][y2])
					next=mp(x2,y2);
		}
	}
	if (next==mp(inf,inf))
	{
		nr++;
		c[x][y]=nr;
		return;
	}
	if (!c[next.fi][next.se])
		sink(next.fi,next.se);
	c[x][y]=c[next.fi][next.se];
}
int main()
{
	int i,t,T,j;
	in=fopen("test.in","r");
	out=fopen("test.out","w");
	fscanf(in,"%d",&t);
	FOR(T,1,t)
	{
		fscanf(in,"%d%d",&n,&m);
		memset(a,0,sizeof(a));
		memset(c,0,sizeof(c));
		nr='a'-1;
		FOR(i,0,103)
			a[0][i]=a[i][0]=inf;
		FOR(i,1,n)
			FOR(j,1,m)
				fscanf(in,"%d",&a[i][j]);
		FOR(i,1,n)
			FOR(j,1,m)
				if(!c[i][j])
					sink(i,j);
		fprintf(out,"Case #%d:\n",T);
		FOR(i,1,n)
		{
			FOR(j,1,m-1)
				fprintf(out,"%c ",c[i][j]);
			fprintf(out,"%c\n",c[i][m]);
		}
	}
	fclose(in);
	fclose(out);
        return 0;
}
