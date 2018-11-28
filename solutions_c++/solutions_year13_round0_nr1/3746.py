/**
 * @author neko13
 */
#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
// 13C
#define DBG 0
#define sz(c) ((int)(c).size())
#define   forl(i, a, b) for(int i = (a); i <  (b); ++i)
#define  forle(i, a, b) for(int i = (a); i <= (b); ++i)
#define   forg(i, a, b) for(int i = (a); i >  (b); --i)
#define  forge(i, a, b) for(int i = (a); i >= (b); --i)
#define  forlc(i, a, b) for(int i##_b = (b), i = (a); i <  i##_b; ++i)
#define forlec(i, a, b) for(int i##_b = (b), i = (a); i <= i##_b; ++i)
#define  forgc(i, a, b) for(int i##_b = (b), i = (a); i >  i##_b; --i)
#define forgec(i, a, b) for(int i##_b = (b), i = (a); i >= i##_b; --i)
#define  forls(i, n, a, b) for(int i = a; i != b; i = n[i])
#define rep(n)  for(int               repp = 0; repp <    (n); ++repp)
#define repc(n) for(int repp_b = (n), repp = 0; repp < repp_b; ++repp)
#define rst(a, v) memset(a, v, sizeof a)
#define cpy(a, b) memcpy(a, b, sizeof a)
#define rstn(a, v, n) memset(a, v, (n)*sizeof((a)[0]))
#define cpyn(a, b, n) memcpy(a, b, (n)*sizeof((a)[0]))
#define ast(b) if(DBG && !(b)) { printf("!! %d\n", __LINE__); while(1) getchar(); }
#define dout DBG && cout << ">>| "
#define pr(x) #x"=" << (x) << " | "
#define mk(x) DBG && cout << "**| "#x << endl
#define pra(arr, a, b) if(DBG) { \
    dout<<#arr"[] | "; \
    forlec(i, a, b) cout<<"["<<i<<"]="<<arr[i]<<" |"<<((i-(a)+1)%13?" ":"\n"); \
    if(((b)-(a)+1)%13) puts(""); \
  }
#define rd(type, x) type x; cin >> x
inline int     rdi() { int d; scanf("%d", &d); return d; }
inline char    rdc() { scanf(" "); return getchar(); }
inline string  rds() { rd(string, s); return s; }
inline double rddb() { double d; scanf("%lf", &d); return d; }
template<class T> inline bool updateMin(T& a, T b) { return a>b? a=b, true: false; }
template<class T> inline bool updateMax(T& a, T b) { return a<b? a=b, true: false; }

char a[5][5];

bool equ(char x, char y) { return y==x || y=='T'; }

bool won(char x) {
  forl(i, 0, 4) {
    if(equ(x, a[i][0]) && equ(x, a[i][1]) && equ(x, a[i][2]) && equ(x, a[i][3])) return true;
    if(equ(x, a[0][i]) && equ(x, a[1][i]) && equ(x, a[2][i]) && equ(x, a[3][i])) return true;
  }
  if(equ(x, a[0][0]) && equ(x, a[1][1]) && equ(x, a[2][2]) && equ(x, a[3][3])) return true;
  if(equ(x, a[0][3]) && equ(x, a[1][2]) && equ(x, a[2][1]) && equ(x, a[3][0])) return true;
  return false;
}

bool full() {
  forl(i, 0, 4)
    forl(j, 0, 4)
      if(a[i][j] == '.')
        return false;
  return true;
}

int main() {
  int cas = 0;
  repc(rdi()) {
    forl(i, 0, 4)
      cin >> a[i];
    printf("Case #%d: ", ++cas);
    /**/ if(won('X')) puts("X won");
    else if(won('O')) puts("O won");
    else if(full()) puts("Draw");
    else /*      */ puts("Game has not completed");
  }
  return 0;
}
