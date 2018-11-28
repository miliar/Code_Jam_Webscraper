#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define MAXN 1000010
#define eps 1e-10
struct Seg
{
	int L;
	int R;
	int W;
};
int nb[MAXN*2],flag[MAXN];
Seg seg[MAXN];
int n,S,R,cnt;
double T;
int m;
bool cmp(Seg A1,Seg A2)
{
	return A1.W<A2.W;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k,len,t,tcas;
	double res,cost;
	double v;
	scanf("%d",&t);
	for(tcas=1;tcas<=t;tcas++)
	{
		scanf("%d%d%d%lf%d",&len,&S,&R,&T,&n);
		memset(flag,0,sizeof(flag));
		m=0;
		cnt=0;
		nb[++m]=0;
		nb[++m]=len;
		for(i=1;i<=n;i++)
		{
			scanf("%d%d",&j,&k);
			nb[++m]=j;
			nb[++m]=k;
			scanf("%d",&k);
			flag[j]=k;
		}
		sort(nb+1,nb+m+1);
		m=unique(nb+1,nb+m+1)-nb-1;
		for(i=1;i<m;i++)
		{
			cnt++;
			seg[cnt].L=nb[i];
			seg[cnt].R=nb[i+1];
			seg[cnt].W=flag[nb[i]];
		}
		sort(seg+1,seg+cnt+1,cmp);
		res=0;
		for(i=1;i<=cnt;i++)
		{
			if(T<eps)res+=(seg[i].R-seg[i].L+0.0)/(S+seg[i].W);
			else
			{
				v=R+seg[i].W;
				cost=(seg[i].R-seg[i].L)/v;
				if(cost<=T)
				{
					T-=cost;
					res+=cost;
				}else
				{
					res+=T+(seg[i].R-seg[i].L-v*T)/(S+seg[i].W);
					T=-100;
				}
			}
		}
		printf("Case #%d: %.8f\n",tcas,res);
	}
	return 0;
}
