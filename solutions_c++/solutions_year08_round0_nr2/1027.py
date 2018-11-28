#include<stdio.h>
#include<algorithm>
using namespace std;
struct tt
{
	int w;
	bool f;
	bool operator <(const tt &o)const
	{
		return w<o.w;
	}
}z[200+16],h[200+16];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int c,o,t,n,m,a1,b1,a2,b2,a,b,x,y,i,j;
	scanf("%d",&c);
	for(o=1;o<=c;o++)
	{
		scanf("%d%d%d",&t,&n,&m);
		for(i=0;i<n+m;i++)
		{
			scanf("%d:%d%d:%d",&a1,&b1,&a2,&b2);
			a1=a1*60+b1;
			a2=a2*60+b2+t;
			z[i].w=a1;
			h[i].w=a2;
			if(i<n)
			{
				z[i].f=false;
				h[i].f=true;
			}
			else
			{
				z[i].f=true;
				h[i].f=false;
			}
		}
		sort(z,z+n+m);
		sort(h,h+n+m);
		x=0;
		y=0;
		a=0;
		b=0;
		j=0;
		for(i=0;i<n+m;i++)
		{
			while(j<n+m&&h[j].w<=z[i].w)
			{
				if(h[j].f)
					b++;
				else
					a++;
				j++;
			}
			if(z[i].f)
			{
				if(!b)
					y++;
				else
					b--;
			}
			else
			{
				if(!a)
					x++;
				else
					a--;
			}
		}
		printf("Case #%d: %d %d\n",o,x,y);
	}
	return 0;
}

