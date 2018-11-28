#include <cstdio>
using namespace std;
#define oo 1000000000
const int d[]={-1,0,1};
const int maxn=105,size=1048575;
struct Tnode
{
	int x,y,z;
}	Q[size+1];
int f[maxn][maxn][maxn],p[maxn],x,y,z,head,tail,test,n,ans;
bool inQ[maxn][maxn][maxn];
char s[10],c[maxn];

inline void Update(int u,int v,int w)
{
	if (1<=v&&v<=100&&1<=w&&w<=100&&f[x][y][z]+1<f[u][v][w])
	{
		f[u][v][w]=f[x][y][z]+1;
		if (!inQ[u][v][w])
		{
			tail=(tail+1)&size;
			Q[tail].x=u;
			Q[tail].y=v;
			Q[tail].z=w;
			inQ[u][v][w]=1;
		}
	}
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	
	scanf("%d",&test);
	for (int kase=1;kase<=test;kase++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			scanf("%s",s);
			if (s[0]=='O') c[i]='O'; else c[i]='B';
			scanf("%d",&p[i]);
		}
		for (int i=0;i<=n;i++)
		for (int j=1;j<=100;j++)
		for (int k=1;k<=100;k++)
		{
			inQ[i][j][k]=0;
			f[i][j][k]=oo;
		}
		f[0][1][1]=0;
		Q[1].x=0;
		Q[1].y=Q[1].z=1;
		inQ[0][1][1]=1;
		for (head=0,tail=1;head!=tail;)
		{
			head=(head+1)&size;
			x=Q[head].x;
			y=Q[head].y;
			z=Q[head].z;
			for (int d1=0;d1<3;d1++)
			for (int d2=0;d2<3;d2++)
				Update(x,y+d[d1],z+d[d2]);
			if (x<n)
			{
				if (c[x+1]=='O'&&p[x+1]==y)
					for (int d2=0;d2<3;d2++)
						Update(x+1,y,z+d[d2]);
				if (c[x+1]=='B'&&p[x+1]==z)
					for (int d1=0;d1<3;d1++)
						Update(x+1,y+d[d1],z);
			}
			inQ[x][y][z]=0;
		}
		ans=oo;
		for (int j=1;j<=100;j++)
		for (int k=1;k<=100;k++)
			if (f[n][j][k]<ans) ans=f[n][j][k];
		printf("Case #%d: %d\n",kase,ans);
	}
	
	return 0;
}
