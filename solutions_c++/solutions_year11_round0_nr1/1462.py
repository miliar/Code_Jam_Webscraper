#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;
#define M 210

struct status
{
	int p,id;
}o[M],b[M];

int n;
char s[5];
int on,bn;
int op,bp;

int ab(int x)
{
	if(x<0)
		return -x;
	return x;
}

int main()
{
	int i,j,k,t,tc=1;
	int ans,dk;
	freopen("out.txt","w",stdout);
	freopen("gcj/A-large.in","r",stdin);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		on=0;bn=0;
		for(i=0;i<n;i++)
		{
			scanf("%s%d",s,&k);
			if(s[0]=='B')
			{
				b[bn].p=k;
				b[bn].id=i;
				bn++;
			}
			else
			{
				o[on].p=k;
				o[on].id=i;
				on++;
			}
		}
		op=1,bp=1;ans=0;
		i=0;j=0;
		while(i<bn||j<on)
		{
			if(i==bn)
			{
				ans+=ab(op-o[j].p)+1;
				op=o[j].p;
				j++;
				continue;
			}
			if(j==on)
			{
				ans+=ab(bp-b[i].p)+1;
				bp=b[i].p;
				i++;
				continue;
			}
			if(b[i].id<o[j].id)
			{
				k=ab(b[i].p-bp)+1;
				ans+=k;
				bp=b[i].p;
				dk=ab(o[j].p-op);
				if(dk<=k)
					op=o[j].p;
				else
				{
					if(o[j].p<op)
						op-=k;
					else
						op+=k;
				}
				i++;
				continue;
			}

			else
			{
				k=ab(o[j].p-op)+1;
				ans+=k;
				op=o[j].p;
				dk=ab(b[i].p-bp);
				if(dk<=k)
					bp=b[i].p;
				else
				{
					if(b[i].p<bp)
						bp-=k;
					else
						bp+=k;
				}
				j++;
				continue;
			}
		}
		printf("Case #%d: ",tc++);
		printf("%d",ans);
		putchar(10);
	}
	return 0;
}


