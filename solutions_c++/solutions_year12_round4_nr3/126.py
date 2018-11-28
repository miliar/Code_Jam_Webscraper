#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<iostream>
#include<cmath>
using namespace std;
const int V=100100;
int pos[V],h[V];
int _,ca,i,j,k,n,id;
int S[V],sn;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	scanf("%d",&_);
	for(ca=1;ca<=_;ca++)
	{
		scanf("%d",&n);
		for(i=1;i<n;i++)
		scanf("%d",&pos[i]);
		sn=0;S[sn++]=n;
		bool wr=false;
		for(i=n-1;i>0;i--)
		{
			while(1)
			{
				if(sn==0){wr=true;break;}
				if(S[sn-1]==pos[i])break;
				else sn--;
			}
			if(wr)break;
			S[sn++]=i;
		}
		if(!wr)
		{
			for(i=0;;i++)
			{
				for(j=1;j<=n;j++)
				h[j]=rand()%100+1;
				bool same=true;
				for(j=1;j<n;j++)
				{
					id=-1;
					for(k=j+1;k<=n;k++)
					if(id==-1||(h[k]-h[j])*(id-j)>(h[id]-h[j])*(k-j))
					id=k;
					if(id!=pos[j]){same=false;break;}
				}
				if(same)break;
			}
		}
		printf("Case #%d:",ca);
		if(wr)puts(" Impossible");
		else{for(i=1;i<=n;i++)printf(" %d",h[i]);puts("");}
	}
}
