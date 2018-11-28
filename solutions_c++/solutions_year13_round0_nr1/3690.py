#include<stdio.h>
#include<conio.h>
void main()
{
int T,set;
FILE *fp,*ot;
fp=fopen("input.txt","r");
ot=fopen("output.txt","w");

fscanf(fp,"%d",&T);
for(set=1;set<=T;set++)
{
char s[4][4],*p;
int x='X',o='O',t='T',i=0,j=0,c[4],r[4],d[4]={0,0,0,0},ch,ij,k=0;
int dot='.',flago=0,flagx=0,flagdot=0,scopy;
clrscr();                      /*
while(feof(fp)==0)
{
fscanf(fp,"%s",*(p+i*3+j));
j++;if(j%4==0)i++;
}                              */
for(j=0;j<4;++j)
fscanf(fp,"%s",s[j]);

for(i=0;i<4;++i)
{
	r[i]=0;
	for(j=0;j<4;++j)
		r[i]+=s[i][j];
}
ch=x*3+t;
//printf("%d %d %d %d",r[0],x,t,x*3+t);
for(j=0;j<4;++j)
{
	c[j]=0;
		for(i=0;i<4;++i)
		c[j]+=s[i][j];
}
//printf("%d %d",c[0],x);

for(i=0;i<4;++i)
{
	for(j=0;j<4;++j)
	{
	ij=i+j;
		if(i==j)
		d[0]+=s[i][j];
			if(ij==3)
			d[1]+=s[i][j] ;
	}
}
//printf("%d %d",d[0],x);

for(i=0;i<4;++i)
{
	if(r[i]==4*x || r[i]==ch)
	{
	flagx=1;
	break;
	}

	if((c[i]==4*x || c[i]==(3*x+t)) && flagx!=1)
	{
	flagx=1;
	break;
	}


	if((d[0]==4*x || d[0]==(3*x+t) || d[1]==4*x || d[1]==(3*x+t)) && flagx!=1)
	{
	flagx=1;
	break;
	}
}
if(flagx!=1)
{	 ch=o*3+t;
	for(i=0;i<4;++i)
	{
		if(r[i]==4*o || r[i]==ch)
		{
		flago=1;
		break;
		}

		if((c[i]==4*o || c[i]==(3*o+t)) && flago!=1 )
		{
		flago=1;
		break;
		}


		if((d[0]==4*o || d[0]==(3*o+t) || d[1]==4*o || d[1]==(3*o+t)) && flago!=1)
		{
		flago=1;
		break;
		}
	}
}
	for(i=0;i<4;++i)
	{
		for(j=0;j<4;++j)
		{
		scopy=s[i][j];
		  if(scopy==dot)
		  {
		  flagdot=1;
		  break;
		  }
		 }
		  if(flagdot==1)
		  break;
	}
if(flagx==1) fprintf(ot,"Case #%d: X won\n",set) ;
if(flago==1) fprintf(ot,"Case #%d: O won\n",set)  ;
if(flago!=1 && flagx!=1)
{
if(flagdot==1) fprintf(ot,"Case #%d: Game has not completed\n",set);
if(flagdot!=1) fprintf(ot,"Case #%d: Draw\n",set);
}
}
getch();
fclose(fp);
fclose(ot);
	}

