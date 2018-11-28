#include<stdio.h>
#include<algorithm>
using namespace std;

struct fp
{
	int data,pos;
	friend bool operator < (fp a,fp b)
	{
		return a.data<b.data;
	}
}star1[100001],star2[100001];

int b[100001];
int hash[100001],hash2[100001];
int main()
{
	int t,bk,n,i,j,k,snake=0;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for(bk=1;bk<=t;++bk)
	{
		int ans=0;
		snake++;
		scanf("%d",&n);
		for(i=0;i<n;++i)
		{
			scanf("%d%d",&star1[i].data,&star2[i].data);
			star1[i].pos=star2[i].pos=i;
			b[i]=star2[i].data;
		}
		sort(star1,star1+n);
		sort(star2,star2+n);
		for(j=0,k=0;j<n;++ans)
		{
			if(star2[j].data<=k)
			{
				if(hash2[star2[j].pos]==snake)
					k++;
				else
					k+=2;
				hash[star2[j].pos]=snake;
				j++;
			}
			else
			{
				int maxb=-1,maxi;
				for(i=0;i<n&&star1[i].data<=k;++i)
				{
					fp now=star1[i];
					if(hash[now.pos]!=snake&&hash2[now.pos]!=snake&&b[now.pos]>maxb)
						maxb=b[now.pos],maxi=now.pos;
				}
				if(maxb==-1)
					break;
				hash2[maxi]=snake;
				k++;
			}
		}
		printf("Case #%d: ",bk);
		if(j<n)
			printf("Too Bad\n");
		else
			printf("%d\n",ans);
	}
	return 0;
}
