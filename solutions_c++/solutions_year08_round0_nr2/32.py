#include<stdio.h>
#include<algorithm>
using namespace std;

struct Time {
	short de, ar;
	char st;
	bool operator<(const Time &b) const { return de<b.de; }
}times[200];

int inline rdmnt() {
	int h, m;
	scanf("%d:%d", &h, &m);
	return h*60+m;
}
int timeline[1600][2];
int main() {
	int N;
	scanf("%d", &N);
	for(int cas=1;cas<=N;cas++) {
		memset(timeline, 0, sizeof(timeline));

		int NA, NB, T;
		scanf("%d%d%d", &T, &NA, &NB);
		for(int i=0;i<NA;i++) {
			times[i].de=rdmnt();
			times[i].ar=rdmnt();
			times[i].st=0;
		}
		for(int i=NA;i<NA+NB;i++) {
			times[i].de=rdmnt();
			times[i].ar=rdmnt();
			times[i].st=1;
		}

		sort(times, times+NA+NB);

		int de[2], tp=0;
		de[0]=de[1]=0;
		for(int i=0;i<1440;i++) {
			int av[2];
			av[0]=timeline[i][0], av[1]=timeline[i][1];
			for(;tp<NA+NB && times[tp].de<=i;tp++) {
				int st=times[tp].st;
				timeline[times[tp].ar+T][!st]++;

				if(av[st]>0) av[st]--;
				else de[st]++;
			}

			timeline[i+1][0]+=av[0];
			timeline[i+1][1]+=av[1];
		}
		printf("Case #%d: %d %d\n", cas, de[0], de[1]);
	}
	return 0;
}