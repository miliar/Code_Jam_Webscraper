#include<stdio.h>
#include<fstream.h>
#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<math.h>

#define MAX 21

int na=0,nb=0,nota=0,notb=0,tat=0;
int flag1[MAX]={0},flag2[MAX]={0},flag3[MAX]={0},flag4[MAX]={0};

void timesort(int a[MAX],int b[MAX],int flg)
{
	int i,j,t,MX=0;
	
	if(flg==1)
			MX=na-1;
	else if(flg==2)
			MX=nb-1;

	for(i=0;i<MX;i++)
	{
		for(j=0;j<MX;j++)
		{
			if(a[j]>a[j+1])
			{
					t=a[j];
					a[j]=a[j+1];
					a[j+1]=t;

					t=b[j];
					b[j]=b[j+1];
					b[j+1]=t;
			}
		}
	}
}

void fmt(char str1[MAX][5],char str2[MAX][5],int flg)
{
	int MX=0;

	if(flg==1)
		MX=na;
	else if(flg==2)
		MX=nb;

	for(int i=0;i<MX;i++)
	{
		str2[i][0]=str1[i][0];
		str2[i][1]=str1[i][1];
		str2[i][2]=str1[i][3];
		str2[i][3]=str1[i][4];
		str2[i][4]='\0';
	}
}

void fmttoint(int times[MAX],char str2[MAX][5],int flg)
{
	int i,j,val,fact=1000,MX=0;

	if(flg==1)
		MX=na;
	else if(flg==2)
		MX=nb;

	for(i=0;i<MX;i++)
	{
		fact=1000;
		times[i]=0;
		for(j=0;j<4;j++)
		{
			val=str2[i][j]-48;
			times[i]+=val*fact;
			fact/=10;
		}
	}
}

void process(int checkdep1[MAX],int checkarr1[MAX],int checkdep2[MAX],int checkarr2[MAX])
{
	int x,y,tempval,eartempval,earyval;
	
	int incrflag=0;

	nota=0;
	notb=0;

	for(x=0;x<na;x++)
		flag1[x]=flag2[x]=0;
	for(y=0;y<nb;y++)
		flag3[y]=flag4[y]=0;


	for(x=0;x<na;x++)
	{
		eartempval=9999;
		incrflag=1;

		for(y=0;y<nb;y++)
		{
			tempval=checkarr2[y]+tat;

			if(((tempval%100)-60)>=0)
			{
				tempval=tempval-60;
				tempval=tempval+100;
			}

			if((tempval<=checkdep1[x])&&(tempval<eartempval))
			{
				if(flag4[y]==0)
				{
					flag4[y]=1;
					incrflag=0;

					if(eartempval!=9999)
						flag4[earyval]=0;
					
					eartempval=tempval;
					earyval=y;
				}
			}
		}

		if(incrflag==1)
		{
			nota++;
		}
	}

	for(x=0;x<nb;x++)
	{
		incrflag=1;
		eartempval=9999;

		for(y=0;y<na;y++)
		{
			tempval=checkarr1[y]+tat;

			if(((tempval%100)-60)>=0)
			{
				tempval=tempval-60;
				tempval=tempval+100;
			}

			if((tempval<=checkdep2[x])&&(tempval<eartempval))
			{
				if(flag2[y]==0)
				{
					flag2[y]=1;
					incrflag=0;
					
					if(eartempval!=9999)
						flag2[earyval]=0;

					eartempval=tempval;
					earyval=y;
				}
			}
		}

		if(incrflag==1)
		{
			notb++;
		}
	}
}

void main()
{
	FILE *fp;
	int i=0,j=0,n=0;
	char depAtmp[MAX][5],arrAtmp[MAX][5],depBtmp[MAX][5],arrBtmp[MAX][5];
	char depAc[MAX][5],arrAc[MAX][5],depBc[MAX][5],arrBc[MAX][5];
	int depA[MAX],arrA[MAX],depB[MAX],arrB[MAX];

	void timesort(int str1[MAX],int str2[MAX],int);
	void fmt(char str1[MAX][5],char str2[MAX][5],int);
	void fmttoint(int str1[MAX],char str2[MAX][5],int);
	void process(int checkdep1[MAX],int checkarr1[MAX],int checkdep2[MAX],int checkarr2[MAX]);
	clrscr();
	fp=fopen("B-small.txt","r");
	if(fp==NULL)
		printf("error");
	fstream fp2;

	fp2.open("outprob2.txt",ios::out);
	if(fp==NULL)
		printf("error2");

	fscanf(fp,"%d",&n);
	printf("Total is %d",n);
	
	for(i=0;i<n;i++)
	{
		nota=0;
		notb=0;

		fscanf(fp,"%d",&tat);

		fscanf(fp,"%d",&na);

		fscanf(fp,"%d",&nb);

		for(j=0;j<na;j++)
		{
			fscanf(fp,"%s",&depAtmp[j]);
			fgetc(fp);
			fscanf(fp,"%s",&arrAtmp[j]);
		}

		for(j=0;j<nb;j++)
		{
			fscanf(fp,"%s",&depBtmp[j]);
			fgetc(fp);
			fscanf(fp,"%s",&arrBtmp[j]);
		}

		fmt(depAtmp,depAc,1);

		fmt(arrAtmp,arrAc,1);

		fmt(depBtmp,depBc,2);

		fmt(arrBtmp,arrBc,2);

		fmttoint(depA,depAc,1);

		fmttoint(arrA,arrAc,1);

		fmttoint(depB,depBc,2);

		fmttoint(arrB,arrBc,2);

		timesort(depA,arrA,1);

		timesort(depB,arrB,2);

		process(depA,arrA,depB,arrB);

		fp2<<"Case #"<<i+1<<": "<<nota<<" "<<notb<<"\n";
	}
}