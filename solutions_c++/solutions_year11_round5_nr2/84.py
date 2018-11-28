#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FORE(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)

const int N=2000;
int _,n,a[N];

int doit() {
   if (n==0) return 0;

   map<int,int> m;
   REP(i,n) m[a[i]]++;
   vector<int> dl;
   int last = -1;
   int ans = n+1;
   FORE(i,m) {
      sort(dl.begin(),dl.end());
      while (i->second < dl.size() || dl.size() && last+1 != i->first) {
	 ans = min(ans, dl.back());
	 dl.pop_back();
      }
      dl.resize(i->second);
      FORE(j,dl) (*j)++;
      last = i->first;
   }
   sort(dl.begin(),dl.end());
   if (dl.size()) ans = min(ans, dl[0]);
   return ans;
}

int main() {
   scanf("%d",&_);
   REP(test,_) {
      scanf("%d",&n);
      REP(i,n) scanf("%d",&a[i]);
      printf("Case #%d: %d\n",test+1,doit());
   }
}
