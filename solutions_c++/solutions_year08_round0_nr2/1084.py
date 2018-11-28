#include <iostream>
using namespace std;

const int maxt = 24*60+100;

int tomin(int hh, int mm) {
	return hh*60 + mm;
}

int sa[maxt], sb[maxt];

int cnt(int s[]) {
	int c = 0;
	for(int i=0;i<maxt-1;i++) {
		if(s[i] < 0) {
			c -= s[i];
		} else {
			s[i+1] += s[i];
		}
	}
	return c;
}

int main() {
	int n;
	scanf("%d", &n);
	for(int i=0;i<n;i++) {
		memset(sa, 0, sizeof(sa));
		memset(sb, 0, sizeof(sb));

		int t,na,nb;
		scanf("%d%d%d", &t, &na, &nb);
		int h1,h2,m1,m2;
		for(int j=0;j<na;j++) {
			scanf("%d:%d %d:%d", &h1,&m1, &h2,&m2);
			int ta = tomin(h1,m1);
			int tb = tomin(h2,m2);
			sa[ta]--;
			sb[tb+t]++;
		}
		for(int j=0;j<nb;j++) {
			scanf("%d:%d %d:%d", &h1,&m1, &h2,&m2);
			int tb = tomin(h1,m1);
			int ta = tomin(h2,m2);
			sb[tb]--;
			sa[ta+t]++;
		}

		// process
		printf("Case #%d: %d %d\n", i+1, cnt(sa), cnt(sb));
	}
	return 0;
}

