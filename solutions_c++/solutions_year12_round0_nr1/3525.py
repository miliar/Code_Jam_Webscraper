#include<stdio.h>

using namespace std;

int main()
{

 char arr[] = {'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
 int i,t,r;
 char str[105];

 scanf("%d",&t);
 
 getchar();

 r = 1;

 while(t--)
 {
	gets(str);

	printf("Case #%d: ",r);

 	for(i=0;str[i]!='\0';i++)
	{
		if(str[i]==' ')
			printf("%c",str[i]);
		else
		{
			printf("%c",arr[str[i]-97]);	
		}
	}

 	printf("\n");
	
	r++;
 }

}

 
