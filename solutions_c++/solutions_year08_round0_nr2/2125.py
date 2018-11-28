#include<stdio.h>
#include<math.h>
#include<conio.h>
#include<alloc.h>
#include<string.h>
#include<stdlib.h>


int N,turna,counta,countb,a,b;
//N to keep track of no of input samples
//turna turnaround time
//a and b to keep track of no of departures frm A and B
//counta  and countb to recoed the no of trains required.
int t1,t2,m1,m2;

struct timetable//data structure used to record time table
{
	char hra,mina,hrd,mind;
	char flag;
	struct timetable *nxt;
};

struct timetable *na,*nb,*present;

//na to record time table at A
//nb to record time table at B

void initialize()// to initialze our processing
{
	turna=a=b=counta=countb=0;
	na=NULL;
	nb=NULL;
}

void create(int flag)// to add an entery in the timetable
{
	long x1,x2;
	struct timetable *present1,*previous;
	present=(struct timetable *) malloc(sizeof(timetable));
	if (present== NULL)
	{
		printf("Not enough memory to allocate buffer\n");
		exit(4);  /* terminate program if out of memory */
	}

	present->nxt=NULL;
	present->hra=(char)t2;
	present->hrd=(char)t1;
	present->mina=(char)m2;
	present->mind=(char)m1;
	present->flag=0;

	x2=t1*60+m1;
	if(flag)
	{
		present1=previous=nb;
		countb++;
	}

	else
	{
		present1=previous=na;
		counta++;
	}

	//to place the time table in the order of Departures at a Station
	if(present1==NULL)
	{
		present1=present;
		if(flag)	nb=present;
		else 		na=present;
	}

	else
	{
		x1=present1->hrd*60+present1->mind;
		if(x1>x2)
		{
			if(flag)	nb=present;
			else 		na=present;
			present->nxt=present1;
			return;
		}

		present1=present1->nxt;

		while(present1)
		{
			x1=present1->hrd*60+present1->mind;
			if(x1>x2)
				break;
			previous=present1;
			present1=present1->nxt;
		}
		present->nxt=previous->nxt;
		previous->nxt=present;
	}
}

void destroy()// free space aftr processing
{
	struct timetable *previous;
	present=na;
	printf("\n");
	while(present)
	{
		previous=present;
		printf("%d:%d %d:%d",present->hrd,present->mind,present->hra,present->mina);
		free(previous);
		present=present->nxt;
	}
	present=nb;
	printf("\n");
	while(present)
	{
		previous=present;
		printf("%d:%d %d:%d",present->hrd,present->mind,present->hra,present->mina);
		free(previous);
		present=present->nxt;
	}
}

int process(struct timetable *present1,struct timetable *present2,int count)
{

	long x1,x2;
	//the evaluation of the no of trains at a station
	while(present1)
	{
		   x1=present1->hra*60+present1->mina+turna;
		   present=present2;
		   while(present)
		   {
			x2=present->hrd*60+present->mind;
			if(x2>=x1 && present->flag==0)
			{
				count--;
				present->flag=1;
				printf("\nInside");
				present=NULL;
			}
			present=present->nxt;
		   }
		   present1=present1->nxt;
	}
	return count;
}

main(int argc,char *argv[])
{
	int i,i1,i2,k;
	char ch,str[7];
	struct room *p,*q,*r;

	FILE *fInput,*fOutput;

	clrscr();
	//Correct Usage of the Code
	if(argc!=3)
	{
		printf("\n\n!!!Improper Usage \v\t Correct Usage::train INPUTFILE OUTPUTFILE");
		exit(1);
	}
	fInput=fopen(argv[1],"r");
	if(fInput==NULL)
	{
		printf("\n\n\t!! CANT OPEN INPUT FILE");
		exit(2);
	}
	fOutput=fopen(argv[2],"w");
	if(fInput==NULL)
	{
		printf("\n\n\t!! CANT OPEN OUTPUT FILE");
		exit(3);
	}
	//++++++++++++++++++++++++++++++++
	//No of samples in input file
	do
	{
		ch=fgetc(fInput);
		if(ch=='\n') break;
		N=N*10+ch-48;
	}while(1);

	for(i=1;i<=N;i++)
	{
		initialize();
		//turnaround time
		do
		{
			ch=fgetc(fInput);
			if(ch=='\n') break;
			turna=turna*10+ch-48;
		}while(1);
		//no of departures frm A
		do
		{
			ch=fgetc(fInput);
			if(ch==' ') break;
			a=a*10+ch-48;
		}while(1);

		//no of departures frm B
		do
		{
			ch=fgetc(fInput);
			if(ch=='\n') break;
			b=b*10+ch-48;
		}while(1);

		//departures frm A
		for(i1=1;i1<=a;i1++)
		{
			t1=t2=m1=m2=0;
			do
			{
				ch=fgetc(fInput);
				if(ch==':') break;
				t1=t1*10+ch-48;
			}while(1);

			do
			{
				ch=fgetc(fInput);
				if(ch==' ') break;
				m1=m1*10+ch-48;
			}while(1);

			do
			{
				ch=fgetc(fInput);
				if(ch==':') break;
				t2=t2*10+ch-48;
			}while(1);
			do
			{
				ch=fgetc(fInput);
				if(ch=='\n'||ch==EOF) break;
				m2=m2*10+ch-48;
			}while(1);
			create(0);
		}

		//no of departures frm B
		for(i2=1;i2<=b;i2++)
		{
			t1=t2=m1=m2=0;
			do
			{
				ch=fgetc(fInput);
				if(ch==':') break;
				t1=t1*10+ch-48;
			}while(1);
			do
			{
				ch=fgetc(fInput);
				if(ch==' ') break;
				m1=m1*10+ch-48;
			}while(1);

			do
			{
				ch=fgetc(fInput);
				if(ch==':') break;
				t2=t2*10+ch-48;
			}while(1);
			do
			{
				ch=fgetc(fInput);
				if(ch=='\n'||ch==EOF) break;
				m2=m2*10+ch-48;
			}while(1);
			create(1);
		}

		printf("\n1");
		countb=process(na,nb,countb);   //evaluation for Station B
		printf("\n2");
		counta=process(nb,na,counta);   //evaluation for Station A
		printf("\n%d %d",counta,countb);

		//Record The OUTPUT
		if(counta<0) counta=0;
		if(countb<0) countb=0;
		if(i!=1)
			fputc('\n',fOutput);
		fputs("Case #",fOutput);
		itoa(i,str,10);
		fputs(str,fOutput);
		fputs(": ",fOutput);
		itoa(counta,str,10);
		fputs(str,fOutput);
		fputc(' ',fOutput);
		itoa(countb,str,10);
		fputs(str,fOutput);
		destroy(); //free memory allocated dynamically
	}
	fclose(fInput);
	fclose(fOutput);
	return 0;
}