#include <cstdio>
#include <algorithm>

using namespace std;
typedef long long LL;
const int M = 1005;

int R,k,N;

int tab[M];
LL sum[M];
int ile[M];

inline int Mod(int i,int n) {
  return (i%n+n)%n;
}

int next[M],prev[M];
bool vis[M];

int cycle_len;
int line_len;
LL cycle_sum;

int main() {
  int d;
  scanf("%d",&d);
  for(int tc=1;tc<=d;++tc) {
    scanf("%d %d %d",&R,&k,&N);
    for(int i=0;i<N;++i)
      scanf("%d",tab+i);
    for(int i=0;i<N;++i) {
      sum[i]=0;
      int cnt=0;
      int ptr=i;
      while(cnt<N && sum[i]+tab[ptr]<=k) {
        ++cnt;
        sum[i]+=tab[ptr];
        ptr=Mod(ptr+1,N);
      }
      ile[i]=cnt;
    }
    for(int i=0;i<N;++i) vis[i]=0;
    int cur=0;
    int poprz=-1;
    int nvisited=0;
    while(!vis[cur]) {
      vis[cur]=true;
      nvisited++;
      if(poprz!=-1) {
        next[poprz]=cur;
        prev[cur]=poprz;
      }
      poprz=cur;
      cur=Mod(cur+ile[cur],N);
    }
    next[poprz]=cur;
    prev[cur]=poprz;
    cycle_len = 1;
    int ptr = next[cur];
    cycle_sum = sum[cur];
    while(ptr != cur) {
      ++ cycle_len;
      cycle_sum += sum[ptr];
      ptr = next[ptr];
    }
    line_len = nvisited-cycle_len;
    LL ret=0;
    int ile_cykli_wykona = (R-line_len)/cycle_len;
    R -= ile_cykli_wykona * cycle_len;
    ret += (LL)ile_cykli_wykona * cycle_sum;
    cur=0;
    while(R) {
      ret += sum[cur];
      -- R;
      cur = Mod(cur+ile[cur],N);
    }
    printf("Case #%d: %lld\n",tc,ret);
  }
  return 0;
}
