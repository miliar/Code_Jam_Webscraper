#include<iostream>
using namespace std;
struct line
{
	int st;
	int end;
}l[1000];
int main()
{
	//freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int cas,n;
    scanf("%d",&cas);
    int p=1;
    while(cas--)
    {
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%d%d",&l[i].st,&l[i].end);
		}
		long long sum=0;
		for(int i=0;i<n;i++)
		{
			for(int j=i+1;j<n;j++)
			{
				if((l[i].st-l[j].st)*(l[i].end-l[j].end)<0)
				{
					sum++;
					
				}
			}
		}
		printf("Case #%d: %lld\n",p,sum);
		p++;
	}
	return 0;
}
