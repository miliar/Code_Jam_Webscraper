#include <iostream>
using namespace std;

int main()
{
	freopen("D-large.in","rt",stdin);
	freopen("outLarge.txt","wt",stdout);
	int t;
	scanf("%d",&t);
	//int m[2000];
	for(int i=1;i<=t;i++)
	{
		//memset(m,0,sizeof(m));
		int n,k=0;
		scanf("%d",&n);
		for(int j=1;j<=n;j++)
		{
			int a;
			scanf("%d",&a);
			if(a!=j) k++;
		}
		printf("Case #%d: %lf\n",i,double(k));
	}
	fclose(stdout);
}



