#include <iostream>
#include <vector>
using namespace std;

int main()
{
	freopen("C-large.in","rt",stdin);
	freopen("outLarge.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int n;
		scanf("%d",&n);
		vector<int> c(n);
		vector<int> p(22,0);
		int min=10000007;
		int sum=0;
		for(int j=0;j<n;j++)
		{
			int u;
			scanf("%d",&u);
			c[j]=u;
			sum+=u;
			if(min>u) min=u;
			for(int k=0;k<=20;k++)
			{
				p[k]+=u%2;
				u/=2;
			}
		}
		printf("Case #%d: ",i);
		int yes=1;
		for(int k=0;k<=20;k++)
			if(p[k]%2) yes=0;
		if(yes)
			printf("%d\n",sum-min);
		else
			printf("NO\n");
	}
	fclose(stdout);
}


			
			




