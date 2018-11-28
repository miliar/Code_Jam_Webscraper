#include<iostream>
using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w+",stdout);
	int num,change,T,cas,tot;			
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		scanf("%d%d",&num,&change);
		tot=(1<<num);
		change=change%tot;
		if(tot==change+1)
			printf("Case #%d: ON\n",cas);
		else
			printf("Case #%d: OFF\n",cas);
	}
	return 0;
}
