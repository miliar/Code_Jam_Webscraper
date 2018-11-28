#include<stdio.h>
#include<cstring>
#include<cmath>
#include<fstream>
using namespace std;
int t,n,k,nu[50];
int main()
{
	
	freopen("ans.out","w",stdout);
	//t=gn();
	freopen("A-large.in","r",stdin);
	scanf("%d",&t);
	int co=0,a=0;
	while(t--)
	{
		co++;
		scanf("%d %d",&n,&k);
		//n=gn();
		//k=gn();
		//a+=k;
		//k=a;
		memset(nu,0,sizeof(nu));
		for(int i=0;i<33&&k!=0;i++)
		{
			nu[i]=k%2;
			k/=2;
		}
		bool f=true;
		for(int i=0;i<n;i++)
			if(nu[i]==0){f=false;break;}
		if(f)
			printf("Case #%d: ON\n",co);
		else
			printf("Case #%d: OFF\n",co);
	}
	scanf(" ");
	return 0;
}
