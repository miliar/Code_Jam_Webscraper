#include<cstdio>
#include<algorithm>
using namespace std;
int h[2005],l[2005];
int hh[2005],ll[2005];
bool is[2005];
int ss[2005][2005];
int main()
{
	int t,cc,n,m,ct1,ct2,a,b,i,j;
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int ux,uy,dx,dy;
	bool ok;
	int uxx,uyy,dxx,dyy;
	bool aa,bb;
	char str[10];
	scanf("%d",&t);
	for(cc=1;cc<=t;cc++)
	{
		ok=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d%s",&h[i],&l[i],str);
			hh[i]=h[i];ll[i]=l[i];
			if(str[0]=='N')
			{
				scanf("%s",str);
				is[i]=0;
			}
			else
			{
				is[i]=1;ok=1;
			}
		}
		scanf("%d",&m);
		for(i=0;i<m;i++)
		{
			scanf("%d%d",&h[i+n],&l[i+n]);
			hh[i+n]=h[i+n];
			ll[i+n]=l[i+n];
		}
		sort(hh,hh+n+m);
		sort(ll,ll+n+m);
		ct1=unique(hh,hh+n+m)-hh;
		ct2=unique(ll,ll+n+m)-ll;
		for(i=0;i<ct1;i++)
		for(j=0;j<ct2;j++)ss[i][j]=0;
		ux=uy=dx=dy=-1;
		for(i=0;i<n;i++)
		{
			a=lower_bound(hh,hh+ct1,h[i])-hh;
			b=lower_bound(ll,ll+ct2,l[i])-ll;
			if(is[i])
			{
				ss[a][b]=1;
				if(ux==-1||ux>a)
				ux=a;
				if(dx==-1||dx<a)dx=a;
				if(uy==-1||uy>b)uy=b;
				if(dy==-1||dy<b)dy=b;
			}
			else 
			{
				ss[a][b]=-1;
			}
		}
	//	printf("%d %d %d %d\n",ux,uy,dx,dy);
		printf("Case #%d:\n",cc);
		for(i=n;i<n+m;i++)
		{
			int j,k;
		//	printf("%d %d\n",h[i],l[i]);
			a=lower_bound(hh,hh+ct1,h[i])-hh;
			b=lower_bound(ll,ll+ct2,l[i])-ll;
			//printf("%d %d**\n",a,b);
			if(a>=ux&&b>=uy&&a<=dx&&b<=dy)
			{
				aa=0;
			}
			else aa=1;
			uxx=ux;uyy=uy;
			dxx=dx;dyy=dy;
			uxx<?=a;
			dxx>?=a;
			uyy<?=b;
			dyy>?=b;
			bb=1;
			for(j=uxx;j<=dxx;j++)
				for(k=uyy;k<=dyy;k++)
				{
					if(ss[j][k]==-1)
					{
						bb=0;
						break;
						
					}
				}
			if(ok==0)bb=1;
			if(aa&bb)printf("UNKNOWN\n");
			else if(bb)printf("BIRD\n");
			else printf("NOT BIRD\n");
		}
	}
	return 0;
}
