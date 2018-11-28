#include <stdio.h>
#include<ctype.h>
#include <conio.h>
#include <iostream.h>
#include <fstream.h>
# define MAXSIZE 10

int cq[MAXSIZE];
int front,rear;

void disp()
{
int i;
for(i=0;i<4;i++)
{
	printf("%d\n",cq[i]);
}
}


int add(int item)
{
	if (front+1 >= MAXSIZE)
	{
		//cq[front]=item;
		return 0;
	}
	else
	{

	       front=front+1;
	       cq[front]=item;
	       return 1;
	}
}
int del()
{
int a;
	if(front < 0 )
	{
	return 0;
	}
	else
	{
		int i;
		a = cq[0];
		for(i=1;i<=front;i++)
			cq[i-1]=cq[i];
		//front--;
		cq[front]=a;
		return(a);

	}
}

double pro(double ik,double ir,double n)
{

int i,num;
double sum,k,r,count;
double result;
k=ik;
r=ir;
//n=10;
result=0;
int temp;
//clrscr();
//add(4);
//add(3);
//add(9);
//add(1);
//add(2);
//add(5);
//add(6);
//add(9);
//add(1);

for(i=0; i<r;i++)
{
	sum=0;
	count=0;
	while(sum+cq[0]<=k && count<n)
	{
		count++;
		sum+=cq[0];
		temp=del();
		//add(temp);
	}
	result+=sum;
}

//disp();
printf("\n\n%.0f",result);

return result;
}               //end of main

void main()
{
int i,j,a;
clrscr();
ifstream fin("c:/123.in",ios::in);
ofstream fout("c:/cout.txt",ios::in);
int t;
fin>> t;
for(i=0;i<t;i++)
{
int r,k,n;
fin>>r;
fin>>k;
fin>>n;
		front = -1;
	for(j=0;j<n;j++)
	{



		fin>>a;
		add(a);

	}
		fout<<"Case #"<<i+1<<": "<<pro(k,r,n)<<"\n";
}
getch();

}


