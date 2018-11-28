// Welcome to Code Jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include <string.h>
#include "stdlib.h"
using namespace std;
void Welcome(char *current)
{    char *reg="welcome to code jam";
	int length=strlen(current);
	long *num=(long *)malloc(sizeof(long)*length);
	long *tmp=(long *)malloc(sizeof(long)*length);
	int Wel_lenth=strlen(reg);
	for(int i=0;i<length;++i)
	{   if(current[i]=='w')
		  num[i]=1;
	    else
		  num[i]=0;
	}
	for(i=1;i<Wel_lenth;++i)
	{
		//copy
		for(int j=0;j<length;++j)
			tmp[j]=num[j];
		  //num-to-0
	    //memset(num,0,length);
		for(int m=0;m<length;++m)
		{  
			  num[m]=0;
		}

		for(j=0;j<length;++j)
		{
			if(reg[i]==current[j])
			{
               for(int k=0;k<j;++k)
				   num[j]+=tmp[k]%10000;
			}
		}



	}
    long Res=0;
	for(i=0;i<length;++i)
		Res+=num[i]%10000;
	if(Res>=10000)
		Res%=10000;

    if(Res<10)
		cout<<"000";
	else if(Res<100)
		cout<<"00";
	else if(Res<1000)
		cout<<"0";

	cout<<Res<<"\n";

	 
}

void main(int argc, char* argv[])
{ 
   freopen("C-large.in","r",stdin);
   freopen("C-large.out","w",stdout);    
	 int N;
     cin>>N;
	 char current[10000];
	 gets(current);
	for(int i=1;i<=N;++i)
	{  cout<<"Case #"<<i<<": " ;
	    gets(current);
		Welcome(current);
	}

}
