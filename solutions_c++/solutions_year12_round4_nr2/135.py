#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;
int T,N,W,L,t;
int i,j,k,cnt,dx,dy;

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);

  scanf("%d",&T);
  for (t=1;t<=T;t++) {
    scanf("%d%d%d",&N,&W,&L);
    vector<int> r(N);
    for (i=0;i<N;i++)
      scanf("%d",&r[i]);

    #define Pii pair<int,int>
    vector<Pii > S(N);
    for (i=0;i<N;i++) {
      S[i].first=r[i];
      S[i].second=i;
    }
    sort(S.begin(),S.end(),greater<Pii >());

    vector<int> X(N),Y(N);
    for (i=cnt=0;i<W;i+=dx) {
      dx=S[cnt].first;
      for (j=0;j<=L;j+=dy) {
        dy=S[cnt].first;
        X[S[cnt].second]=i;
        Y[S[cnt].second]=j;
        if (++cnt>=N) break;
        dy+=S[cnt].first;
      }
      if (cnt>=N) break;
      dx+=S[cnt].first;
    }

    printf("Case #%d: ",t);
    for (i=0;i<N;i++)
      printf("%d %d%s",X[i],Y[i],i+1==N?"\n":" ");
  }
  return 0;
}
