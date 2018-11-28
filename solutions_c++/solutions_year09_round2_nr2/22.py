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

string s;

void doit()
{
  int n=SIZE(s);
  int poz=n-1;
  while (poz>0 && s[poz-1]>=s[poz]) poz--;
  if (!poz)
  {
    string a;
    REP(i,n) if (s[i]!='0') a+=s[i];
    sort(ALL(a));
    int x=n+1-SIZE(a);
    string b; b+=a[0];
    REP(i,x) b+='0';
    FOR(i,1,n-1) b+=a[i];
    puts(b.c_str());
  } else
  {
    char mi='9'; mi++;
    int mii=-1;
    FOR(i,poz,n-1) if (s[i]>s[poz-1] && s[i]<mi) { mi=s[i]; mii=i; }
    swap(s[poz-1],s[mii]);
    sort(s.begin()+poz,s.end());
    puts(s.c_str());
  }
}

int main()
{
  scanf("%d",&ILE);
  FOR(LICZ,1,ILE)
  {
    printf("Case #%d: ",LICZ);
    char st[100];
    scanf("%s",st);
    s=string(st);
    doit();
  }
  return 0;
}
