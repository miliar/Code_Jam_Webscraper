#include<iostream>
using namespace std;
int main()
{
	int i;
	int w,k;
	int n;
   freopen("D://A-large.in","r",stdin);
 	freopen("D://A-small.txt","w",stdout);
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%d %d",&w,&k);
		printf("Case #%d: ",i+1);
		if( (k&( (1<<w) -1 )) == (1<<w)-1)
		{
			printf("ON\n");
		}else printf("OFF\n");
	}

	return 0;
}