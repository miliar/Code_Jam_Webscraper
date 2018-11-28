#include<stdio.h>
#include<stdlib.h>
void main()
{
	FILE *fp,*fp1;
	int n,m,sum,i,temp;
	if((fp=fopen("1.txt","r"))==NULL)
	{
		printf("can not open this file.\n");
		exit(0);
	}
	if((fp1=fopen("2.txt","w"))==NULL)
	{
		printf("can not open this file.\n");
		exit(0);
	}
	fscanf(fp,"%d",&sum);
	for(i=0;i<sum;i++)
	{
		fscanf(fp,"%d %d",&n,&m);
		temp=1;
		while(n)
		{
			temp=temp*2;
			n--;
		}
		if((m+1)%temp==0)
			fprintf(fp1,"Case #%d: ON\n",i+1);
		else
			fprintf(fp1,"Case #%d: OFF\n",i+1);
	}
	fclose(fp);
	fclose(fp1);
}