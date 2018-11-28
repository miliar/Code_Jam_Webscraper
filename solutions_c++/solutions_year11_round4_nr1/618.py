#include<stdio.h>
#include<algorithm>
using namespace std;

int walkway[1000][3];
pair<int, int> seg[2010];
double solve() {
	int X, S, R, t, N;
	scanf("%d%d%d%d%d", &X, &S, &R, &t, &N);

	int last=0, p=0;
	for(int i=0;i<N;i++) {
		int b, e, w;
		scanf("%d%d%d", &b, &e, &w);

		seg[p].first=0;
		seg[p].second=b-last;
		p++;

		seg[p].first=w;
		seg[p].second=e-b;
		p++;

		last=e;
	}
	seg[p].first=0;
	seg[p].second=X-last;
	p++;

	sort(seg, seg+p);

	double time=0, leftTime=t;
	for(int i=0;i<p;i++) {
		int len=seg[i].second, w=seg[i].first;
		double tt=(double)len/(w+R);
		if(tt>leftTime) {
			time+=(double)(len-(w+R)*leftTime)/(w+S)+leftTime;
			leftTime=0;
		} else {
			time+=tt;
			leftTime-=tt;
		}
	}

	return time;
}

int main() {
	int t;
	scanf("%d", &t);
	for(int c=1;c<=t;c++) {
		printf("Case #%d: %.8lf\n", c, solve());
	}
}