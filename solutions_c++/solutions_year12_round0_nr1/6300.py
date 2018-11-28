
#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

int main()
{
	char arr[30] = "yhesocvxduiglbkrztnwjpfmaq";
	char str[110] = {0};
	int n;
	
	scanf("%d", &n);
	getchar();
	for(int i=0; i<n; i++)
	{
		gets(str);
		str[strlen(str)] = 0;
		char *ptr = str;
		
		while(*ptr)
		{
			if(*ptr != ' ')
				*ptr = arr[*ptr-97];
				
			ptr++;
		}
		
		printf("Case #%d: %s\n", i+1, str);
	}
	
	return 0;
}
