#include <cstdio>
#include <memory.h>

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int N,x=1;
    scanf("%d",&N);
    while (x <= N)
    {
          int n,k,b,t;
          scanf("%d %d %d %d",&n,&k,&b,&t);
          int pos[n+3],v[n+3];
          int sampai=0,diangkat=0;
          int status[n+3];
          memset(status,-1,sizeof status);
          for (int i = 0; i < n; i++)
              scanf("%d",&pos[i]);
          for (int i = 0; i < n; i++)
              scanf("%d",&v[i]);
          for (int i = 0; i < n; i++)
          {
              if ((double)(b-pos[i])/(double)v[i] > (double)t) continue;
              status[i] = 0;
              double mini = 2000000000.0;
              for (int j = i+1; j < n; j++)
              {
                  if (v[i] > v[j] && ((double)(b-pos[j])/(double)v[j] > (double)t))
                  {
                           double apa=(double)(pos[j]-pos[i])/(double)(v[i]-v[j]);
                           if (apa < t) status[i]++;
                  }
              }
              /*for (int j = i+1; j < n; j++)
              {
                  if (v[i] > v[j])
                  {
                           double apa=(double)(pos[j]-pos[i])/(double)(v[i]-v[j]);
                           if (apa < mini) status[i]++;
                  }
              }*/
          }
          //for (int i = 0; i < n; i++)
          //    printf("%d ",status[i]);
          //printf("\n");
          for (int i = n-1; i >= 0; i--)
              if (status[i] != -1)
              {
                 diangkat += status[i];
                 sampai++;
                 if (sampai == k) break;
              }
          printf("Case #%d: ",x);
          if (sampai == k)
             printf("%d\n",diangkat);
          else printf("IMPOSSIBLE\n");
          x++;
    }
    return 0;
}
