#include <cstdio>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

const int S = 12;
const int Q = 1010;
const int INF = 5000;
int memo[Q][S];
int query[Q];

int read_int(){
  char buf[1000];
  gets(buf);
  int x;
  sscanf(buf, "%d", &x);
  return x;
}

string read_str(){
  char buf[1000];
  gets(buf);
  return string(buf);
}

int calc(int q, int s, int ss){
  int& res = memo[q][s];
  if(res >= 0){return res;}
  if(q == 0){return res = 0;}
  if(query[q] == s){return res = INF;}
  int r = INF;
  for(int i = 0; i < ss; ++i){
    r = min(r, calc(q-1, i, ss) + (i == s ? 0 : 1));
  }
  return res = r;
}

int solve(){
  int s = read_int();
  map<string, int> s2i;
  for(int i = 0; i < s; ++i){s2i[read_str()] = i;}
  int q = read_int();
  for(int i = 0; i < q; ++i){
    query[i+1] = s2i[read_str()];
  }
  for(int i = 0; i <= q; ++i)for(int j = 0; j < s; ++j){memo[i][j] = -1;}
  int res = INF;
  for(int i = 0; i < s; ++i){res = min(res, calc(q, i, s));}
  /*
  for(int i = 0; i <= q; ++i){
    for(int j = 0; j < s; ++j){printf("%d ", memo[i][j]);}
    puts("");
  }
  */
  return res;
}

int main(){
  int t = read_int();
  for(int c = 1; c <= t; ++c){
    printf("Case #%d: %d\n", c, solve());
  }
  return 0;
}
