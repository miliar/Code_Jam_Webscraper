#include <stdio.h>
#include <algorithm>

using namespace std;

int m[3000],t,l;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    int cnt = 0, N, S, P, cur;
    while (t--)
    {
          cnt++;
          scanf("%d%d%d",&N,&S,&P);
          for (l=0; l<N; l++)
              scanf("%d",&m[l]);
          sort(m,m+N);
          reverse(m,m+N);
          int ans = 0;
          for (l=0; l<N; l++)
          {
              cur = m[l] - P;
              if (cur<0) continue;
              if (P - cur/2 < 2) ans++; else
              if (P - cur/2==2 && S) { ans++; S--; }
          }
          
          printf("Case #%d: %d\n",cnt,ans);
          
    }
}
