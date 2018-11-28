#include <cstdio>
#include <queue>

using namespace std;

int main()
{
  freopen("theme.in","r",stdin);
  freopen("theme.out","w",stdout);
  int testCase,caseno,i,j;
  long long c,r,k,n,count,temp,sum;
  queue <long long> q;
  scanf(" %d",&testCase);
  for(caseno=1;caseno<=testCase;caseno++)
  {
    
    while(!q.empty())
    {
      q.pop();
    }
    scanf(" %lld %lld %lld",&r,&k,&n);

    for(j=0;j<n;j++)
    {
      scanf(" %lld",&temp);
      q.push(temp);
    }
    printf("Case #%d: ",caseno);
    sum = 0;
    for(i=0;i<r;i++)
    {
      count = 0;
      c = n;
      while(1)
      {
	count = count + q.front();
	if(count <=k)
	{
	  if(c==0)
	    break;
	  else
	  {
	    temp = q.front();
	    q.pop();
	    q.push(temp);
	    sum = sum + temp;
	    c--;
	  }
	  
	}
	else
	{
	  break;
	}
      }
    }
    printf("%lld\n",sum);
    
  }
  return 0;
}
