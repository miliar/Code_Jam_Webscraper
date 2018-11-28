#include<string>
#include<algorithm>
#include<cstdlib>
#include<vector>
using namespace std;
const int maxn=30;
int comb[maxn][maxn];
int oppo[maxn][maxn];
char info[1000],z[1000];
int l;
int dy(char t)
{
  return t-'A'+1;
}
void init()
{
  char com[10];
  int n,i;
  memset(oppo,0,sizeof(oppo));
  memset(comb,0,sizeof(comb));
  scanf("%d",&n);
  for (i=1;i<=n;i++)
  {
    scanf("%s",com);
    comb[dy(com[0])][dy(com[1])]=dy(com[2]);
    comb[dy(com[1])][dy(com[0])]=dy(com[2]);
  }
  scanf("%d",&n);
  for (i=1;i<=n;i++)
  {
    scanf("%s",com);
    oppo[dy(com[0])][dy(com[1])]=1;
    oppo[dy(com[1])][dy(com[0])]=1;
  }
}
void work()
{
  int n,i,j;
  scanf("%d",&n);
  scanf("%s",info);
  l=1;z[0]=info[0];
  for (i=1;i<n;i++)
  {
    z[l]=info[i];
    l++;
    while (l>=2&&comb[dy(z[l-1])][dy(z[l-2])])
    {
      z[l-2]=comb[dy(z[l-1])][dy(z[l-2])]+'A'-1;
      l--;
    }
    for (j=0;j<l-1;j++)
      if (oppo[dy(z[j])][dy(z[l-1])])
      {
        l=0;
        break;
      }
  }
}
void print()
{
  int i;
  for (i=0;i<l;i++)
  {
    if (i) printf(", ");
    printf("%c",z[i]);
  }
  printf("]\n");
}    
int main()
{
  freopen("blarge.in","r",stdin);
  freopen("blarge.out","w",stdout);
  int cas,ii;
  scanf("%d",&cas);
  for (ii=1;ii<=cas;ii++)
  {
    init();
    work();
    printf("Case #%d: [",ii);
    print();
  }
  return 0;
}
