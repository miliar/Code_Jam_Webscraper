#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	int tcase,ncase;
	int ans,i;
	int l,p,c;
	scanf("%d",&ncase);
	for(tcase=1;tcase<=ncase;tcase++)
	{
		scanf("%d%d%d",&l,&p,&c);
		i=ceil(log((double)p/l)/log(c));
		ans=ceil(log(i)/log(2));
		printf("Case #%d: %d\n",tcase,ans);
	}
	return 0;
}
