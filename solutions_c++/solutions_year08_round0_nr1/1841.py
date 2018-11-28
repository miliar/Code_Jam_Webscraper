#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

char engine[150][50];
int flag[150];
int m,sw=0;

int setflag(char []);
int checkflag(int);
void setzero();

void main()
{
	FILE *fp1, *fp2;
	int i,j,l,a;
	char temp[50];
	clrscr();

	fp1=fopen("search.txt","r");
	fp2=fopen("search_a.txt","w");

	if(fp1==NULL)
	{
		printf("Cannot find source file\n");
		exit(1);

	}

	if(fp2==NULL)
	{
		printf("Cannot open target file\n");
		exit(2);
	}

	int n;
	fscanf(fp1,"%d",&n);
	fgetc(fp1);

	for(i=0;i<n;i++)
	{
		sw=0;
		fscanf(fp1,"%d",&m);
		fgetc(fp1);
		for(j=0;j<m;j++)
		{
			fgets(temp,50,fp1);
			strcpy(engine[j],temp);
		}
		setzero();

		fscanf(fp1,"%d",&l);
		fgetc(fp1);
		for(j=1;j<=l;j++)
		{
			fgets(temp,50,fp1);
			a=setflag(temp);
			if(a==1)
				a=setflag(temp);
		}
		fprintf(fp2,"Case #%d: %d\n",i+1,sw);
	}

	getch();
}

int setflag(char a[])
{
	int i,p;

	for(i=0;i<m;i++)
	{
		if(!strcmp(a,engine[i]))
			break;
	}

	if(flag[i]==1)
		return(0);

	p=checkflag(i);
	if(p==1)
	{
		sw++;
		setzero();
		return(1);
	}
	flag[i]=1;
	return(0);
}

int checkflag(int a)
{
	int i;
	for(i=0;i<m;i++)
	{
		if(i==a)
			continue;
		if(flag[i]==0)
			return(0);
	}
	return(1);
}

void setzero()
{
	for(int i=0;i<m;i++)
	{
		flag[i]=0;
	}
}
