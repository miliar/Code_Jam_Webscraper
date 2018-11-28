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

void wypisz(PII p)
{
  printf("(%d %d)\n",p.FI,p.SE);
}
void wypisz(VI t)
{
  REP(i,SIZE(t)) printf("%d ",t[i]); puts("");
}
void wypisz(vector<PII> t)
{
  REP(i,SIZE(t)) printf("(%d %d) ",t[i].FI,t[i].SE); puts("");
}
void wypisz(VS t)
{
  REP(i,SIZE(t)) printf("%s\n",t[i].c_str());
}
void wypisz(vector<VI> t)
{
  REP(i,SIZE(t)) wypisz(t[i]);
}


int ILE;
int n,s,p;
int t[200];
int tab[120][120];

int main()
{
  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    scanf("%d%d%d",&n,&s,&p);
    REP(i,n) scanf("%d",t+i);
    FOR(j,0,100) FOR(i,0,100) tab[j][i]=-INFTY;
    tab[0][0]=0;
    REP(i,n)
    {
      int special_i_suma=0, special=0, suma=0, zadne=0;
      FOR(a,0,10) FOR(b,a,10) FOR(c,b,min(a+2,10)) if (a+b+c==t[i])
      {
        if (c-a==2 && c>=p) special_i_suma=1;
        else if (c-a==2) special=1; else if (c>=p) suma=1; else zadne=1;
      }
      FOR(j,0,100) if (tab[i][j]>=0)
      {
        if (special_i_suma) tab[i+1][j+1]=max(tab[i+1][j+1],tab[i][j]+1);
        if (special) tab[i+1][j+1]=max(tab[i+1][j+1],tab[i][j]);
        if (suma) tab[i+1][j]=max(tab[i+1][j],tab[i][j]+1);
        if (zadne) tab[i+1][j]=max(tab[i+1][j],tab[i][j]);
      }
    }
    printf("%d\n",tab[n][s]);
  }
  return 0;
}
