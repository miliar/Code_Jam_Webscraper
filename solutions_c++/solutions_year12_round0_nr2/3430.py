#include<cstdio>
#include<algorithm>
using namespace std;
#define N 100
#define JT 1.0/3.0
int t[N];
int n,m,s,p;

int main(int argc, const char *argv[]){
  scanf("%d", &n);
  for(int i=1; i<=n; i++){
    int l =0;
    scanf("%d%d%d", &m, &s, &p);
    for(int j=0; j<m; j++){
      scanf("%d", &t[j]);
    }
    sort(t, t+m);
    m--;
    while((t[m]+2)/3.0>=p && m>=0){
      l++;
      m--;

    }
    while((t[m]+4)/3.0>=p && m>=0 && s && t[m]>=2){
      l++;
      m--;
      s--;

    }
  printf("Case #%d: %d\n",i, l);
  }

  return 0;
}
