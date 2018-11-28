#include <iostream>
using namespace std;
struct node 
{
	int l,r;
};
node map[1005];
int main ()
{
	freopen("al.txt","r",stdin);
	freopen("ansl.txt","w",stdout);
	int T;
	int t,p,sum,ll,rr,n,i;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		p=0;
		scanf("%d",&n);
		sum=0;
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&ll,&rr);
			for(i=0;i<p;i++)
			{
				if((ll>map[i].l&&rr<map[i].r)||(ll<map[i].l&&rr>map[i].r))sum++;
			}
			map[p].l=ll;
			map[p++].r=rr;
		}
		printf("Case #%d: %d\n",t,sum);
	}
}