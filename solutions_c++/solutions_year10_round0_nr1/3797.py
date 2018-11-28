#include<iostream>
using namespace std;
int main()
{
	//freopen("A-large.in","r",stdin);
	//freopen("out.out","w",stdout);//

	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		int n,k;
		scanf("%d %d",&n,&k);
		int na=1<<n;
		int nb=na-1;
		printf("Case #%d: ",i);
		if(nb>k)
			puts("OFF");
		else
		{
			int cha=k-nb;
			if(cha%na==0)
				puts("ON");
			else
				puts("OFF");
		}
	}
}