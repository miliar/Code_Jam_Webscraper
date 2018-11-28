#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<cstring>
using namespace std;
char map[30] = "yhesocvxduiglbkrztnwjpfmaq";
int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("output.out","w",stdout);
	int n ,i , j;
	scanf("%d",&n);
	getchar();
	for(i = 0 ; i < n ; i ++)
	{
		char a[1000];
		
		gets(a);
		int aa = strlen(a);
		printf("Case #%d: ",i+1);
		for(j = 0 ; j < aa ;j ++)
		{
			if(a[j] == ' ')
				printf(" ");
			else
				printf("%c",map[a[j]-'a']);
		}
		printf("\n");
	}
	return 0;
}
