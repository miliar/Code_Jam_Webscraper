#include <iostream>
#include <algorithm>
using namespace std;

template<class T>
T choose(int n, int k) {
  k >?= n-k;
  T c = 1;
  for(int i = 1; i <= n-k; ++i)
    c *= k+i, c /= i;
  return c;
}

typedef long long ll;

ll bin[41][41];

int main() {
	for(int i=0;i<=40;++i)
		for(int j=0;j<=40;++j)
			bin[i][j]=choose<ll>(i,j);
	double proba[41], probb[41];
	int T;
	scanf("%d",&T);
	for(int t=0;t<T;++t) {
		double *pa = proba, *pb = probb;
		memset(proba, 0, sizeof(proba));
		int N,C;
		scanf("%d%d",&C,&N);
		pa[N]=1;
		double e=N<C?0:1,d=1;
		for(int i=0;i<10000 ;++i) {//&& (e<1 || d>1e-10)
			memset(pb, 0, sizeof(probb));
			for(int c=0;c<=C;++c) {
				for(int c2=max(0,c-N);c2<=c;++c2) {
					pb[c]+=(pa[c2]*bin[C-c2][c-c2]*bin[c2][N+c2-c])/bin[C][N];//bin[N][c-c2]*
				}
			}
			d=(i+2)*(pb[C]-pa[C]);
			e+=d;
			swap(pa,pb);
		}
		printf("Case #%d: %.7lf\n",t+1,e);
	}
}