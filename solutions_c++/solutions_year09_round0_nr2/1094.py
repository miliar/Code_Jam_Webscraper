// Watersheds.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include"stdlib.h"
using namespace std;

struct Direct
{
	int toX;
	int toY;
	char flag;
};
int min(int N,int W,int E, int S);


void Watersheds(int H,int W)
{ int map[102][102];
 
for(int i=1;i<=H;++i)
   for(int j=1;j<=W;++j)
	   cin>>map[i][j];

   for(i=0;i<=W+1;++i)
   {
	   map[0][i]=map[H+1][i]=65535;
   }

   for(i=0;i<=H+1;++i)
   {
	   map[i][0]=map[i][W+1]=65535;
   }

   Direct d[102][102];
   for(i=0;i<=H+1;++i)
	   for(int j=0;j<=W+1;++j)
	   {
		   d[i][j].flag=NULL;
		   d[i][j].toX=-1;
		   d[i][j].toY=-1;
	   }

   for(i=1;i<=H;++i)
	   for(int j=1;j<=W;++j)
	   {
           int ToDirect=min(map[i-1][j],map[i][j-1],map[i][j+1],map[i+1][j]);
		   if(ToDirect==0)
		   {
			   if(map[i-1][j]<map[i][j])
			   {
				   d[i][j].toX=i-1;
                   d[i][j].toY=j;
			   }

		   }
		   else if(ToDirect==1)
		   {
			   if(map[i][j-1]<map[i][j])
			   {
				   d[i][j].toX=i;
                   d[i][j].toY=j-1;
			   }
		   }
		   else if(ToDirect==2)
		   {
			   if(map[i][j+1]<map[i][j])
			   {
				   d[i][j].toX=i;
                   d[i][j].toY=j+1;
			   }
		   }
		   else //if(ToDirect==3)
		   {
			   if(map[i+1][j]<map[i][j])
			   {
				   d[i][j].toX=i+1;
                   d[i][j].toY=j;
			   }

		   }
	   }
	   char flag='a';

        for(i=1;i<=H;++i)
			for(int j=1;j<=W;++j)
			{
              if(d[i][j].flag==NULL)
			  {
				 // d[i][j].flag=flag;

				  if(d[i][j].toX==-1)
				  {
					  d[i][j].flag=flag;
                       ++flag;
				  }
				  else
				  {

                  int m=i,n=j;

					  while(d[m][n].flag==NULL)
					  {
						   int tmpM,tmpN;
						   tmpM=d[m][n].toX;
						   tmpN=d[m][n].toY;
                           if(tmpM==-1)
							   break;
						   m=tmpM;
						   n=tmpN;
					  }

					  if(d[m][n].flag==NULL)//to  sink 
					  {   m=i;
					      n=j;
						  while(m!=-1)
						  { int tmpM,tmpN;
							  d[m][n].flag=flag;
						   tmpM=d[m][n].toX;
						   tmpN=d[m][n].toY;
						   m=tmpM;
						   n=tmpN;
						  }

						   ++flag;
					  }
					  else
					  {
						  char currentFlag=d[m][n].flag;
						  m=i;
					      n=j;
						  while(d[m][n].flag==NULL)
						  { int tmpM,tmpN;
                                 d[m][n].flag=currentFlag;
					             tmpM=d[m][n].toX;
						         tmpN=d[m][n].toY;
						         m=tmpM;
						         n=tmpN;
						  }						  
					  }
				  }				  
			  }
			}
		for(i=1;i<=H;++i)
		{  
			for(int j=1;j<=W;++j)
			{
				cout<<d[i][j].flag<<" ";
			}
			cout<<"\n";
		}
}


int min(int N,int W,int E, int S)
{    int tmp1,min1;
     int tmp2,min2;
	 int tmp;
	if(N<=W)
	{
		tmp1=0;
		min1=N;
	}
	else
	{
		tmp1=1;
		min1=W;
	}
	if(E<=S)
	{
		tmp2=2;
		min2=E;
	}
	else
	{
		tmp2=3;
		min2=S;
	}

	if(min1<=min2)
	{
		tmp=tmp1;

	}
	else
	{
		tmp=tmp2;

	}
	return tmp;
}

void main(int argc, char* argv[])
{ 	//freopen("input.in","r",stdin);
//    freopen("B-small-attempt2.in","r",stdin);
    freopen("B-large.in","r",stdin);
//	freopen("output.out","w",stdout);
	freopen("B-large.out","w",stdout);
	int T;
	cin>>T;
	for(int i=0;i<T;++i)
	{int H,W;
	 cin>>H>>W;
	 cout<<"Case #"<<i+1<<":\n";
	 Watersheds(H,W);
	}
}
