#include <iostream>
using namespace std;
int f[2000] , p[2000] ,next[2000];

int R , K , N;
int find_next(int & tail) {
  int ret = 0;
  int tmp = tail;
  
  if(tail == N)
    tail = 0;

  bool ck = true;
  while(ret + f[tail] <=K && (ck || tmp!=tail)) {
    ck = false;
    ret+=f[tail++];
    
    if(tail == N)
      tail = 0;
  }
  return ret;
}

int main(void) {
  freopen("csmall.in","r",stdin);
  freopen("csmall.out","w",stdout);

  int T , times = 0;
  cin >> T;
  while(T--) {
    ++times;
    cin >> R >> K >> N;
    
    for (int i = 0;i<N;++i)
      cin >> f[i];
    
    for (int i = 0;i<N;++i) {
      int t = i;
      p[i] = find_next(t);
      next[i] = t;
    }

    long long sum = 0;
    int now = 0;
    for (int i = 0;i<R;++i) {
      sum+=p[now];
      now = next[now];
    }
    printf("Case #%d: %I64d\n",times , sum);
  }
  return 0;
}