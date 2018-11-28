#include<stdio.h>
#include<string.h>
#define MAX 200
int main()
{
	char key[]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int testCases;
	
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.txt","w",stdout);

	scanf("%d",&testCases);
	while(getchar()!='\n');//to eat the ENTER char
	char a[testCases][MAX];
	for(int i=0;i<testCases;i++)
		fgets(a[i],MAX,stdin);
	for(int i=0;i<testCases;i++)
	{
		printf("Case #%d: ",i+1);
		for(int j=0;j< strlen(a[i])-1; j++)
		{
			if(a[i][j]==' ')
				printf(" ");
			else
				printf("%c",key [ a[i][j] - 'a']);
		}
		printf("\n");
	}
	//for(int i=0;i<testCases;i++)
	//	printf("\nCase #%d: %s\n",i+1,a[i]);
	return 0;
}
