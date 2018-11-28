#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <queue>
#include <deque>
using namespace std;


#define pb push_back
#define mp make_pair
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(int)(n); ++i)
#define all(a) (a).begin(), (a).end()
        
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;

map<ll,int> d;
queue<ll> q;


char tab[15][15];
char bad[15][15];
vector<pii> s, t;
int n, m, k;

inline ll getID(vector<pii> a) {
 sort(all(a));
 ll res=0;
 forn (i, k) {
  res=(res<<4)+a[i].first;
  res=(res<<4)+a[i].second;
 }  
 return res;
}

void getState(ll res, vector<pii>& a) {
 a.clear();
 forn (i, k) {
  int yy=res&15; res>>=4;
  int xx=res&15; res>>=4;
  a.pb(mp(xx, yy));
 }
 reverse(all(a));
}

int dx[]={0,0,-1,1};
int dy[]={-1,1,0,0};

inline bool neig(int x1, int y1, int x2, int y2) {
 forn (i, 4) if (x1+dx[i]==x2 && y1+dy[i]==y2) return true;
 return false;
}

inline bool good(vector<pii>& a) {
 if (k==1) return true;
 forn (i, k) {
  bool ok=0;
  forn (j, k) if (i!=j)
   ok|=neig(a[i].first, a[i].second, a[j].first, a[j].second);
  if (!ok) return false;
 }
 return true;
}



int solve(ll S, ll T) {
 vector<pii> a, b;
 d[S]=0;
 q.push(S);
 while (!q.empty()) {
  ll x=q.front();
  q.pop();
  int dd=d[x];           
  if (x==T) return dd;

  

  forn (i, n) forn (j, m) bad[i][j]=0;
  getState(x, a);
  bool con=good(a);
  forn (i, k) bad[a[i].first][a[i].second]=1;

  forn (i, k) {
   int x=a[i].first, y=a[i].second;

   forn (j, 4) {
    int x1=x+dx[j], y1=y+dy[j];
    int x2=x-dx[j], y2=y-dy[j];
    if (x1<0 || x1>=n || y1<0 || y1>=m || tab[x1][y1]=='#' || bad[x1][y1]) continue;
    if (x2<0 || x2>=n || y2<0 || y2>=m || tab[x2][y2]=='#' || bad[x2][y2]) continue;

    b=a;
    b[i]=mp(x1, y1);

    bool con2=good(b);

    if (con2 || con) {
     ll y=getID(b);
     if (d.count(y)==0) {
      d[y]=dd+1, q.push(y);
     }
    }
   }

  }                        


 }
 return -1;
}

int main() {
 freopen("a.in", "r", stdin);
 freopen("a.out", "w", stdout);

 int nt; scanf("%d\n", &nt);
 for (int tc=1; tc<=nt; ++tc) {
  scanf("%d %d", &n, &m); gets(tab[0]);
  forn (i, n) gets(tab[i]);

  d.clear();
  while (!q.empty()) q.pop();

  k=0;
  s.clear();
  t.clear();
  forn (i, n) forn (j, m) if (tab[i][j]=='o' || tab[i][j]=='w') ++k, s.pb(mp(i, j));
  forn (i, n) forn (j, m) if (tab[i][j]=='x' || tab[i][j]=='w') t.pb(mp(i, j));
  forn (i, n) forn (j, m) if (tab[i][j]!='#' && tab[i][j]!='.') tab[i][j]='.';

  ll S=getID(s);
  ll T=getID(t);

  int res=solve(S, T);

  printf("Case #%d: %d\n", tc, res);


 }

 return 0;
}

