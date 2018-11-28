#include<iostream>
using namespace std;

const int SIZE=1000;
int a[SIZE],b[SIZE];

int main()
{
	int ncase,tcase;
	int i,j,n,ans;
	scanf("%d",&ncase);
	for(tcase=1;tcase<=ncase;tcase++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d%d",&a[i],&b[i]);
		}
		ans=0;
		for(i=0;i<SIZE;i++)
		{
			for(j=i+1;j<SIZE;j++)
			{
				if((a[i]-a[j])*(b[i]-b[j])<0)
					ans++;
			}
		}
		printf("Case #%d: %d\n",tcase,ans);
	}
	return 0;
}