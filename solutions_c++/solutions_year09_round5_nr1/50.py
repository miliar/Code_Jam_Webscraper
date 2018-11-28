#include <cstdio>
#include <set>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int moves[4][2]={{0,1},{1,0},{0,-1},{-1,0}};

int n, m, total, ans;
char field[20][20];
long long s, f;
vector<long long> q;
map<long long, int> res;

void push(long long x){
  q.push_back(x);
}

bool con(int p1, int p2){
  //return (p1+m == p2) || (p1-m == p2) || (p1%m < m-1 && p1+1==p2) || (p1%m>0 && p1-1==p2);
  int cx1=p1/m, cy1=p1%m;
  int cx2=p2/m, cy2=p2%m;
  for (int z=0; z<4; z++){
    if (cx1+moves[z][0]==cx2 && cy1+moves[z][1]==cy2) return true;
  }
  return false;
}

bool stable(int * wh){
  char used[7]={0};
  used[0] = 1;
  int i, j, h;
  for (i=1; i<total; i++){
    for (j=0; j<total; j++){
      if (!used[j]) continue;
      for (h=0; h<total; h++){
        if (used[h]) continue;
        if (con(wh[j], wh[h])){
          used[h] = 1;
        }
      }
    }
  }
  for (i=0; i<total; i++){
    if (!used[i]) return false;
  }
  return true;
}

void check(int * nwh, bool was_stable, int nd){
  int i, j, zwh[7];
  long long nmask = 0;
  for (i=0; i<total; i++){
    for (j=i+1; j<total; j++){
      if (nwh[i]==nwh[j]) return;
    }
    zwh[i] = nwh[i];
  }
  bool Z = stable(nwh);
  if (!was_stable && !Z) return;
  sort(zwh, zwh+total);
  for (i=0; i<total; i++){
    nmask *= (n*m);
    nmask += zwh[i];
  }
  if (res.find(nmask) != res.end()) return;
  res[nmask] = nd;
  q.push_back(nmask);
}

void go(long long cur){
  int i, wh[7], nwh[7];
  char occ[20][20]={0};
  int nd = res[cur] + 1;
  for (i=0; i<total; i++){
    wh[i] = (int)(cur % (n*m));
    occ[wh[i]/m][wh[i]%m] = 1;
    cur /= n*m;
  }
  bool S = stable(wh);
  for (i=0; i<total; i++){
    memcpy(nwh, wh, sizeof(wh));
    int cx=wh[i]/m, cy=wh[i]%m;
    if (cy<m-1 && field[cx][cy+1]!='#' && cy>0 && field[cx][cy-1] != '#' && !occ[cx][cy-1]){
      nwh[i] = wh[i]+1;
      check(nwh, S, nd);
    }
    if (cy>0 && field[cx][cy-1]!='#' && cy<m-1 && field[cx][cy+1]!='#' && !occ[cx][cy+1]){
      nwh[i] = wh[i]-1;
      check(nwh, S, nd);
    }
    if (cx<n-1 && field[cx+1][cy]!='#' && cx>0 && field[cx-1][cy]!='#' && !occ[cx-1][cy]){
      nwh[i] = wh[i]+m;
      check(nwh, S, nd);
    }
    if (cx>0 && field[cx-1][cy]!='#' && cx<n-1 && field[cx+1][cy]!='#' && !occ[cx+1][cy]){
      nwh[i] = wh[i]-m;
      check(nwh, S, nd);
    }
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    scanf("%d%d\n", &n, &m);
    int i, j;
    total = 0;
    s = f = 0;
    for (i=0; i<n; i++){
      gets(field[i]);
      for (j=0; j<m; j++){
        if (field[i][j]=='w' || field[i][j]=='x'){
          total++;
          f *= n*m;
          f += (i*m + j);
        }
        if (field[i][j]=='w' || field[i][j]=='o'){
          s *= n*m;
          s += (i*m + j);
        }
      }
    }
    q.clear();
    res.clear();
    push(s);
    res[s] = 0;
    ans = -1;
    for (i=0; i<(int)q.size(); i++){
      long long cur = q[i];
      if (cur == f){
        ans = res[f];
        break;
      }
      else go(cur);
    }
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
