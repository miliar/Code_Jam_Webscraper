#include <stdlib.h>
#include <stdio.h>
#include <string.h>

bool foo(int a, int b)
{
	char arr[100];
	char brr[100];
	snprintf(arr,100,"%d%d",a,a);
	snprintf(brr,100,"%d",b);
	if(strstr(arr,brr))
		return 1;
	return 0;
}

int main()
{
	int t;
	scanf("%d\n",&t);
	for(int m=1;m<=t;++m)
	{
		int a,b;
		scanf("%d %d",&a,&b);
		int cnt = 0;
		for(int i=a;i<b;++i)
		{
			for(int j=i+1;j<=b;++j)
			{
				if(foo(i,j))cnt++;
			}
		}
		printf("Case #%d: %d\n",m,cnt);
	}
	return 0;
}
