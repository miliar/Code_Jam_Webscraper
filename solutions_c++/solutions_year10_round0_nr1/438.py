#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,n,m,num,oo=1;
	cin>>t;
	while(t--)
	{
		printf("Case #%d: ",oo++);
		scanf("%d%d", &n,&m);
		m%=(1<<n);
		if(m==(1<<n)-1)
		{
			printf("ON\n");
		}
		else printf("OFF\n");
	}
}
