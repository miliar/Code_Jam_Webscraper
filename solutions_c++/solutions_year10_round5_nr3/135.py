#include<stdio.h>
#include<queue>
#include<map>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

map<int,int> f;
LL ans=0;

int n;
priority_queue<pair<int,int> > Q;
int main(){
  int ca;
  scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    f.clear();
    while (!Q.empty()) Q.pop();
    scanf("%d",&n);
    for (int i=0; i<n; i++){
      int x,y; scanf("%d%d",&x,&y);
      f[x]=y;
      if (y>1) Q.push(make_pair(y,x));
    }
    LL ans=0;
    while (!Q.empty()){
      int x = Q.top().second;
      int y = Q.top().first;
      if (y != f[x]){
        Q.pop();
        continue;
      }
      Q.pop();
      f[x] -= 2;
      f[x+1] += 1;
      f[x-1] += 1;
      if (f[x]>1) Q.push(make_pair(f[x],x));
      if (f[x+1]>1) Q.push(make_pair(f[x+1],x+1));
      if (f[x-1]>1) Q.push(make_pair(f[x-1],x-1));
      ans++;
    }
    printf("Case #%d: %lld\n",tt,ans);
  }
  return 0;
}
