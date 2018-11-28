#include <cstdio>
#include <algorithm>
using namespace std;
int i,j,k,s,t,n,m,T,x,y;
const int fx[4][2]={{0,1},{1,0},{0,-1},{-1,0}};
int a[6010][6010];
const int M=3000;
struct node{
	int x,y;
}n1[30000],n2[30000];
int ii,tow,tim,tot,t1,t2;
char st[50];
bool cmp(node x,node y)
{
	return x.y<y.y || x.y==y.y && x.x<y.x;
}
bool cmp1(node x,node y)
{
	return x.x<y.x || x.x==y.x && x.y<y.y;
}
main()
{
	int I=0;
	scanf("%d",&T);
	while (T--)
	{
		memset(a,0,sizeof a);
		tot=0;
		t1=t2=0;
		scanf("%d",&n);
		x=y=0;
		tow=0;
		for (ii=1;ii<=n;++ii)
		{
			scanf("%s%d",st,&tim);
			for (j=1;j<=tim;++j)
			{
				for (k=0;k<strlen(st);++k)
				switch (st[k]){
					case 'F':
						if (tow==0) {
							++t1;
							n1[t1].x=x;
							n1[t1].y=y;
						}
						else if (tow==1){
							++t2;
							n2[t2].x=x;
							n2[t2].y=y;
						}
						else if (tow==2){
							++t1;
							n1[t1].x=x;
							n1[t1].y=y-1;
						}
						else {
							++t2;
							n2[t2].x=x-1;
							n2[t2].y=y;
						}
						x+=fx[tow][0];
						y+=fx[tow][1];
						break;
					case 'L': tow=(tow+3)%4;break;
					case 'R':tow=(tow+1)%4;break;
				}
			}
		}
		sort(n1+1,n1+t1+1,cmp);
		t=0;
		for (i=2;i<=t1;++i)
		{
			if (n1[i].y==n1[i-1].y)
			{
				if (!t) t=1;
				else {
					for (j=n1[i-1].x;j<n1[i].x;++j)
					{
						a[M+j][M+n1[i].y]=1;
					}
					t=0;
				}
			}
			else t=0;
		}
		sort(n2+1,n2+t2+1,cmp1);
		t=0;
		for (i=2;i<=t2;++i)
		if (n2[i].x==n2[i-1].x)
		{
			if (!t) t=1;
			else {
				for (j=n2[i-1].y;j<n2[i].y;++j)
					a[M+n2[i].x][M+j]=1;
				t=0;
			}
		}
		else t=0;

		int ans=0;
		for (i=0;i<=6000;++i)
		for (j=0;j<=6000;++j)
			ans+=a[i][j];
		printf("Case #%d: %d\n",++I,ans);
	}
	return 0;
}
