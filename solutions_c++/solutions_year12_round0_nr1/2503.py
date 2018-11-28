#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
	char c[27]="yhesocvxduiglbkrztnwjpfmaq";
	//char c[27]="ynficwlbkuomxsevzpdrjgthaq";
	//		    abcdefghijklmnopqrstuvwxyz
	int h;
	char cc[300]={},b[1];
	scanf("%d",&h);
	gets(b);
	for(int k=1;k<=h;k++)
	{
		printf("Case #%d: ",k);
		cin.getline(cc,300);
		for(int i=0;1;i++)
		{
			if(cc[i]=='\0'){printf("\n");break;}
			if(cc[i]==' ')printf(" ");
			else printf("%c",c[(int)cc[i]-97]);
		}
	}
	return 0;
}
