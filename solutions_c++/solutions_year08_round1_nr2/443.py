#include <iostream>
using namespace std;
#define N 2001
#define M 2001
int cut[M][N],ans[N],num[M],ok[N];
int main()
{
  int c,n,m,i,j,t,x,y,tmp0,sum=0,min=INT_MAX,yes,cs=0;
  scanf("%d",&c);
  while(c--)
    {
      min=INT_MAX;
      cs++;
      yes=0;
      memset(cut,-1,sizeof cut);
      scanf("%d%d",&n,&m);
      for(i=0;i<m;i++)
	{
	  scanf("%d",&t);
	  while(t--)
	    {
	      scanf("%d%d",&x,&y);
	      cut[i][x]=y;
	    }
	}
      memset(ans,0,sizeof ans);
      while(ans[0]==0)
	{
	  sum=0;
	  j=n;
	  while(ans[j]==1)
	    j--;
	  ans[j]=1;
	  for(i=j+1;i<=n;i++)
	    ans[i]=0;
	  memset(num,0,sizeof num);
	  for(i=1;i<=n;i++)
	    {
	      for(j=0;j<m;j++)
		{
		  if(cut[j][i]==ans[i])
		    num[j]++;
		}
	      sum+=ans[i];
	    }
	   tmp0=0;
	   for(j=0;j<m;j++)
	     {
	       if(num[j]==0)
		 {
		   tmp0=1;
		   break;
		 }
	     }
	   if(tmp0==0&&sum<min)
	     {
	       for(i=1;i<=n;i++)
		 ok[i]=ans[i];
	       min=sum;
	       yes=1;
	     }
	 }
       if(yes==1)
	 {
	   printf("Case #%d: ",cs);
	   for(i=1;i<=n;i++)
	     printf("%d ",ok[i]);
	   printf("\n");
	 }
       else
	 printf("Case #%d: IMPOSSIBLE\n",cs);
    }
  return 0;
}
