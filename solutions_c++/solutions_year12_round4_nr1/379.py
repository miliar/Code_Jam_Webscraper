#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;


int N, d[10100], l[10100], D;
int h[10100];

int main() {
  int T;
  scanf("%d", &T);
  for (int tc=1; tc<=T; tc++) {
    scanf("%d", &N);
    for (int i=0; i<N; i++) scanf("%d %d", d+i, l+i);
    scanf("%d", &D);
    d[N]=D;
    l[N]=0;
    memset(h,-1,sizeof h);

    int x, y;
    x=y=d[0];
    h[0]=y;
    for (int i=0; i<N; i++) {
      y=h[i];
      x=d[i];
      for (int j=i+1; j<=N; j++) {
	if (x+y>=d[j]) h[j]=max(h[j], min(l[j], d[j]-d[i]));
	else break;
      }
    }
    
    printf("Case #%d: %s\n", tc, h[N]?"NO":"YES");
  }

  return 0;
}
