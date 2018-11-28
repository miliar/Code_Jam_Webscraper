#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

struct W {
  int b, e, w;
  W(int b, int e, int w)
    : b(b), e(e), w(w) { }
};
bool operator < (const W& a, const W& b) {
  return a.w < b.w;
}

int main()
{
  int T, C;

  scanf("%d", &T);
  for(C=1; C<=T; ++C) {
    int X, S, R, N;
    double t;
    scanf("%d%d%d%lf%d", &X, &S, &R, &t, &N);

    vector<W> ws;
    double walklen = X, addtime = 0;
    for(int i=0; i<N; ++i) {
      int b, e, w;
      scanf("%d%d%d", &b, &e, &w);
      walklen -= e - b;
      addtime += (e - b) / (double)(S + w);
      ws.push_back(W(b, e, w));
    }
    sort(ws.begin(), ws.end());

    double time = 0;
    if(walklen / R > t) {
      time = t + (walklen - R * t) / S + addtime;
    } else {
      time = walklen / R;
      t -= time;
      for(int i=0; i<N; ++i) {
	W w = ws[i];
	double len = w.e - w.b;
	if(len / (R + w.w) > t) {
	  time += t + (len - (R + w.w) * t) / (S + w.w);
	  t = 0;
	} else {
	  time += len / (R + w.w);
	  t -= len / (R + w.w);
	}
      }
    }
    printf("Case #%d: %.9f\n", C, time);
  }
  return 0;
}
