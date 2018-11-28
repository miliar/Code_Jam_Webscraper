#include<stdio.h>
#include<iostream.h>

int main()
{
FILE *in,*out;

int  num,m,digi=0,n,numbercount[10]={0},i,tempncount[10]={0},arg,flag,k,n1,m1,count,c=1;


in=fopen("in.txt","r");
out=fopen("out.txt","w");
fscanf(in,"%d",&count);

while(count--)
{

for(i=0;i<10;i++)
	numbercount[i]=0;

fscanf(in,"%d",&num);
n=num;


while(n>0)
{
	m=n%10;
	n=n/10;
	digi++;
	if(m!=0)
			numbercount[m]++;

}

arg=num+1;
while(1)
{
	flag=0;
	for(k=0;k<10;k++)
		tempncount[k]=0;
	n1=arg;
	while(n1>0)
	{
	m1=n1%10;
	n1=n1/10;
	tempncount[m1]++;

	}
	
	
for(i=1;i<10;i++)
	if(numbercount[i]!=tempncount[i])
	{
			flag=1;
	break;
	
	}
if(flag==0)
{
	fprintf(out,"Case #%d: %d\n",c++,arg);
	break;


}
else

arg+=1;



}
}
fclose(in);
fclose(out);
}

