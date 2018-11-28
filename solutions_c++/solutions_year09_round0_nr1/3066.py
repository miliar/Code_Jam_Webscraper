#include<stdio.h>
#include<iostream>
#include<math.h>
#include<string.h>
#include<stdlib.h>
#include<unistd.h>
using namespace std;

int main(int argc, char * argv[])
{
	int L,D,N,k,flag,m;
	char alien[5000][15];
	char * text;
	long long count;
	text = (char *)malloc(sizeof(char *));
	cin>>L>>D>>N;
	for(int i=0;i<D;i++)	
		cin>>alien[i];
	for(int i=0;i<N;i++)
	{
		cin>>text;
		count=0;
		for(int j=0;j<D;j++)
		 {
		 int k=0;
		 for(m=0;m<L;m++)
		 {
		    if(text[k]!='\0')
		    {
			flag=0;
			if(text[k]=='(')
			{
				while(text[++k]!=')')
				  if(text[k]==alien[j][m]) flag=1;
				if(flag==0)
				 break;
			}
			else 	 
				if(alien[j][m]!=text[k]) 
					break;
			k++;		
		     }			
		   }
		   if (m==L)
		   count++;		  
		  }
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
return 0;
}	
