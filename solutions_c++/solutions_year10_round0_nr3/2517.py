#include<cstdio>
#include<queue>
using namespace std;
queue<int> mq;

int g[1001],R,N,k;
int temp[1001];

int main()
{
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    int T;
    scanf("%d",&T);
    int t=1;
    while(T--)
    {
      scanf("%d%d%d",&R,&k,&N);
      
      while(!mq.empty())
       mq.pop();
      
      
      for(int i=0;i<N;i++)
      {
       scanf("%d",&g[i]);
        mq.push(g[i]);
      }
      int tmp,top,ans=0,tempid;
      for(int r=0;r<R;r++)
      {
        tmp=0,tempid=0;
        while(tmp<=k&&!mq.empty())
        {
          top = mq.front();
          
          if(tmp+top<=k)
          {
            tmp+=top;
            mq.pop();
            temp[tempid++]=top;
            //mq.push(top);
          }
          else
          break;
        }
        ans+=tmp;
        for(int i=0;i<tempid;i++)
         mq.push(temp[i]);
      }
      printf("Case #%d: %d\n",t++,ans);
    }
    return 0;
}
