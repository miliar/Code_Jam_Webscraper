#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;
int t,i,j,k,l,m,n,place[5001],d[100],p;
bool isc[5001];
int main()
{
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	scanf("%d\n",&t);
	for(m=1;m<=t;m++)
	{
		scanf("%d%d",&k,&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&d[i]);
		}
		p=1;
		for(i=1;i<=k;i++) {isc[i]=true;}
		for(i=1;i<=k;i++)
		{
			l=1;
			while(l!=i)
			{
				p++;
				if (p>k) {p=1;}
				if (isc[p])
				{
					l++;
				}				
			}
			place[p]=i;
			isc[p]=false;
			if (i!=k)
			{
				while (!isc[p])
				{
					p++;
					if (p>k) {p=1;}
				}
			}
		}
		printf("Case #%d:",m);
		for(i=0;i<n;i++)
		{
			printf(" %d",place[d[i]]);
		}
		printf("\n");
	}
	return 0;
}