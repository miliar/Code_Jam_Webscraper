#include<iostream>
using namespace std;
int main()
{
	int i,j,t,n,p,s,ans;
	int score;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		ans=0;
		scanf("%d%d%d",&n,&s,&p);
		for(j=0;j<n;j++)
		{
			scanf("%d",&score);
			if(score>=3*p-2&&score>=p)
			ans++;
			else
			if((score==3*p-3||score==3*p-4)&&s>0&&score>=p)
			{
				ans++;
				s--;
			}
		}
		printf("Case #%d: %d\n",i,ans);
	}
	getchar();
}
