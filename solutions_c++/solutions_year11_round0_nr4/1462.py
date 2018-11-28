#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;//

int main()
{
	freopen("D.txt","w",stdout);
	int n,t,i,a,k;
	double num;
	scanf("%d",&t);
	k=t;
	while(t--)
	{
		num=0;
		scanf("%d",&n);
		for(i=1;i<=n;i++)
		{
			scanf("%d",&a);
			if(a!=i)
				num++;
		}
		printf("Case #%d: %.6lf\n",k-t,num);
	}return 0;
}