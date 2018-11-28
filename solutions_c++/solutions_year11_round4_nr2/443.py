#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#define oo 505
using namespace std;

struct tp{int x,y;}A,p,s[oo][oo];
int a[oo][oo],w[oo][oo];
int n,m,d,u,v,q,D,B,Test,best;

char ss[oo];

tp ask(int x,int y,int u,int v)
{
	tp A;
	A.x=A.y=0;
	A.x=s[u][v].x-s[x-1][v].x-s[u][y-1].x+s[x-1][y-1].x;
	A.y=s[u][v].y-s[x-1][v].y-s[u][y-1].y+s[x-1][y-1].y;
	A.x-=x*a[x][y]+x*a[x][v]+u*a[u][y]+u*a[u][v];
	A.y-=y*a[x][y]+v*a[x][v]+y*a[u][y]+v*a[u][v];
	return A;
}

int ask2(int x,int y,int u,int v)
{
	return w[u][v]-w[x-1][v]-w[u][y-1]+w[x-1][y-1]-a[x][y]-a[x][v]-a[u][y]-a[u][v];
}

bool check(int x,int y,int k)
{
	if (k&1){
		u=x+k/2,v=y+k/2;
		A=ask(x,y,x+k-1,y+k-1);
		B=ask2(x,y,x+k-1,y+k-1);
		if (A.x-u*B==0 && A.y-v*B==0) return 1;
		return 0;
	}else{
		u=x+x+k-1,v=y+y+k-1;
		A=ask(x,y,x+k-1,y+k-1);
		B=ask2(x,y,x+k-1,y+k-1);
		if (A.x+A.x-u*B==0 && A.y+A.y-v*B==0) return 1;
		return 0;
	}
}

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	scanf("%d",&Test);
	for (int t=1;t<=Test;++t){
		printf("Case #%d: ",t);
		scanf("%d%d%d",&n,&m,&D);
		memset(s,0,sizeof(s));
		memset(w,0,sizeof(w));
		for (int i=1;i<=n;++i){
			p.x=p.y=0,q=0;
			scanf("%s",ss);
			for (int j=1;j<=m;++j){
				a[i][j]=ss[j-1]-'0';
				p.x+=i*a[i][j];
				p.y+=j*a[i][j];
				q+=a[i][j];
				s[i][j].x=s[i-1][j].x+p.x;
				s[i][j].y=s[i-1][j].y+p.y;
				w[i][j]=w[i-1][j]+q;
			}
		}

		best=0;
		for (int i=1;i<=n-2;++i)
		for (int j=1;j<=m-2;++j)
		for (int k=min(n-i+1,m-j+1);k>=3 && k>best;--k)
		if (check(i,j,k)){
			best=k;
			break;
		}

		if (best>=3) printf("%d\n",best);
		else puts("IMPOSSIBLE");
	}
	return 0;
}