#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int n,k;
	int t;
	scanf("%d",&t);
	int num=0;
	while(t--)
	{
		
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",++num);
		int temp=pow(2,n);
		int temp1=temp-1;
		if(k==0)
		{
			printf("OFF\n");
			continue;
		}
		
		if((k%temp)==temp1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}



