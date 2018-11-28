// Alien.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include"string.h"
#include<string>
using namespace std;
void Alien()
{

	int L,D,N;
	freopen("A-large.in","r",stdin);
	freopen("Output_large.out","w",stdout);
	scanf("%d",&L);
	scanf("%d",&D);
	scanf("%d",&N);

	string d[5000];
	for(int i=0;i<D;++i)
	{
		cin>>d[i];
	}

	int lenth=(d[0]).size();
    string current;
	for(i=0;i<N;++i)
	{
		cin>>current;
       int total=0;
		
	for(int j=0;j<D;++j)
	{   const char *tmp0=current.c_str();
	char tmp1[1000];
	char *tmp;

	strcpy(tmp1,tmp0);
	tmp=tmp1;
	   int Reg_L=0,Reg_R=0;
	   int flag=1;
		for(int k=0;k<lenth;++k)
		{    
			if(*tmp=='(')
			{
                Reg_L=(int)strchr(tmp,'(')-(int)strchr(tmp,tmp[0])+1;
                Reg_R=(int)strchr(tmp,')')-(int)strchr(tmp,tmp[0])-1;
				
			}
			else
			{
				Reg_L=Reg_R=0;
				
			}


           int localflag=0;

			while(Reg_L<=Reg_R)
			{
				if(tmp[Reg_L]==d[j][k])
				{
                  localflag=1;
				}
				else
				{
                      
				}
				++Reg_L;

			}
			if(localflag==0)
			{
				flag=0;
				break;
			}


			if(*tmp=='(')
			{
              tmp+=Reg_R+2;
			}
			else
			{
              ++tmp;
			}

			
				

		}

		if(flag==1)
		{
         ++total;
		}
	}
		








        printf("Case #%d: %d\n",i+1,total);




	}


}





int main(int argc, char* argv[])
{
	
Alien();
	return 0;
}
