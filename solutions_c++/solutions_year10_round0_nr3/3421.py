#include <stdio.h>
#include <string.h>
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,r,k,a[10000],visit[10000],cir,j,next[10000],num[10000],i;
    scanf("%d",&t);
    for (int I=1;I<=t;I++)
    {
          scanf("%d%d%d",&r,&k,&n);
          for (i=0;i<n;i++)
              scanf("%d",&a[i]);
          int start=0;
          int find=0;
          memset(visit,0,sizeof(visit));
          while (!find)
          {
                if (visit[start])
                {
                    find=1;
                    cir=start;
                    break;
                }
                else
                    visit[start]=1;
                int sum=0;
                int count=0;
                for (j=start;count<n;j=(j+1)%n)
                {
                    count++;
                    if (sum+a[j]>k) break;
                    else
                        sum+=a[j];
                }
                next[start]=j;
                num[start]=sum;
                start=j;
          }
          int length=0;
          int p=cir;
          while (next[p]!=cir)
          {
                length++;
                p=next[p];
          }
          length++;
          int first=0;
          p=0;
          while (next[p]!=cir)
          {
                first++;
                p=next[p];
          }
          first++;
          //r=first+length*p1+tt;
          int p1=(r-first>=0)?(r-first)/length:0;
          int tt=(r-first>=0)?(r-first-length*p1):0;
          long long cnt=0;
          int ready=0;
          if (r-first<0) first=r;
          for (i=0;i<first;i++)
          {
              cnt+=num[ready];
              ready=next[ready];
          }
          long long cnt1=0;
          ready=cir;
          for (i=0;i<length;i++)
          {
              cnt1+=num[ready];
              ready=next[ready];
          }
          cnt+=cnt1*p1;
          ready=cir;
          cnt1=0;
          for (i=0;i<tt;i++)
          {
              cnt1+=num[ready];
              ready=next[ready];
          }
          cnt+=cnt1;
          printf("Case #%d: %lld\n",I,cnt);
    }
    return 0;
}
