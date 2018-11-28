#include<iostream>
using namespace std;
int a[1001];
int main()
{
	freopen("in.txt","rt",stdin);
	freopen("D_large.txt","wt",stdout);
	int TC,i,n;
	scanf("%d",&TC);
	for(int tc = 0;tc<TC;tc++)
	{
		scanf("%d",&n);
		double c=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",a+i);
			if(a[i] != i+1) c++;
		}
		printf("Case #%d: %.6lf\n",tc+1,c);

	}
	return 0;
}