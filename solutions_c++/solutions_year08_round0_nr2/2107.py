#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;


#define CC 100
typedef 
struct
{
	int st;
	int ed;
}
tt;
int main()
{
	int cases,times;
	int lagtime,na,nb;
	tt a[CC],b[CC],t;
	int i,j,k,tota,totb,flag;
	FILE *pin;
	FILE *pout;	
	pin  = fopen("e:\\in.txt", "r");
	pout = fopen("e:\\out.txt", "w");

	fscanf(pin,"%d",&cases);
	for (times=0;times<cases;times++)
	{
		//Init
		for (i=0;i<CC;i++)
		{
			a[i].st=0;
			a[i].ed=0;
			b[i].st=0;
			b[i].ed=0;
		}
		fscanf(pin,"%d",&lagtime);
		fscanf(pin,"%d%d",&na,&nb);
		for (i=0;i<na;i++)
		{
			int ta,tb,tc,td;
			fscanf(pin,"%d:%d %d:%d",&ta,&tb,&tc,&td);
			a[i].st=ta*60+tb;
			a[i].ed=tc*60+td;
		}
		for (i=0;i<nb;i++)
		{
			int ta,tb,tc,td;
			fscanf(pin,"%d:%d %d:%d",&ta,&tb,&tc,&td);
			b[i].st=ta*60+tb;
			b[i].ed=tc*60+td;
		}

		//Solve
		int pa,pb;
		tota=0; totb=0;
		for (i=0;i<na;i++)
			for (j=i+1;j<na;j++)
				if (a[i].ed>a[j].ed)
				{
					t=a[i]; 
					a[i]=a[j]; 
					a[j]=t;
				}
		for (i=0;i<nb;i++)
			for (j=i+1;j<nb;j++)
				if (b[i].st>b[j].st)
				{
					t=b[i]; 
					b[i]=b[j]; 
					b[j]=t;
				}

		pa=0; pb=0;
		do
		{
			if (pa>=na) break;
			flag=0;
			do
			{
				if (a[pa].ed + lagtime<= b[pb].st)
				{
					flag=1;
					totb++;
				}
				pb++;
			}
			while (pb<nb && flag==0);
			pa++;
		}
		while (pa<na);


		for (i=0;i<na;i++)
			for (j=i+1;j<na;j++)
				if (a[i].st>a[j].st)
				{
					t=a[i]; 
					a[i]=a[j]; 
					a[j]=t;
				}
		for (i=0;i<nb;i++)
			for (j=i+1;j<nb;j++)
				if (b[i].ed>b[j].ed)
				{
					t=b[i]; 
					b[i]=b[j]; 
					b[j]=t;
				}

		pa=0; pb=0;
		do
		{
			flag=0;
			if (pb>=nb) break;
			do
			{
				if (b[pb].ed + lagtime<= a[pa].st)
				{
					flag=1;
					tota++;
				}
				pa++;
			}
			while (pa<na && flag==0);
			pb++;
		}
		while (pb<nb);

		fprintf(pout,"Case #%d: %d %d\n",times+1,na-tota,nb-totb);
	}
	
	fclose(pin);
	fclose(pout);
	return 0;
}