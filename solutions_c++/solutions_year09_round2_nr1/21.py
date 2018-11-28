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
#include<cassert>
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

int l;
string s;

int ile;

PII t[300000];
double tab[300000];
string tab1[300000];

inline bool white(char ch) { return ch==' ' || ch=='\n' || ch==10 || ch==13; }

int ii;

void parse(int v)
{
  t[v]=MP(-1,-1);
  while (white(s[ii])) ii++;
  assert(s[ii]=='(');
  ii++;
  while (white(s[ii])) ii++;
  string a;
  while (!white(s[ii]) && s[ii]!=')') { a+=s[ii]; ii++; }
  sscanf(a.c_str(),"%lf",tab+v);
  while (white(s[ii])) ii++;
  if (s[ii]==')') { ii++; return; }
  a="";
  while (!white(s[ii]) && s[ii]!='(') { a+=s[ii]; ii++; }
  tab1[v]=a;
  ile++;
  t[v].FI=ile; parse(ile);
  ile++;
  t[v].SE=ile; parse(ile);
  while (white(s[ii])) ii++;
  assert(s[ii]==')');
  ii++;
}

set<string> all;

void zlaz(int v,double p)
{
  p*=tab[v];
  if (t[v].FI==-1) { printf("%.10lf\n",p); return; }
  if (all.count(tab1[v]))
  {
    zlaz(t[v].FI,p);
  } else
  {
    zlaz(t[v].SE,p);
  }
}

int main()
{
  char st[100];
  gets(st);
  sscanf(st,"%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d:\n",LICZ);
    gets(st);
    sscanf(st,"%d",&l);
    s="";
    REP(i,l)
    {
      gets(st); s+=string(st);
    }
    ile=0; ii=0;
//    printf("\"%s\"\n",s.c_str());
    parse(0);
    gets(st);
    int n;
    sscanf(st,"%d",&n);
    char st1[300000];
    REP(i,n)
    {
      gets(st1);
      VS tt(parse(string(st1)));
      all.clear();
      FOR(j,2,SIZE(tt)-1) { all.insert(tt[j]); }
      zlaz(0,1.0);
    }
  }
  return 0;
}
