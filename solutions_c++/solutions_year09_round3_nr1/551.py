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

int T, t, x, i;
char S[128], C[300];
long long b, f;

int main()
{
 freopen("a.in", "r", stdin);
 freopen("a.out", "w", stdout);

 scanf("%d",&T);
 for (t=1; t<=T; ++t)
     {
      scanf("%s\n",&S);
      memset(C,-1,sizeof(C));
      C[S[0]]=1;
      i=x=1;
      while (S[i]==S[0]) ++i;
      C[S[i]]=0;
      for (i=0; i<strlen(S); ++i)
           if (C[S[i]]==-1) C[S[i]] = (++x);
      ++x;      
      b=1;
      for (f=0,i=strlen(S)-1; i>=0; --i)
          {
           f = f + C[S[i]] * b;
           b *= x;
          }
      printf("Case #%d: %I64d\n",t,f);
     }

 return 0;
}
