#include<stdio.h>
#include<iostream>
using namespace std;
#include<string.h>
int main()
{
	char a[]="yhesocvxduiglbkrztnwjpfmaq";
	
	int t;
	int j,i;
	scanf("%d",&t);
	cin.ignore();
	for(j=1;j<=t;j++){
//		printf("\nCase #%d: ",j);
		char b[102];
		cin.getline(b,102);
                printf("Case #%d: ",j);

		for(i=0;b[i]!=0;i++){
			if(b[i]==' ')
				printf(" ");
			else
				printf("%c",a[b[i]-97]);
		}
	printf("\n");	
	}
	return 0;
}
