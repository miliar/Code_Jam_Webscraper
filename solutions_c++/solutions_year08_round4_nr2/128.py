/* Jakub Radoszewski (jakubr) */

//#include<iostream>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<algorithm>
#include<vector>
#include<string>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<utility>
#include<sstream>
#include<cstring>
using namespace std;

#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define ALL(X) (X).begin(),(X).end()
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define INFTY 100000000
#define VAR(V,init) __typeof(init) V=(init)
#define FORE(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define SIZE(x) ((int)(x).size())

typedef vector<int> VI;
typedef pair<int,int> PII;
typedef long long ll;
typedef vector<string> VS;

ll nwd(ll a,ll b) { return !b?a:nwd(b,a%b); }
inline int CEIL(int a,int b) { return a%b ? a/b+1 : a/b; }
template <class T> inline T sqr(const T&a) { return a*a; }

VS parse(string s)
{
  string a;
  VS wyn;
  REP(i,(int)s.size())
    if (s[i]!=' ') a+=s[i];
    else if (!a.empty()) { wyn.PB(a); a=""; }
  if (!a.empty()) wyn.PB(a);
  return wyn;
}

int toi(char ch) { return int(ch)-int('0'); }

int chg(char ch) { return int(ch)-int('a'); }

int ILE;

int n,m,A;
VI w;

/* Pasted code */
/* Algorytm Euklidesa. */

/* Rozszerzony Euklides.
 * Dla a i b podaje (p,q,d) takie, ze ap+bq=d. */
void euclid(int a, int b, ll &p, ll &q, int &d)
{
  if (!b) { p=1; q=0; d=a; } else
  {
    ll p1,q1; int d1;
    euclid(b,a%b,p1,q1,d1);
    d=d1;
    p=q1; q=p1-q1*(a/b);
  }
}

/* Odwrotnosc v modulo p (NWD(v,p)=1). */
int odwrotnosc(int v,int p)
{
  ll x,y; int z;
  euclid(v,p,x,y,z);
  return int(x%p+p)%p;
}



inline void spr(int x,int y)
{
  if (SIZE(w)>2) return;
  if (!x && !y) return;
  if (!y)
  {
    if ((A%x==0) && A/x<=m)
    {
      w.PB(x); w.PB(y); w.PB(0); w.PB(A/x); return;
    } else return;
  }
  if (y==1)
  {
    if (!x) return;
    int b=(A+x-1)/x;
    int bx=b*x;
    int a=bx-A;
    if (a>=0 && a<=n && b>=0 && b<=m)
    {
      w.PB(x); w.PB(y); w.PB(a); w.PB(b); return;
    } else return;
  }
}

void chk()
{
  int s=(w[2]-w[0])*(w[5]-w[1])-(w[4]-w[0])*(w[3]-w[1]);
  if (abs(s)!=A) { puts("WA"); exit(0); }
}

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d:",LICZ);
    scanf("%d%d%d",&n,&m,&A);
    w.clear();
    w.PB(0); w.PB(0);
    FOR(x,0,n) FOR(y,0,1) spr(x,y);
    if (SIZE(w)>2)
    {
      REP(i,6) printf(" %d",w[i]); puts("");
      chk();
      continue;
    }    
    swap(n,m);
    FOR(x,0,n) FOR(y,0,1) spr(x,y);
    if (SIZE(w)<=2) puts(" IMPOSSIBLE");
    else
    {
      swap(w[0],w[1]); swap(w[2],w[3]); swap(w[4],w[5]);
      chk();
      REP(i,6) printf(" %d",w[i]); puts("");
    }
/*    bool ok=1;
    FOR(i,0,n) if (ok) FOR(j,0,m)
    {
      if (i!=0 && i!=n) continue;
      if (j!=0 && j!=m) continue;
      if (!ok) break;
      FOR(k,0,n) if (ok) FOR(l,0,m) if (ok) FOR(a,0,n) if (ok) FOR(b,0,m)
      {
        if (!ok) break;
        int x1=k-i,y1=l-j,x2=a-i,y2=b-j;
        if (abs(x1*y2-x2*y1)==A)
        {
          printf(" %d %d %d %d %d %d\n",i,j,k,l,a,b);
          ok=0;
          break;
        }
      }
    }
    if (ok) puts(" IMPOSSIBLE");*/
  }
  return 0;
}
