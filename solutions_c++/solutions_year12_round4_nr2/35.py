#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define FOR(i, s, t) for(i = (s); i < (t); i++)
#define RFOR(i, s, t) for(i = (s)-1; i >= (t); i--)

struct T{
  int l, r, h;
};

vector<T> s;
pair<int, int> r[1004];
int x[1004], y[1004];
int W, H;

void insert(int pos, T t){
  s.resize(s.size()+1);
  for(int i = s.size()-2; i >= pos; i--)
    s[i+1] = s[i];
  s[pos] = t;
}

void erase(int pos){
  while(pos+1 < s.size()){
    s[pos] = s[pos+1];
    pos++;
  }
  s.resize(s.size()-1);
}

int main()
{
  #ifdef __FIO
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);
  #endif
  int _;
  scanf("%d", &_);
  for(int i0 = 1; i0 <= _; i0++){
    printf("Case #%d: ", i0);
    int n;
    int i, j, k;
    scanf("%d%d%d", &n, &W, &H);
    for(i = 0; i < n; i++){
      scanf("%d", &r[i].fi);
      r[i].se = i;
    }
    sort(r, r+n, greater<pair<int, int> >());
    s.clear();
    x[r[0].se] = 0;
    y[r[0].se] = 0;
    j = r[0].fi;
    s.pb((T){0, j, r[0].fi});
    for(i = 1; i < n; i++){
      if(j+r[i].fi > W){
        s[s.size()-1].r = W;
        break;
      }
      x[r[i].se] = j+r[i].fi;
      y[r[i].se] = 0;
      s.pb((T){j, j+r[i].fi*2, r[i].fi});
      j += r[i].fi*2;
    }
    for(; i < n; i++){
      k = 0;
      for(j = 1; j < s.size(); j++)
        if(s[j].h < s[k].h)
          k = j;
      if(s[k].l == 0){
        if(s[k].r < r[i].fi){
          if(s[k].r == W){
            x[r[i].se] = 0;
            y[r[i].se] = s[k].h+r[i].fi;
            s[k].h += r[i].fi*2;
          }
          else{
            s[k+1].l = s[k].l;
            erase(k);
            i--;
          }
        }
        else{
          x[r[i].se] = 0;
          y[r[i].se] = s[k].h+r[i].fi;
          s[k].l = r[i].fi;
          insert(k, (T){0, r[i].fi, s[k].h+r[i].fi*2});
        }
      }
      else if(s[k].r == W){
        if(W-s[k].l < r[i].fi){
          s[k-1].r = s[k].r;
          erase(k);
          i--;
        }
        else{
          x[r[i].se] = W;
          y[r[i].se] = s[k].h+r[i].fi;
          s[k].r = W-r[i].fi;
          insert(k+1, (T){W-r[i].fi, W, s[k].h+r[i].fi*2});
        }
      }
      else if(s[k].r-s[k].l < r[i].fi*2){
        if(s[k-1].h > s[k+1].h)
          s[k+1].l = s[k].l;
        else
          s[k-1].r = s[k].r;
        erase(k);
        i--;
      }
      else{
        x[r[i].se] = s[k].l+r[i].fi;
        y[r[i].se] = s[k].h+r[i].fi;
        insert(k, (T){s[k].l, s[k].l+r[i].fi*2, s[k].h+r[i].fi*2});
        s[k+1].l = s[k+1].l+r[i].fi*2;
      }
    }
    for(i = 0; i < n; i++)
      printf("%d %d ", x[i], y[i]);
    printf("\n");
  }
  return 0;
}
