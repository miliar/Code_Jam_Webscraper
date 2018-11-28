#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
	//freopen("snapper.in","r",stdin);
//	freopen("snapper.out","w",stdout);
	int cs,n,k;
	scanf("%d",&cs);	
	for(int t=1;t<=cs;++t)
	{		
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",t);
		k&=((1<<n)-1);
		if(k==(1<<n)-1)	 printf("ON\n");
		else printf("OFF\n");
	}
}
