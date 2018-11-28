#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{

	char inp[] ="welcome to code jam";
	char ch;
	int ctr,i,k,num;
	int str[20];
	cin>>num;
	ch=getchar();
	for (k=0;k<num;k++)
	{	
	str[0]=1;
	ctr=0;
	for(i=1;i<20;i++)
		str[i]=0;
	
	do
	{
	ch=getchar();
	if(ch == 10 )
		break;	
	for(i=0;i<19;i++)
		if(ch == inp[i])
			str[i+1] = (str[i+1]+str[i])%10000; 
	if(ch == 10 )
		break;	
	ctr++;
	}while(ch != 10);
	
	printf("Case #%d: %04d",k+1,str[19]);
	if(k < (num-1)) printf("\n");	
	}
}
