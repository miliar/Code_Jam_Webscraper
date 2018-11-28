#include<cstdio>

struct run
{
      long long int cost,next;
};

long long int n,k;
long long int a[1009];
run nextrun[1009][32];
void genrun0()
{
     int i,cur;
     long long int csum;
     csum=0;
     cur=-1;
     for(i=0;i<32;i++)
     {
       nextrun[n][i].cost=0;
       nextrun[n][i].next=n;
     }
     for(i=0;i<n;i++)
     {
        
        while(csum<=k)
        {
          cur++;
          cur %=n;
          csum+=a[cur];
          if(cur==i && csum-a[cur]!=0)
            break;
        }
        nextrun[i][0].cost=csum-a[cur];
	if(csum==a[cur])
	  nextrun[i][0].next=n;
	else
          nextrun[i][0].next=cur;
        csum-=a[i];
     }
}
void genrun(int runno)
{
  int i,nextno;
  for(i=0;i<n;i++)
  {
    nextno = nextrun[i][runno-1].next;
    nextrun[i][runno].cost = nextrun[i][runno-1].cost+nextrun[nextno][runno-1].cost;
    nextrun[i][runno].next = nextrun[nextno][runno-1].next;
  }
}
int main()
{
    long long int t,r;
    int i,j,it;
    scanf("%lld",&t);
//    printf("%lld test cases\n",t);
    for(i=1;i<=t;i++)
    {
       scanf("%lld%lld%lld",&r,&k,&n);
//       printf("%lld %lld %lld inputs\n");
       for(j=0;j<n;j++)
         scanf("%lld",&a[j]);
//       printf("Case #%d: ",i);
       genrun0();
       for(j=1;j<32;j++)
	 genrun(j);
       /*
       for(j=0;j<3;j++)
       {
	 printf("For %d runs\n",1<<j);
	 for(it=0;it<n;it++)
	   printf("%lld %lld\t",nextrun[it][j].cost,nextrun[it][j].next);
	 printf("\n");
       }
       */
       long long int runcnt,ans;
       ans=0;
       runcnt=0;
       int curpos;
       curpos=0;
       while(r>0)
       {
	 if(r&1)
	 {
	   ans+=nextrun[curpos][runcnt].cost;
	   //printf("%d runs adds %lld \tans now %lld\n",1<<runcnt,nextrun[curpos][runcnt].cost,ans);
	 curpos=nextrun[curpos][runcnt].next;
	 }
	 r>>=1;
	 runcnt++;
       }
       printf("Case #%d: %lld\n",i,ans);
    }
    return 0;
}
