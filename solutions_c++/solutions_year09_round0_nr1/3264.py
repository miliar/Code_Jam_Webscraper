// google1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <string>
#include <iostream>
using namespace std; 


int test(char *a,char *b)
{
	int i=0;
	int j=1;
	char *aa, *bb;
	int ss=1;

	if(a[0]=='\0' && *b=='\0')
		return 1;
	if(*a=='\0' || *b=='\0')
		return 0;

	if(*b=='(')
	{
		while(b[i]!=')')
		{
			i=i+1;
		}
		bb=b+i+1;
		aa=a+1;
		for(j=1;j<i;j++)
		{
			if(*a==b[j])
			{
				return (test(aa,bb));
			}
		}
	}
	if (*a==*b)
	{
		aa=a+1;
		bb=b+1;
		return (test(aa,bb));
	}

	return 0;
}



int main(int argc, char* argv[])
{

	int D,L,N,i,j,ii,jj;
	FILE *fp;
	FILE *fpp;
	char s[5000][15];
	char n[28*15];
	int sum;

	fpp = fopen( "fout.txt", "w" );
	fp=fopen("A-small-attempt1.in","r");	
///////////////////////////
	if(!fp)
	{
		printf("不能打开文件\n");
		return 0;
	}
/////////////////////////
    fscanf(fp,"%d",&L);
    fscanf(fp,"%d",&D);
	fscanf(fp,"%d",&N);

	for(i=0;i<D;i++)
		fscanf(fp,"%s",s[i]);

	for(i=0;i<N;i++)
	{
		sum=0;
		fscanf(fp,"%s",n);



		for(j=0;j<D;j++)
		{
			sum=sum+test(s[j],n);
		}
		fprintf(fpp,"Case #%d: %d\n",(i+1),sum);

	}

//////////////////////////


/*
	{
		char aa[15]={"dac"};
		char cc[15]="(ab)(bc)(ca)";
		printf("%s\n",aa);
		printf("%s\n",cc);
		printf("\ntest=%d\n",test(aa,cc));
	}
*/



/*
while(s[i][j])
{
	printf("%c",s[i][j]);
	j=j+1;
}

	for(i=0;i<D;i++)
		printf("%s\n",s[i]);

	for(i=0;i<N;i++)
		printf("%s\n",n[i]);
*/

fclose(fp);
fclose(fpp);


	printf("Hello World!\n");
	return 0;
}



