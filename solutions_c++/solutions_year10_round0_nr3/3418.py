
#include <iostream> 
using namespace std;
#define scanf scanf_s
int start_loop,len_loop,sum_loop,visit[1100];
int T,R,N,K,g[2010];

__int64 S[1010];

int begin(int i,int &sum)
{
	int j;
	sum=0;
   for(j=i;j<i+N;j++)
	   if(sum+g[j]<=K)
		   sum+=g[j];
	   else
		   break;
   

   if(j>N)
	   return j-N;
   else
	   return j;
}


void find_loop()
{
   memset(visit,0,sizeof(visit));
   int index=0,i=1,j,sum;
  sum_loop=0;
  S[0]=0;
   while(!visit[i])
   {
	  
     visit[i]=++index;
	//  cout<<visit[i]<<"  "<<i<<"  ";
	   i=begin(i,sum);
	//   cout<<i<<" **  \n";
	 S[index]=S[index-1]+sum;
	// printf("%I64d %d",S[index],sum);
   }
   len_loop=index-visit[i]+1;
   start_loop=visit[i];
  // printf("len = %d  start=== %d\n",len_loop,start_loop);
}


int main()
{  
	freopen("d:\\C-large.in","r",stdin);
	freopen("d:\\b.txt","w",stdout);

  scanf("%d",&T);
  for(int cas=1;cas<=T;cas++)
  {
	  printf("Case #%d: ",cas);
     scanf("%d%d%d",&R,&K,&N);
	 for(int i=1;i<=N;i++)
	 {
		 scanf("%d",&g[i]);
	    g[i+N]=g[i];
	 }
   find_loop();

   if(R<=start_loop)
	   printf("%I64d\n",S[R]);
   else
   {
	   __int64 loopsum=S[start_loop+len_loop-1] - S[start_loop-1];

	   int loopcount=( R-(start_loop-1) )/len_loop;
	   int left=( R-(start_loop-1) )%len_loop;
      printf("%I64d\n",S[start_loop +left -1] + loopsum * loopcount);
   }

  }
     
  return 0; 
}
