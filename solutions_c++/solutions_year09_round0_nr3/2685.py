// google3.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int test(char *tt, char *aa)
{
	char *ttt;
	char *aaa;
	int i,j,sum;
	if(aa[0]=='\0')
	{
		return 1;
	}
	if(aa[0]!='\0' && tt[0]=='\0')
	{
		return 0;
	}
	ttt=tt;
	aaa=aa;
	sum=0;
	i=0;
	j=0;


	while(tt[i]!='\0')
	{
		if(tt[i]==aa[0])
		{
			sum=sum+test((ttt=tt+i+1),(aaa=aa+1));
		}
		i++;
	}

	return sum;
		
}



void da(char *t,int b)
{
	char tt;
	int i;
	for(i=0;i<4;i++)
	{
		t[i]=(b%10)+'0';
		b=(b-b%10)/10;
	}

	for(i=0;i<2;i++)
	{
		tt=t[i];
		t[i]=t[3-i];
		t[3-i]=tt;
	}
}







int main(int argc, char* argv[])
{
	int N,i,j;
	FILE *fp;
	FILE *fpp;
	char s[510];
	char a[20]="welcome to code jam";
	int ans;
	char dad[4];


	fpp = fopen( "fout.txt", "w" );
	fp=fopen("C-small-attempt1.in","r");	
///////////////////////////
	if(!fpp)
	{
		printf("不能打开文件\n");
		return 0;
	}
	if(!fp)
	{
		printf("不能打开文件\n");
		return 0;
	}
/////////////////////////



	fgets(s,500,fp);
//	printf("%s\n",s);
//	N=s[0]-'0';

	i=0;
	N=0;
	while(s[i]!='\0')
	{
		i=i+1;
	}
	for(j=1;j<i;j++)
	{
		N=10*N+s[j-1]-'0';
	}
//	printf("%d\n",N);





	for(i=0;i<N;i++)
	{
		fgets(s,500,fp);

//		printf("%s",s);

		ans=test(s,a);
		ans=ans%10000;


		da(dad,ans);


		fprintf(fpp,"Case #%d: %c%c%c%c\n",(i+1),dad[0],dad[1],dad[2],dad[3]);

	}


fclose(fp);
fclose(fpp);

	return 0;
}

