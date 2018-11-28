#include <iostream>
#include <algorithm>
using namespace std;
struct Line
{
	int a,b;
};
bool cmp(Line A,Line B)
{
	return A.a<B.a;
}
Line line[2005];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,i,n;
	int j;
	int p,q;
	scanf("%d",&t);
	for (i=1;i<=t;i++)
	{
		scanf("%d",&n);
		for (j=0;j<n;j++)
		{
			scanf("%d%d",&line[j].a,&line[j].b);
		}
		sort(line,line+n,cmp);
		int ans=0;
		for (p=0;p<n;p++)
		{
			for (q=0;q<p;q++)
			{
				if (line[p].b<line[q].b)
				{
					ans++;
				}				
			}
		}
		printf("Case #%d: %d\n",i,ans);
		
	}
	return 0;
}