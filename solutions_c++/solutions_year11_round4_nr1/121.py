#include <stdio.h>
#include <math.h>
#include <algorithm>
using namespace std;
int S[1000100];
int X,W,R,t,N;
int main()
{
  int Tcases;
  scanf("%d",&Tcases);
  for(int tcases=1;tcases<=Tcases;tcases++)
    {
      scanf("%d%d%d%d%d",&X,&W,&R,&t,&N);
      for(int i=0;i<X;i++)
	S[i]=0;
      for(int i=1;i<=N;i++)
	{
	  int st,en,sp;
	  scanf("%d%d%d",&st,&en,&sp);
	  for(int j=st;j<en;j++)
	    {
	      
	      S[j]+=sp;
	    }
	}
      sort(S,S+X);
      double secleft=t;
      double answer=0;
      for(int i=0;i<X;i++)
	{
	 
	  //run at S[i]+R
	  double runtime=min(secleft,1.0/(S[i]+R));
	  double walktime=(1.0-runtime*(S[i]+R))/(S[i]+W);
	  answer+=runtime+walktime;
	  secleft-=runtime;
	  //printf("%d %lf %lf\n",S[i],runtime,walktime);
	}
      //printf("\n");
	
      printf("Case #%d: %1.10f\n",tcases,answer);
      
    }
}
