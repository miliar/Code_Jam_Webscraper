#include <iostream>
#include <string.h>
using namespace std;
int main()
{
	int t;
	int n,k;
	int cas=0;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		cas++;
		printf("Case #%d: ",cas); 
		scanf("%d %d",&n,&k);
		while(k)
		{
			if(k%2==0)break;
			else n--;
			if(!n)break;
			k/=2;
		}
		if(!n)puts("ON");
		else puts("OFF");
	}
	return  0;
}