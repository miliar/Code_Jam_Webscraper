#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<algorithm>
using namespace std;
int n,m,map[510][510];
double AB(double x)
{if(x<0)return -x;return x;}
const double eps=1e-8;
bool check(int x)
{
	double dx,dy,td,tx,ty,cx,cy;
	for(int i=0;i+x-1<n;i++)
	for(int j=0;j+x-1<m;j++)
	{
		dx=0.0;dy=0.0;
		cx=(double)i+(double)x/2.0;
		cy=(double)j+(double)x/2.0;
		for(int ii=0;ii<x;ii++)
		for(int jj=0;jj<x;jj++)
		{
			if(ii==0&&jj==0)continue;
			if(ii==x-1&&jj==0)continue;
			if(ii==0&&jj==x-1)continue;
			if(ii==x-1&&jj==x-1)continue;
			td=(double)map[i+ii][j+jj];
			tx=(double)(i+ii)+0.5;
			ty=(double)(j+jj)+0.5;
			dx+=td*(tx-cx);dy+=td*(ty-cy);
		}
	//	printf("%d %.3f %.3f\n",x,dx,dy);
		if(AB(dx)<eps&&AB(dy)<eps)return true;
	}
	return false;
}
int D,i,j,_,ca,K;
char ch[510];
int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	scanf("%d",&_);ca=0;
	while(_--)
	{
		ca++;
		scanf("%d%d%d",&n,&m,&D);
		for(i=0;i<n;i++)
		{
			scanf("%s",ch);
			for(j=0;j<m;j++)
			{
				map[i][j]=ch[j]-'0';
				map[i][j]+=D;
			}
		}
		K=min(n,m);
		bool can=false;
		while(1)
		{
			if(K<=2)break;
			if(check(K)){can=true;break;}
			else K--;
		}
		printf("Case #%d: ",ca);
		if(!can)puts("IMPOSSIBLE");
		else printf("%d\n",K);
	}
}
