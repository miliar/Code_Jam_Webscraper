#include <cstdio>
#include <string>
using namespace std;

const int mod=10000;
const int maxn=1024;
const char t[]="welcome to code jam";


char s[maxn];
int f[maxn][32];
int n, m;

inline void add(int& x, int y) {
 x+=y;
 if (x>=mod) x-=mod;
}

int main() {
 freopen("c-small.in", "r", stdin);
 freopen("c-small.out", "w", stdout);

 m=strlen(t);
 int T; scanf("%d\n", &T);
 for (int tc=1; tc<=T; ++tc) {
  gets(s);
  int n=strlen(s);
  memset(f, 0, sizeof(f));
  f[0][0]=1;
  int res=0;
  for (int i=0; i<n; ++i)
   for (int j=0; j<m; ++j) if (f[i][j]) {
    add(f[i+1][j], f[i][j]);
    if (s[i]==t[j]) {
     add(f[i+1][(j+1)%m], f[i][j]);
     if (j+1==m) add(res, f[i][j]);
    }                              
   }
  printf("Case #%d: %04d\n", tc, res);
 


 }


 return 0;
}
