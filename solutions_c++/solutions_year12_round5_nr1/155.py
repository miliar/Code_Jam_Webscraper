#include <cstdio>
#include <algorithm>
#define MAXN 1050

using namespace std;

class Level {
   public:
      int l,p,id;
      const bool operator<(const Level &b) const {
         int c1=p*b.l;
         int c2=l*b.p;
         if(c1!=c2) return c1>c2;
         return id<b.id;
      }
};

int n;
Level lvl[MAXN];

int main(void)
{
   int t,cas=1;
   scanf("%d",&t);
   while(t--) {
      scanf("%d",&n);
      for(int i=0;i<n;i++) {
         lvl[i].id=i;
         scanf("%d",&(lvl[i].l));
      }
      for(int i=0;i<n;i++)
         scanf("%d",&(lvl[i].p));
      sort(lvl,lvl+n);
      printf("Case #%d:",cas++);
      for(int i=0;i<n;i++)
         printf(" %d",lvl[i].id);
      puts("");
   }
   return 0;
}
