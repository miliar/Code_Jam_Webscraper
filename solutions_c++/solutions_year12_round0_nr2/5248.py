#include<iostream>
#include<stdio.h>

using namespace::std;

int main()
{
	char in[50];
	int T,N,s,sp,p;
	int i,j,k,t,avg;
	int score, tscore[100];
        int count=0,s1;
	cin>>T;
	
		
	for(i=0; i<T; i ++)
	{	
		cin>>N;		
		cin>>s; 
		cin>>p;	
		
		count=0;
		for(k=0;k<N;k++)
		{
		cin>>tscore[k];
		}
		for(k=0;k<N;k++)
		{	
			t =tscore[k];
			t = t-p;
			if (t>=0){
			avg=(int)t/2;
			if(avg>=p)count++;
			else if( p-avg == 1) count++;
			else if( p-avg == 2 && s>0) 
			{ 	
			count++; 
			--s;}
			}
		}
		N=s=p=0;
		
cout<<"Case #"<<i+1<<": "<<count<<endl;
}
}	
