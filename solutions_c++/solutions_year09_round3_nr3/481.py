using namespace std;

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <queue>

#define MP make_pair
#define PB push_back

inline int min(int a, int b) { return a<b?a:b; }
inline int max(int a, int b) { return a>b?a:b; }
inline int modul(int a) { return a>0?a:-a; }
inline long long sqr(long long a) { return a*a; }

int cmp(const int &a, const int &b) { return a<b; }

int T, t, i, Q, P, A[10], j, c, W[128], best;

int main()
{
 freopen("c.in", "r", stdin);
 freopen("c.out", "w", stdout);

 scanf("%d",&T);
 for (t=1; t<=T; ++t)
      {
       scanf("%d %d",&P,&Q);
       for (i=0; i<Q; ++i)
           scanf("%d",&A[i]);           
       best = P*Q;     
       do
         {
          memset(W, 0, sizeof(W));
          W[0] = W[P+1] = 1;
          c=0;
          for (i=0; i<Q; ++i)
              {
               j=A[i]-1;
               while (W[j]==0) --j;
               c += A[i]-j-1;
               j=A[i]+1;
               while (W[j]==0) ++j;
               c += j-A[i]-1;
               W[A[i]]=1;
              }
          best = min(c,best);
         }
      while (next_permutation(A, A+Q));
      printf("Case #%d: %d\n",t,best);
     }

 return 0;
}
