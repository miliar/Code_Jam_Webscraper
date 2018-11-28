#include<cstdio>
#include<algorithm>

using namespace std;

struct st {
  int p, t, id;
};
bool operator < (const st& a, const st& b)
{
  if(a.p * b.t != b.p * a.t)
    return b.p * a.t < a.p * b.t;
  return a.id < b.id;
}

st S[1024];

int main()
{
  int T;
  scanf("%d", &T);
  
  for(int CN=1; CN<=T; ++CN) {
    int N;
    scanf("%d", &N);
    
    for(int i=0; i<N; ++i) {
      int t;
      scanf("%d", &t);
      S[i].t = t;
      S[i].id = i;
    }
    
    for(int i=0; i<N; ++i) {
      int p;
      scanf("%d", &p);
      S[i].p = p;
      S[i].id = i;
    }
    
    sort(S, S+N);
    
    printf("Case #%d:", CN);
    for(int i=0; i<N; ++i)
      printf(" %d", S[i].id);
    puts("");
  }
  
  return 0;
}
