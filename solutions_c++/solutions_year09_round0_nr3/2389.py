#include <stdio.h>
#include <stdlib.h>

int ctr=0;

void cjm(char *p,char *str,int stk_pos,int cur_pos)
{
	if(str[cur_pos]=='\0')
	{
		if(p[stk_pos]=='\0')
			ctr++;
		return;
	}
	if(p[stk_pos]=='\0')
	{
		ctr++;
		return;
	}
	if(str[cur_pos]==p[stk_pos])
	{
		cjm(p,str,stk_pos+1,cur_pos+1);
		cjm(p,str,stk_pos,cur_pos+1);
	}
	else
	{
		cjm(p,str,stk_pos,cur_pos+1);
	}
}

main()
{
	int i,j,k;
	char str[500];

	int n;
	FILE *fp=fopen("input","r");

	FILE *fp2=fopen("output.txt","w");

	fscanf(fp,"%d",&n);

	char *p="welcome to code jam";
	char ch;
	fscanf(fp,"%c",&ch);
	for(i=0;i<n;i++)
	{
		ctr=0;
		fscanf(fp,"%[^\n]",str);
		char ch;
		fscanf(fp,"%c",&ch);
		cjm(p,str,0,0);
		ctr%=10000;
		fprintf(fp2,"Case #%d: %04d\n",i+1,ctr);
	}
}
