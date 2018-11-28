#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>

using namespace std;

#define MAX 60
#define INFTY 0x3F3F3F3F

char boa[MAX][MAX];

int R,C,F,ans;

int cur;

void go(int x,int y,int mask);

inline void fall(int x,int y,int mask) {
  int h=0;
  while(boa[x][y])
    ++h, ++x;
  --h, --x;
  if(h<=F) {
    go(x,y,h==0 ? mask : 3);
  }
}

void go(int x,int y,int mask) {
  if(x==R) {
    ans=cur;
    return;
  }
  if((mask&1) && boa[x][y-1]) fall(x,y-1,1);
  if((mask&2) && boa[x][y+1]) fall(x,y+1,2);
  if(boa[x][y-1] && !boa[x+1][y-1]) {
    boa[x+1][y-1]=1;
    ++cur;
    if(cur<ans)
      go(x,y,3);
    boa[x+1][y-1]=0;
    --cur;
  }
  if(boa[x][y+1] && !boa[x+1][y+1]) {
    boa[x+1][y+1]=1;
    ++cur;
    if(cur<ans)
      go(x,y,3);
    boa[x+1][y+1]=0;
    --cur;
  }
}

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int tests;
  scanf("%d",&tests);
  for(int test=1;test<=tests;++test) {
    int i,j;
    scanf("%d%d%d",&R,&C,&F);
    memset(boa,0,sizeof(boa));
    for(i=1;i<=R;++i)
      scanf("%s",&boa[i][1]);
    for(i=1;i<=R;++i)
      for(j=1;j<=C;++j)
        if(boa[i][j]=='#')
          boa[i][j]=0;
    ans=INFTY;
    go(1,1,3);
    printf("Case #%d: ",test);
    if(ans<INFTY)
      printf("Yes %d\n",ans);
    else
      printf("No\n");
  }
  return 0;
}
