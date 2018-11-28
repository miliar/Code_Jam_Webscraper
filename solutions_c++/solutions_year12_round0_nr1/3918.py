#include<stdio.h>

int arr[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	int t,i;
	char c;
	scanf("%d",&t);
	getchar();
	for(i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		while((c=getchar())!='\n')
		{
			if(c==' ')
				putchar(c);
			else
				putchar(arr[c-'a']);
		}
		putchar('\n');
	}
	return 0;
}