#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{

	char ch,a[5000][15];
	
	int ctr,ctrl,i,j,k,l,d,num;
	long long int str[5000][16],total;
	cin>>l>>d>>num;
	ch=getchar();
	for (i=0;i<d;i++)
		{
		for(j=0;j<l;j++)
		a[i][j]=getchar();
		ch=getchar();
		}
	//ch=getchar();
	for (k=0;k<num;k++)
	{	
	ctr =0;
	ctrl=0;

	for(i=0;i<d;i++)
		{
		str[i][0]=1;
		for(j=1;j<=l;j++)
			str[i][j]=0;
		}
	do
	{
	ch=getchar();
	//putchar(ch);
	if(ch == 10 )
		break;
	if(ch == '(')
		ctrl=1;
	if(ch == ')')
		 ctrl=0;	
	for(i=0;i<d;i++)
			if(ch == a[i][ctr])
				str[i][ctr+1] += str[i][ctr]; 
	if(ctrl != 1 )	
		ctr++;
	}while(ch != 10);
	total=0;
	for(i=0;i<d;i++)
		total += str[i][l];
	cout<<"Case #"<<k+1<<": "<<total;
	if(k < (num-1)) printf("\n");	
	}
}
