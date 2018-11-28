#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	freopen("A-small-attempt4.in.txt","r",stdin);
	freopen("out","w",stdout);
	int t,cnt=1;
	int n,k,i;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		
		printf("Case #%d: ",cnt++);
		int res=1<<n;
		if((k+1)%res==0) 
			printf("ON\n");
		else
			printf("OFF\n");

	}


	return 0;
}
