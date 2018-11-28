#include <iostream>
using namespace std;
#define MAX 10000
int t;
int R[MAX],K[MAX],N[MAX];
int g[MAX][MAX];
int total[MAX];
int q[MAX];
int f=0,r=-1;
void cqu();
void cqu()
	{
		f=0;
		r=-1;
		for(int i=0;i<MAX;i++)
			q[i]=0;
	}
int wsum(int);int wsum(int a)
    {
          int s=0;
	      for(int b=0;b<N[a];b++)
                  s+=g[a][b];
          return s;
    }
void insert(int item)
     {
	 r=(r+1)%MAX;
	 q[r]=item;
     }
int del()
    {
	 int n=q[f];
	 f=(f+1)%MAX;
	 return n;
    }
int main()
    {
	  int sum=0;
	  int i,j,k;
	  cin>>t;
	  for(i=0;i<t;i++)
		  {
			      cin>>R[i];
			      cin>>K[i];
			      cin>>N[i];
			      for(int k=0;k<N[i];k++)
				      cin>>g[i][k];
		  }
	  for(i=0;i<t;i++)
			   {
				      for(k=0;k<N[i];k++)
							 insert(g[i][k]);
				      for(int j=0;j<R[i];j++)
				      {
				      if(wsum(i)<K[i])
						     {
					     total[i]+=wsum(i);
                                             continue;
                                     }
                      sum=0;
				      while((sum+q[f])<=K[i])
                        {
						 int a=del();
						 sum=sum+a;
						 insert(a);
					    }
                      total[i]+=sum;                                                           
                      }
			cqu();
               }
          for(i=0;i<t;i++)
			  cout<<"\nCase #"<<i+1<<": "<<total[i];
          return 0;
    }
