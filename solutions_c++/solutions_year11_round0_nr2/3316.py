// B.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include<iostream>
#include<stack>
#include<fstream>
using namespace std;
int main()
{   ifstream acin("B-small.in",ios::in);
    ofstream acout("B-small.out",ios::out);

    char ch[100];
	char cc[3];
	char dd[2];
	int ng;
	int c;
	int count;
	int d;
	int pre;
	int i,j,k;
	int casenum=1;
    acin>>ng;
	
	while(ng)
	{    
		acin>>c;
		
		if(c)
		{   
			acin>>cc[0];
			acin>>cc[1];
			acin>>cc[2];
			
		}
		acin>>d;

		if(d) 
		{
			acin>>dd[0];
			acin>>dd[1];
			
		}
    acin>>count;

	for(i=0;i<count;i++)
	{
		acin>>ch[i];
		
	}
        pre=0;


	for(i=1;i<count;i++)
	{    
		if(pre<0){pre=i;continue;}
		
		else if((c&&ch[i]==cc[0]&&ch[pre]==cc[1])||(c&&ch[i]==cc[1]&&ch[pre]==cc[0]))
		{
			ch[pre]='1';
			ch[i]=cc[2];
			pre=i;

		}
		else if( (d&&ch[i]==dd[0])||(d&&ch[i]==dd[1]))
		{   pre=i;
			if(ch[i]==dd[0]) 
		  for(k=i-1;k>=0;k--)
		  {
			  if(ch[k]==dd[1])
			  {
				  {
					  for(j=0;j<=i;j++) 
					  {ch[j]='1'; }
					  pre=-1;
					  break;
				  }                  
			  }
		  
		   }
		else 
		
			 for(k=i-1;k>=0;k--)
		  {
			  if(ch[k]==dd[0])
			  {
				  {
					  for(j=0;j<=i;j++) 
					  {ch[j]='1';}
					  pre=-1;
					  break;
				  }                  }
		  }
		
		}
		else {pre=i;}
	}
	acout<<"Case #"<<casenum<<": [";

	for(i=0;i<count;i++)
	{
		if(ch[i]!='1') {acout<<ch[i]; break;}

	}

  for(i++;i<count;i++)
  {
	  if(ch[i]!='1'){ acout<<", "<<ch[i];} 
  }

	acout<<"]"<<endl;
	casenum++;
	ng--;
	}
	return 0;
}
