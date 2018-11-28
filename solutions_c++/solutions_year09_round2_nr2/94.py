#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std; 

typedef vector<int> vi;
typedef vector<string> vs;
typedef unsigned long long ll;

#define all(a) a.begin(), a.end()
#define sz(a) (int)a.size()
#define clr(a, v) memset((a), (v), sizeof(a))
#define forn(i, n) for (int i = 0; i < (n); ++i)

const int inf=1000000000;

char s[256];
int x[32];
int a[32];
int n;

char f[1<<22][2];
int next[1<<22][2];

char rec(int m, int i, int gr) {
 if (i>=n) return gr;
 char& res=f[m][gr];
 if (res!=-1) return res;
 res=0;
 if (gr==1) {
  for (int j=0; j<n; ++j) if ((~m&(1<<j)) && (i>0 || a[j]>0)) {
   char t=rec(m|(1<<j), i+1, gr);
   if (t && !res) {
    res=t;
    next[m][gr]=j;
    break;
   }
  }
 } else {
  for (int j=0; j<n; ++j) if ((~m&(1<<j)) && (i>0 || a[j]>0)) {
   if (a[j]>=x[i]) {
    char t=rec(m|(1<<j), i+1, a[j]>x[i]);
    if (t && !res) {
     res=t;
     next[m][gr]=j;
     break;
    }
   }
  }
 }
 return res;
}

void make(int m, int i, int gr) {
 if (i>=n) return;
 int j=next[m][gr];
 putchar('0'+a[j]);

 make(m|(1<<j), i+1, max(gr, int(a[j]>x[i])));
}



int main() {
 freopen("b.in", "r", stdin);
 freopen("bb.out", "w", stdout);

 int nt; scanf("%d", &nt);
 gets(s);

 for (int tc=1; tc<=nt; ++tc) {
  gets(s);
  n=strlen(s);
 
  for (int i=0; i<n; ++i)
   x[i]=a[i]=s[i]-'0';


  
  for (;;) {
   sort(a, a+n);

   memset(f, 0xff, sizeof(f));
   if (rec(0, 0, 0)) {
    printf("Case #%d: ", tc);
    make(0, 0, 0);
    puts("");
    break;
   }

   reverse(x, x+n);
   x[n++]=0;
   reverse(x, x+n);
   a[n-1]=0;   
  }




  
  
 }

 return 0;
}
