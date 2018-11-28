// QRB.cpp
#include "stdafx.h"
#include "stdlib.h"
#include <conio.h>

#include "string.h"

char wc[]="welcome to code jam\0" ;
int wclen,dictlen;
void find(char * str,int from,int index,int * count)
{
	if(index>=wclen)
	{
		(*count)++;
		return;
	}
	if(from>=dictlen)
		return;
	for(int i=from;i<dictlen;i++)
	{
		if(str[i]==wc[index])
		{
			find(str,i+1,index+1,count);
		}
	}
}
int _tmain(int argc, _TCHAR* argv[])
{
	printf("Input filename:");
	char fn[256]="";
	memset(fn,0,255);
	int i=0;
	do
	{
		fn[i++]=getch();
		putch(fn[i-1]);
		if(i>255)
		{
			printf("\ninput error!\n");
			return 0;
		}
	}while(fn[i-1]!='\r'&&fn[i-1]!='\n');
	fn[i-1]='\0';
	wclen=(int)strlen(wc);
	FILE * fp=fopen(fn,"r");
	FILE * fpout=fopen("out.txt","w");
	if(!fp)
	{
		printf("file error!");
		return 0;
	}
	int cases=0,count;
	fscanf(fp,"%d",&cases);
	char * buf;
	i=0;
	while(i<cases)
	{
		buf=new char[512];
		memset(buf,0,511);
		fgets(buf,511,fp);
		if(buf[0]=='\r'||buf[0]=='\n'||buf[0]=='\0')
		{
			delete [] buf;
			continue;
		}
		dictlen=(int)strlen(buf);
		if(buf[dictlen-1]=='\n')
			buf[dictlen-1]='\0';
		count=0;
		find(buf,0,0,&count);
		printf("Case #%d: %04d\n",i+1,count);
		fprintf(fpout,"Case #%d: %04d\n",i+1,count);
		delete [] buf;
		i++;
	}
	fclose(fpout);
	fclose(fp);
	getch();
	return 0;
}

