// AAA
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<iomanip>
using namespace std;


int X,S,R,tt,N;
struct NODE
{
	int ll,rr;
	int w;
}nod[10000];
bool cmp1(NODE a,NODE b)
{
	return a.ll<b.ll;
}
bool cmp2(NODE a,NODE b)
{
	return a.w<b.w;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;scanf("%d",&T);
	int CN=0;
	
	while(T--)
	{
		scanf("%d%d%d%d%d",&X,&S,&R,&tt,&N);
		for(int i=1;i<=N;i++) scanf("%d%d%d",&nod[i].ll,&nod[i].rr,&nod[i].w);
		sort(&nod[1],&nod[N+1],cmp1);
		
		int total=nod[1].ll-0;
		for(int i=2;i<=N;i++) total+=(nod[i].ll-nod[i-1].rr);
		total+=X-nod[N].rr;
		
		nod[++N].w=0;
		nod[N].ll=0;nod[N].rr=total;
		
		sort(&nod[1],&nod[N+1],cmp2);
		
		
		double ans=0,tim=tt+0.0;
		for(int i=1;i<=N;i++)
		{
			double len=nod[i].rr-nod[i].ll;
			double vv=R+nod[i].w;
			
			if(tim*vv>len)
			{
				ans+=len/vv;
				tim-=len/vv;
			}
			else
			{
				ans+=tim;
				len-=(tim*vv);
				
				vv=S+nod[i].w;
				ans+=len/vv;
				
				for(int j=i+1;j<=N;j++)
				{
					len=nod[j].rr-nod[j].ll;
					vv=S+nod[j].w;
					ans+=len/vv;
				}
				break;
			}
		}
		printf("Case #%d: %.7f\n",++CN,ans);
	}
    
    //system("pause");
    return 0;
}
