#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#define MAXN 2050

using namespace std;

const int maxy=1000000000;

int n;
int see[MAXN];
int ht[MAXN];

bool dfs(int i1,int i2,int mc,int md) {
   if(i1==i2) return 1;
   for(int i=i1;i<i2;i++)
      if(see[i]<=i||see[i]>i2) return 0;
   vector<int> arr;
   for(int i=i1;i<i2;i=see[i])
      arr.push_back(i);
   arr.push_back(i2);
   int mmc=mc,mmd=md;
   for(int j=arr.size()-2;j>=0;j--) {
      int il=arr[j];
      int ir=arr[j+1];
      ht[il]=ht[ir]-((ir-il)*mmc+mmd-1)/mmd;
      if(!dfs(il+1,ir,ht[ir]-ht[il]+1,ir-il)) return 0;
      mmc=ht[ir]-ht[il];
      mmd=ir-il;
   }
   return 1;
}

inline void solve() {
   ht[n-1]=maxy;
   if(!dfs(0,n-1,0,1)) {
      puts(" Impossible");
      return;
   }
   for(int i=0;i<n;i++)
      printf(" %d",ht[i]);
   puts("");
}

int main(void)
{
   int t,cas=1;
   scanf("%d",&t);
   while(t--) {
      scanf("%d",&n);
      for(int i=0;i<n-1;i++) {
         scanf("%d",see+i);
         see[i]--;
      }
      printf("Case #%d:",cas++);
      solve();
   }
   return 0;
}
