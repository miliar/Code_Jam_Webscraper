/* This is a problem from POI :)
http://main.edu.pl/en/archive/oi/6/pie
*/

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


#define MAX 500

bool edge[MAX][MAX],visited[MAX],need[MAX];
int indeg[MAX],outdeg[MAX];
int wyn;

set<PII> zb;

inline void dodaj(int a,int b)
{
  if (zb.count(MP(a,b))) return;
  zb.insert(MP(a,b)); ++wyn;

  //  printf("%c %c %d %d\n",char(a),char(b),a,b);

  edge[a][b]=edge[b][a]=true;
  need[a]=need[b]=true;
  ++outdeg[a];
  ++indeg[b];
}

int comp_res;

void dfs(int v)
{
  visited[v]=true;
  if (indeg[v]>outdeg[v]) comp_res += indeg[v]-outdeg[v];
  FOR(i,1,MAX) if (need[i] && !visited[i] && edge[v][i]) dfs(i);
}

int ILE;
int k,n;
char st[10000];

char leet[1000];

int main()
{
  leet['o']='0';
  leet['i']='1';
  leet['e']='3';
  leet['a']='4';
  leet['s']='5';
  leet['t']='7';
  leet['b']='8';
  leet['g']='9';

  scanf("%d",&ILE);
  FOR(iii,1,ILE)
  {
    printf("Case #%d: ",iii);
    fprintf(stderr,"Case #%d: \n",iii);
    memset(edge,0,sizeof(edge));
    memset(visited,0,sizeof(visited));
    memset(need,0,sizeof(need));
    memset(outdeg,0,sizeof(outdeg));
    memset(indeg,0,sizeof(indeg));
    zb.clear();

    scanf("%d",&k);
    scanf("%s",st);
    n=strlen(st);
    wyn=0;
    REP(i,n-1)
    {
      char a=st[i],b=st[i+1];
      dodaj(a,b);
      if (leet[a]) dodaj(leet[a],b);
      if (leet[b]) dodaj(a,leet[b]);
      if (leet[a]&&leet[b]) dodaj(leet[a],leet[b]);
    }

    FOR(i,1,MAX-1) if (need[i] && !visited[i])
    {
      comp_res=0;
      dfs(i);
      wyn+=comp_res;
      if (!comp_res) ++wyn;
    }
    printf("%d\n",wyn);
  }
  return 0;
}
