#include<cstdio>
#include<algorithm>
using namespace std;
int T,n,w,h,num,snum,l,k,x[1111],y[1111],a[1111],b[1111],xx[1111],yy[1111];

struct node
{
	int w,p;
}
r[1111];

bool cmp(node a,node b)
{
	return a.w<b.w;
}

int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for (int tt=1; tt<=T; tt++)
	{
		scanf("%d%d%d",&n,&w,&h);
		for (int i=1; i<=n; i++)
		{
		    scanf("%d",&r[i].w);
	        r[i].p=i;
		}
		sort(r+1,r+n+1,cmp);
		printf("Case #%d:",tt);
		num=snum=0; l=0; k=0;
		for (int i=1; i<=n; i++)
		{
			if (l==0)
			    y[i]=0;
			else
			    y[i]=l+r[i].w;
			if (num==0)
			    x[i]=0;
			else
			{
				for (; k<=num; k++)
				{
					x[i]=x[a[k]]+r[a[k]].w+r[i].w;
					if (y[a[k]]>y[i]+r[i].w)
					    break;
			    }
		    }
			l=y[i]+r[i].w;
			b[++snum]=i;
			if (l+r[i+1].w>h)
			{
				num=snum; l=0; k=1; snum=0;
				memcpy(a,b,sizeof b);
		    }
	    }
	    for (int i=1; i<=n; i++)
	        xx[r[i].p]=x[i],yy[r[i].p]=y[i];
	    for (int i=1; i<=n; i++)
	        printf(" %d %d",xx[i],yy[i]);
	    printf("\n");
    }
}
