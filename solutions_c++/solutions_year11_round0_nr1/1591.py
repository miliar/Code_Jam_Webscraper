#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
using namespace std;
int lo,lb;
char com[1000];
int info[1000][2];
int n,ntime;
void init()
{
  int i;
  char t;
  scanf("%d",&n);
  for (i=1;i<=n;i++)
  {
    while (scanf("%c",&t),t==' ');
    if (t=='O') info[i][1]=0;
    else info[i][1]=1;
    scanf("%d",&info[i][0]);
  }
}
void work()
{
  int i;
  int ltimeo=0,ltimeb=0,lposo=1,lposb=1;
  ntime=0;
  for (i=1;i<=n;i++)
  {
    if (info[i][1]==0)
    {
      ntime=max(ntime,ltimeb+abs(lposb-info[i][0]))+1;
      lposb=info[i][0];
      ltimeb=ntime;
    }
    else
    {
      ntime=max(ntime,ltimeo+abs(lposo-info[i][0]))+1;
      lposo=info[i][0];
      ltimeo=ntime;
    }
  }
}
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("a-large.out","w",stdout);
  int cas,ii,i;
  scanf("%d\n",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    work();
    printf("Case #%d: %d\n",ii,ntime);
  }
  return 0;
}
