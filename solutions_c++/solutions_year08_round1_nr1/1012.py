#include<iostream.h>
#include<string.h>
#include<conio.h>
#include<math.h>
#include<fstream.h>
#include<stdio.h>
void main()
{
FILE *infile =freopen("c:\\tc\\bin\\input.txt","r",stdin);
FILE *outfile=freopen("c:\\tc\\bin\\output1.txt","w",stdout);
int T=0;
scanf("%d",&T);
for(int k=1; k<=T ;k++)
{
int a,i,j;
a=0;
scanf("%d",&a);
long a_in[1000],b_in[1000];
for(i=0;i<a;i++)
scanf("%ld",&a_in[i]);
for(i=0;i<a;i++)
scanf("%ld",&b_in[i]);
long  temp;
for(i=0;i<a-1;i++)
	for(j=0;j<a-i-1;j++)
{
	if(a_in[j]>a_in[j+1])
	{
	temp =a_in[j];
	a_in[j]=a_in[j+1];
	a_in[j+1]=temp;
	}if(b_in[j]<b_in[j+1])
	{
	temp =b_in[j];
	b_in[j]=b_in[j+1];
	b_in[j+1]=temp;
	}
}
double sum;
sum=0;
for(i=0;i<a;i++)
sum+= a_in[i] * b_in[i];


printf("Case #%d: %.0lf\n",k,sum);
}
fclose(infile);
fclose(outfile);
}
