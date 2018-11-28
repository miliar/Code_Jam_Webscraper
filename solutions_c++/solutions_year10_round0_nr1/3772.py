#include<iostream>
#include<math.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int t,n,k,s,i;
	scanf("%d",&t);
	for(i=1;i<=t;i++)
	{
		scanf("%d%d",&n,&k);
		s=pow(2.0,double(n));
		k++;
		printf("Case #%d: ",i);
		if(k%s==0)
			printf("%s\n","ON");
		else printf("%s\n","OFF");

	}
	return 0;
}