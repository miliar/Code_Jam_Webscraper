#include <stdio.h>
#include <algorithm>
#include <queue>
#define MAXN 1050

using namespace std;

class Pair {
   public:
      int x,l;
      Pair() {}
      Pair(int xi,int li):x(xi),l(li) {}
      const bool operator<(const Pair &b) const {
         if(x!=b.x) return x<b.x;
         return l>b.l;
      }
};

int n;
int s[MAXN];

inline int min(int a,int b) { return a<b?a:b; }

inline int solve() {
   int i,j,opt=n;
   Pair pr;
   priority_queue<Pair> pq;
   vector<Pair> tmp;
   std::sort(s,s+n);
   for(i=0;i<n;i=j) {
      tmp.clear();
      for(j=i;j<n&&s[j]==s[i];j++) {
         if(pq.empty()) {
            tmp.push_back(Pair(s[i],1));
            //pq.push(Pair(s[i],1));
         } else {
            pr=pq.top();
            pq.pop();
            if(pr.x==s[i]-1) {
               tmp.push_back(Pair(s[i],pr.l+1));
               //pq.push(Pair(s[i],pr.l+1));
            } else {
               opt=min(opt,pr.l);
               tmp.push_back(Pair(s[i],1));
               //pq.push(Pair(s[i],1));
            }
         }
      }
      for(vector<Pair>::iterator it=tmp.begin();it!=tmp.end();it++)
         pq.push(*it);
   }
   while(!pq.empty()) {
      pr=pq.top();
      pq.pop();
      opt=min(opt,pr.l);
   }
   return opt;
}

int main(void)
{
   int t,i,casenum=1;
   scanf("%d",&t);
   while(t--) {
      scanf("%d",&n);
      for(i=0;i<n;i++)
         scanf("%d",s+i);
      printf("Case #%d: %d\n",casenum++,solve());
   }
   return 0;
}
