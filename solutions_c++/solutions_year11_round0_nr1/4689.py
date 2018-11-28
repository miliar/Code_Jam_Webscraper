//============================================================================
// Name        : 0.cpp
// Author      : wlq
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <ctype.h>
#include <string.h>
using namespace std;

int main(void) {
     int a;
	cin>>a;
	//cout<<a<<endl;
	string s;
	for(int i=0;i<a;i++)
	{
		cin>>s;
		int ss=atoi(s.c_str());
	//	cout<<"SS:"<<ss<<endl;
		int nu0=0,nub=0;
		int waitnu0=0,waitnub=0;
		int z=0;
		int stepo=1,stepb=1;
		int flag=0;
		for(int j=0;j<ss;j++)
		{
			cin>>s;
			if(s=="O")
			{  	
		       nu0=0;
				cin>>s;
				int os=atoi(s.c_str());

				while(stepo!=os)
				{
					if(stepo>os)stepo--;
					else stepo++;
					nu0++;
					
				}
				//cout<<"o move"<<nu0<<endl;
				if(stepo==os){
					nu0++;
					//cout<<"o push"<<nu0<<endl;
					
				}
				if(flag==0)
		    {			
					z+=nu0;
					waitnu0+=nu0;	
					
			}
			else if(flag==1)
			{
					z+=nu0;
					waitnu0+=nu0;
					
			}
			 else
			{	
			if(flag==2&&waitnub>=nu0) 
			{	
			z+=1;
			waitnu0=1;
			//cout<<"flag>="<<flag<<" waitnu0="<<waitnu0<<" z="<<z<<endl;
			}
			else 
			{
			z+=nu0-waitnub;
			waitnu0=nu0-waitnub;
			//cout<<"flag<="<<flag<<" waitnu0="<<waitnu0<<" z="<<z<<endl;
			}
													
		}
			//	cout<<"flag="<<flag<<" waitnu0="<<waitnu0<<" z="<<z<<endl;							
				flag=1;
							
			
		    }
			if(s=="B")
			{
				nub=0;
				cin>>s;
				int bs=atoi(s.c_str());
			//	cout<<"bs"<<bs<<endl;

				while(stepb!=bs)
				{
					if(stepb>bs)
					     stepb--;
					else  
						stepb++;
					nub++;
					
					
				}//cout<<"b move"<<nub<<endl;
				if(stepb==bs){
					nub++;
			//	cout<<"b push"<<nub<<endl;
				
				}
				if(flag==0)
				{			
					z+=nub;
					waitnub+=nub;				
				}
				else if(flag==2)
				{
					z+=nub;
					waitnub+=nub;
				
				}
			    else
				{	
				if(flag==1&&waitnu0>=nub) 
				{	
					z+=1;
					waitnub=1;
				//	cout<<"flag>="<<flag<<" waitnu0="<<waitnu0<<" z="<<z<<endl;
				}
				else if(flag==1&&waitnu0<nub)
				{
					z+=nub-waitnu0;
					waitnub=nub-waitnu0;
				//	cout<<"flag<="<<flag<<" waitnu0="<<waitnu0<<" z="<<z<<endl;
				}
						
				}
				//cout<<"flag="<<flag<<" waitnub="<<waitnub<<" z="<<z<<endl;
								
				flag=2;
			
		    }
		
		}
		
	
		 cout<<"Case #"<<i+1<<": "<<z<<endl;
	}
}
