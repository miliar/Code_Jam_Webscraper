#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

struct time
{
	int hour;
	int min;
}a[100],b[100],c;

struct pq
{
	struct time t[100];
	int top;
}p1,p2;


int count1=0, count2=0, t;

int cmp(struct time, struct time);

int cmp1(struct time, struct time);

void main()
{
	int i,j,na,nb,n,k;
	char a1,a2;
	clrscr();
	FILE *fp1, *fp2;

	fp1=fopen("timetab.txt","r");
	if(fp1==NULL)
	{
		printf("Cannot open source file\n");
		exit(1);
	}

	fp2=fopen("timetaba.txt","w");
	if(fp2==NULL)
	{
		printf("Cannot open target file\n");
		exit(2);
	}

	fscanf(fp1,"%d",&n);
	for(k=1;k<=n;k++)
	{
		count1=0;
		count2=0;
		fscanf(fp1,"%d",&t);
		fscanf(fp1,"%d %d",&na,&nb);
		fgetc(fp1);
		for(i=0;i<na;i++)
		{
			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.hour=(a1-'0')*10+(a2-'0');
			fgetc(fp1);
			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.min=(a1-'0')*10+(a2-'0');
			fgetc(fp1);

			for(j=i-1;j>=0&&!cmp(c,a[j]);j--)
			{
				a[j+1]=a[j];
			}
			a[j+1]=c;

			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.hour=(a1-'0')*10+(a2-'0');
			fgetc(fp1);
			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.min=(a1-'0')*10+(a2-'0');
			fgetc(fp1);

			for(j=i-1;j>=0&&cmp(c,p1.t[j]);j--)
			{
				p1.t[j+1]=p1.t[j];
			}
			p1.t[j+1]=c;
		}
		p1.top=na-1;


		for(i=0;i<nb;i++)
		{
			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.hour=(a1-'0')*10+(a2-'0');
			fgetc(fp1);
			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.min=(a1-'0')*10+(a2-'0');
			fgetc(fp1);

			for(j=i-1;j>=0&&!cmp(c,b[j]);j--)
			{
				b[j+1]=b[j];
			}
			b[j+1]=c;

			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.hour=(a1-'0')*10+(a2-'0');
			fgetc(fp1);
			a1=fgetc(fp1);
			a2=fgetc(fp1);
			c.min=(a1-'0')*10+(a2-'0');
			fgetc(fp1);

			for(j=i-1;j>=0&&cmp(c,p2.t[j]);j--)
			{
				p2.t[j+1]=p2.t[j];
			}
			p2.t[j+1]=c;
		}

		p2.top=nb-1;
		i=0;
		while(i<na)
		{
			if(p2.top>=0)
			{
				c=p2.t[p2.top];
				if(cmp1(c,a[i]))
					count1++;
				else
					p2.top--;
			}
			else
				count1++;
			i++;
		}

		i=0;
		while(i<nb)
		{
			if(p1.top>=0)
			{
				c=p1.t[p1.top];
				if(cmp1(c,b[i]))
					count2++;
				else
					p1.top--;
			}
			else
				count2++;
			i++;
		}
		fprintf(fp2,"Case #%d: %d %d\n",k,count1,count2);
	}
	fclose(fp1);
	fclose(fp2);
	getch();
}

int cmp(struct time c, struct time a)
{
	if(c.hour>a.hour)
		return(1);
	else if(c.hour==a.hour)
	{
		if(c.min>a.min)
			return(1);
		else
			return(0);
	}
	return(0);
}

int cmp1(struct time c, struct time a)
{
	if(c.hour>a.hour)
		return(1);
	else if(c.hour==a.hour)
	{
		if(c.min+t>a.min)
			return(1);
		else
			return(0);
	}
	return(0);
}



