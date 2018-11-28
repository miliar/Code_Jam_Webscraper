#include <cstdio>
#include <vector>
using namespace std;

int T,N,cnt;
struct event
{
    int P,i;
};
vector<event> V[2];
char s[2],x;
int main ()
{
    freopen("input.in","r",stdin);freopen("output.out","w",stdout);
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
    cnt=0;V[0].clear();V[1].clear();
    scanf("%d",&N);
    for (int i=1;i<=N;++i)
    {
        scanf("%s %d",s,&x);
        if (s[0]=='O') V[0].push_back((event){x,i});
        else V[1].push_back((event){x,i});
    }
    int i=0,j=0,pos[]={1,1};
    int m=V[0].size(),n=V[1].size();
    while (i<m && j<n)
    {
          ++cnt;
          if (V[0][i].i<V[1][j].i)
          {
              if (pos[1]<V[1][j].P) ++pos[1];
              else if (pos[1]>V[1][j].P) --pos[1];
              if (pos[0]<V[0][i].P) ++pos[0];
              else if (pos[0]>V[0][i].P) --pos[0];
              else ++i;
          }
          else
          {
              if (pos[0]<V[0][i].P) ++pos[0];
              else if (pos[0]>V[0][i].P) --pos[0];
              if (pos[1]<V[1][j].P) ++pos[1];
              else if (pos[1]>V[1][j].P) --pos[1];
              else ++j;
          }
    }
    while (i<m)
    {
          ++cnt;
          if (pos[0]<V[0][i].P) ++pos[0];
          else if (pos[0]>V[0][i].P) --pos[0];
          else ++i;
    }
    while (j<n)
    {
          ++cnt;
          if (pos[1]<V[1][j].P) ++pos[1];
          else if (pos[1]>V[1][j].P) --pos[1];
          else ++j;
    }
    printf("Case #%d: %d\n",z,cnt);
    }
    return 0;
}
