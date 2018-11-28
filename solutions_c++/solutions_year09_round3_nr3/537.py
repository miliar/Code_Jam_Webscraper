#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
using namespace std;

int v[50],pos[50][2];
bool br[200];
int rel[200];
int p;

int simulate(int n)
{
  int ret=0;
  memset(rel,0,sizeof(rel));
  for(int i=0;i<n;i++) {
    rel[v[i]]=1;
    int pos=v[i]-1;
    while(pos >= 0 && !rel[pos]) { pos--; ret++; }
    pos=v[i]+1;
    while(pos < p && !rel[pos]) { pos++; ret++; }
  }
  return ret;
}

int main()
{
  int tt;
  scanf("%d",&tt);
  for(int t=1;t<=tt;t++) {
    memset(br,0,sizeof(br));
    memset(rel,0,sizeof(rel));
    memset(pos,0,sizeof(pos));
    memset(v,0,sizeof(v));
    int q;
    scanf("%d %d", &p, &q);
    for(int i=0;i<q;i++) {
      scanf("%d", &v[i]);
      v[i]--;
    } 
    sort(v,v+q);
    int res=1<<30;
    do {
      memset(rel,0,sizeof(rel));
      memset(br,0,sizeof(br));
      memset(pos,0,sizeof(pos));
      int t = simulate(q);
      res=min(res,t);
    } while(next_permutation(v,v+q));
    printf("Case #%d: %d\n", t, res);
  }

  return 0;
}
