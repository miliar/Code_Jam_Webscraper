
#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int n,k;
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	int cnt=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",cnt++);	
		if(k==((int)pow(2.0,n)-1))
			printf("ON\n");else 
		{
			int flag=1;
			int gg=(int)pow(2.0,n)-1,dd;
			for(int i=2;gg*i+i-1<=k;++i)
			{
				dd=i*gg+i-1;
				if(dd==k)
				{
					printf("ON\n");flag=0;
					break;
				}
			}
			if(flag)printf("OFF\n");
		}

	}
	return 0;
}