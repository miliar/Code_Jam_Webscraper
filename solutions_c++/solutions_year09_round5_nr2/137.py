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
#include<numeric>
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

int los(int m)
{
  return (int)((double)m*(rand()/(RAND_MAX+1.0)));
}

char poly[10000];
VS pol;
int n,k;

int tab[200][30];

#define M 10009

void odczyt()
{
  scanf("%s",poly);
  scanf("%d%d",&k,&n);
  REP(i,n)
  {
    char st[1000];
    scanf("%s",st);
    REP(j,28) tab[i][j]=0;
    int l=strlen(st);
    REP(j,l) tab[i][st[j]-'a']++;
  }
  int i=0;
  int l=strlen(poly);
  pol.clear();
  while (1)
  {
    int i0=i;
    while (i<l && poly[i]!='+')
    {
      i++;
    }
    string a=string(poly+i0,poly+i);
    pol.PB(a);
    i++;
    if (i>=l) break;
  }
//  REP(ii,SIZE(pol)) puts(pol[ii].c_str());
}

int dwum[101][101];

int tt[30];
string a;
int wyn[10];

void brut(int poz,int d)
{
  if (poz==d)
  {
    int akt=1;
    REP(i,SIZE(a)) { akt*=tt[a[i]-'a']; akt%=M; }
    wyn[d]=(wyn[d]+akt)%M;
    return;
  }
  REP(i,n)
  {
    REP(j,26) tt[j]+=tab[i][j];
    brut(poz+1,d);
    REP(j,26) tt[j]-=tab[i][j];
  }
}

void doit(string s)
{
  a=s;
  dwum[0][0]=1;
  FOR(i,1,100)
  {
    dwum[i][0]=dwum[i][i]=1;
    FOR(j,1,i-1) dwum[i][j]=(dwum[i-1][j-1]+dwum[i-1][j])%M;
  }
  FOR(d,1,k)
  {
    brut(0,d);
  }
}

int main()
{
  int ILE;
  scanf("%d",&ILE);
  FOR(II,1,ILE)
  {
    printf("Case #%d:",II);
    odczyt();
    FOR(i,1,k) wyn[i]=0;
    REP(i,SIZE(pol)) doit(pol[i]);    
    FOR(i,1,k) printf(" %d",wyn[i]);
    puts("");
  }
  return 0;
}
