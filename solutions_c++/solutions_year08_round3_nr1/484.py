#include <iostream>
#include <algorithm>
using namespace std;
bool cmp(const int &a,const int &b)
{
	return a>b;
}
int main()
{
	int i,n,cs=0,p,k,t,l,fre[2000];
	int sum=0;
	scanf("%d",&n);
	while(n--)
	{
		cs++;
		scanf("%d%d%d",&p,&k,&l);
		for(i=0;i<l;i++)
			scanf("%d",&fre[i]);
		sort(fre,fre+l,cmp);
		sum=0;
		t=0;
		for(i=0;i<l;i++)
		{
			if(i%k==0)
				t++;
			sum+=fre[i]*t;
		}
		if(t>p)
			printf("Case #%d: Impossible\n",cs);
		else
			printf("Case #%d: %d\n",cs,sum);
	}
	return 0;
}