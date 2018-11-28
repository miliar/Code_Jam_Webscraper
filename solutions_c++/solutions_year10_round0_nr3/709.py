#include <stdio.h>
#include <math.h>
long long g[20000];

long long int cycle[20000];
long long int cycid[20000];
bool occ[20000];
long long cyccost[20000];
long long nextcost[20000];
long long R,k,N;
int main()
{
  long long int T;
  scanf("%lld",&T);
  for(long long int t=1;t<=T;t++)
    {
      scanf("%lld %lld %lld",&R,&k,&N);
      for(long long int i=0;i<N;i++)
	scanf("%lld",&g[i]);

      
      for(long long int i=0;i<N;i++)
	occ[i]=0;
      
      long long int pos=0;
      long long int cl=0;
      long long currcost=0;
      long long int cycst,cyclen;
      long long cyclegain=0;
      
      while(1)
	{
	  
	  cycle[cl]=pos;
	  cycid[pos]=cl;
	  occ[pos]=1;
	  cyccost[cl]=currcost;
	  // printf("%d\n",cl);
	  long long int pop=0;
	  long long int currpos=pos;
	  for(long long int i=pos;i<pos+N;i++)
	    {
	      if(pop+g[i%N]>k)
		{
		  break;
		}
	      else
		{
		  currpos=(i+1)%N;
		  pop+=g[i%N];
		}
	    }
	  currcost+=pop;
	  nextcost[cl]=pop;
	  cl++;


	  pos=currpos;
	  if(occ[pos])
	    {
	      cycst=pos;
	      cyclen=cl-cycid[pos];
	      cyclegain=currcost-cyccost[cycid[pos]];
	      break;
	    }
	  
	}
      //printf("%d %lld\n",cycst,cyclegain);
      //for(int c=0;c<cl;c++)
      //	{
      //	  printf("%d %lld %lld\n",cycle[c],cyccost[c],nextcost[c]);
      //	}

      long long int baki=R;
      long long amount=0;
      for(long long int c=0;;c++)
	{
	  long long next=nextcost[c];


	  if(baki==0)
	    {
	      break;
	    }
	  if(cycle[c]==cycst)
	    {
	      //printf("Amount is %lld\n",amount);
	      if(cyclen>0)
		{
		  long long more=baki%cyclen;
		  amount+=(baki/cyclen)*cyclegain+cyccost[c+more]-cyccost[c];
		}
	      break;
	    }
	  else
	    {
	      amount+=next;
	      baki--;
	    }
	    
	}

      printf("Case #%lld: %lld\n",t,amount);




    }
}
