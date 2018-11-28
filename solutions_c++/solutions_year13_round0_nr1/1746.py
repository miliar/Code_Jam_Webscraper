#include <iostream>
#include <iomanip>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
using namespace std;
#define INF 0x7fffffff
#define LL long long
#define LD long double
#define PII pair<int,int>
#define x first
#define y second
#define pb push_back
#define sz(a) int(a.size())
#define all(a) a.begin(),a.end()
#define For(i,a,b) for(int i=a;i<=b;i++)
#define dbg(x) cerr<<__LINE__<<": "<<#x<<" = "<<(x)<<endl

char map[8][8];
string ans,st;

inline int same(char &a,char &b,char &c,char &d) {
  st=a;
  st+=b;
  st+=c;
  st+=d;
  sort(all(st));
  st.resize(unique(all(st))-st.begin());
  if (sz(st)==1) return 1;
  if (sz(st)>2) return 0;
  if (st[0]=='T') swap(st[0],st[1]);
  return st[0]=='O'&&st[1]=='T' ||
         st[0]=='X'&&st[1]=='T';
}

inline void check(int r,int c) {
  if (same(map[r][1],map[r][2],map[r][3],map[r][4])) {
    ans=st.substr(0,1)+" won";
  } else
  if (same(map[1][c],map[2][c],map[3][c],map[4][c])) {
    ans=st.substr(0,1)+" won";
  } else
  if (r==1&&c==1 || r==4&&c==4) {
    if (same(map[1][1],map[2][2],map[3][3],map[4][4])) {
      ans=st.substr(0,1)+" won";
    }
  } else
  if (r==1&&c==4 || r==4&&c==1) {
    if (same(map[1][4],map[2][3],map[3][2],map[4][1])) {
      ans=st.substr(0,1)+" won";
    }
  }
}

int main() {
  freopen("A-large.in","r",stdin);
  freopen("OUT2","w",stdout);
  int T;
  scanf("%d",&T);
  For(t,1,T) {
    For(i,1,4) scanf("%s",map[i]+1);

    ans="";
    int emp=0;
    for (int i=1;i<=4;i++)
      for (int j=1;j<=4;j++)
        if (map[i][j]=='X' ||
            map[i][j]=='O' ||
            map[i][j]=='T') {
          check(i,j);
          if (ans!="") goto End;
        } else emp++;

    if (!emp) ans="Draw";
         else ans="Game has not completed";

    End: printf("Case #%d: %s\n",t,ans.data());
  }
  return 0;
}

