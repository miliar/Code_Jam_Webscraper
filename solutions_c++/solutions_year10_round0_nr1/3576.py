#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T,count=1;
	int i,k,n;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&k);
		
		printf("Case #%d: ",count++);

		if((k+1)%(1<<n)==0) 
			printf("ON");
		else
			printf("OFF");

		printf("\n");

	}


	return 0;
}