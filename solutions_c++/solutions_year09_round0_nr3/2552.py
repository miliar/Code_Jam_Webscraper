#include <stdio.h>
#include <stdlib.h>
int count=0;
void find(char *p,char *str,int i,int j)
{
	if(str[j]=='\0')
	{
		if(p[i]=='\0')
			count++;
		return;
	}
	if(p[i]=='\0')
	{
		count++;
		return;
	}
	if(str[j]==p[i])
	{
		find(p,str,i+1,j+1);
		find(p,str,i,j+1);
	}
	else
	{
		find(p,str,i,j+1);
	}
}

main()
{
	int i,j,k;
	char str[500];

	int n;
	FILE *in=fopen("in","r");

	FILE *ou=fopen("ou","w");

	fscanf(in,"%d",&n);

	char *p="welcome to code jam";
	char ch;
	fscanf(in,"%c",&ch);
	for(i=0;i<n;i++)
	{
		count=0;
		fscanf(in,"%[^\n]",str);
		char ch;
		fscanf(in,"%c",&ch);
		find(p,str,0,0);
		count%=10000;
		fprintf(ou,"Case #%d: %04d\n",i+1,count);
	}
}
