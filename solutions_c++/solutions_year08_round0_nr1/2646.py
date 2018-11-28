//Author: Rajitha Rani
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char**estr,**qstr;
int*q;
int noe,noq;
char buff[1000];
int getIndex(char*str,char**arr,int size)
{
	for(int i=0;i<size;i++)
		if(strcmp(str,arr[i])==0)
			return i;
	return -1;
}
void makeIntoInt()
{
	q=(int*)malloc(sizeof(int)*noq);
	for(int i=0;i<noq;i++)
	{
		q[i]= getIndex(qstr[i],estr,noe);
		//printf("%d\n",q[i]);
	}
}
void freeAll()
{
	for(int i=0;i<noe;i++)
		free(estr[i]);
	for(int i=0;i<noq;i++)
		free(qstr[i]);
	free(estr);	
	free(qstr);
	free(q);
}
void make2DArray(int caseno)
{
	int *p=(int*)malloc(sizeof(int)*noe*noq);
	for(long i=0;i<noe;i++)
		p[i+(noq-1)*noe]=noq;
	p[q[noq-1] + (noq-1)*noe ] = 0;

	for(long i=noq-2;i>=0;i--)
	{
		for(long j=0;j<noe;j++)
		{
			p[j+i*noe]=p[j+(i+1)*noe]+1;
		}
		p[q[i] + i*noe ] = 0;
	}
	
	int count=0;
	int cr=0,max;
	max=p[0];
	for(long i=0;i<noe;i++)
		if(p[i]>max)
			max=p[i];
	cr=max;
	while(cr<noq)
	{
		max=p[cr*noe];
		for(long i=0;i<noe;i++)
			if(p[i+cr*noe]>max)
				max=p[i+cr*noe];
		cr+= max;
		//printf("%d\n",cr);
		count++;
	}
	printf("case#%d: %d\n",caseno,count);
	free(p);
}
void readCase(FILE*fp,int caseno)
{
	fscanf(fp,"%d\n",&noe);
	estr=(char**)malloc(sizeof(char*)*noe);
	char buff[1000];
	for(int i=0;i<noe;i++)
	{
		fgets(buff,1000,fp);
		estr[i]= strdup(buff);
		//printf("%d) %s\n",i,buff);
	}
	fscanf(fp,"%d\n",&noq);
	if(noq){
	//printf("noq=%d\n",noq);
	qstr=(char**)malloc(sizeof(char*)*noq);
	for(int i=0;i<noq;i++)
	{
		fgets(buff,1000,fp);
		qstr[i]= strdup(buff);
		//printf("%d) %s\n",i,buff);
	}
	makeIntoInt();
	make2DArray(caseno);
	freeAll();
	}
	else
		printf("case #%d: 0\n",caseno);
}

void main()
{
	int noc;
	FILE*fp=fopen("input.txt","rt");
	fscanf(fp,"%d\n",&noc);
	for(int i=0;i<noc;i++)
		readCase(fp,i+1);
	fclose(fp);
}
