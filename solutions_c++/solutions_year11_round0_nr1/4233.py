#include<stdio.h>
#include<conio.h>

void main()
{
FILE *f,*f1;
int n,it,s[100],tun[100],i=0,j=0,dif=0,time=0,to=0,tb=0,op=1,bp=1,a;
char turn[100];
f = fopen("input.txt","r");

f1 = fopen("output.txt","w");

fscanf(f,"%d",&n);
for(i=0;i<n;i++)
{
fscanf(f,"%d ",&it);
for(j=0;j<it;j++)
{
turn[j] = fgetc(f);
fscanf(f," %d ",&s[j]);
fflush(f);
}

op=1;bp=1;time=0;to=0;tb=0;
for(j=0;j<it;j++)
{

	if(turn[j]=='O')
	{
	if(s[j]!=op)
		{
		if(s[j]>op)
		dif = s[j]-op;
		else
		dif = op-s[j];

		if((dif)>(time-to))
		{
		a = time - to;
		}
		else
		a = dif;

		if(s[j]>op)
		op = op + a;
		else
		op = op - a;

		}

		if(s[j]>op)
		dif = s[j]-op;
		else
		dif = op-s[j];

		op = s[j];
	time = time + dif +1;
	to = time;
	}
	else
	{
	if(s[j]!=bp)
		{
		if(s[j]>bp)
		dif = s[j]-bp;
		else
		dif = bp-s[j];

		if((dif)>(time-tb))
		{
		a = time - tb;
		}
		else
		a = dif;

		if(s[j]>bp)
		bp = bp + a;
		else
		bp = bp - a;
		}

		if(s[j]>bp)
		dif = s[j]-bp;
		else
		dif = bp-s[j];


	time = time + dif +1;
	tb = time;
	bp = s[j];
	}

}

fprintf(f1,"Case #%d: %d\n",i+1,time);

}

}






