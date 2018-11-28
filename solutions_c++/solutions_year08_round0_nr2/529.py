#include <stdio.h>
#include <vector>
#include <queue>

using namespace std;

struct tstr {
	int start;
	int dest;
	int type;
	tstr(int s, int d, int t) {
		start=s; dest=d; type=t;
	}
	bool operator<(const tstr &a) {
		return start<a.start;
	}
};

vector<tstr> sced;
int NA, NB,R;

int main() {
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,T;
	int i,j;
	scanf("%d", &T);
	for (t=1; t<=T; t++) {
		sced.clear();
		scanf("%d", &R);
		scanf("%d %d", &NA, &NB);
		for (i=0; i<NA; i++) {
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			tstr t(h1*60+m1,h2*60+m2+R,0);
			sced.push_back(t);
		}
		for (i=0; i<NB; i++) {
			int h1,m1,h2,m2;
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			tstr t(h1*60+m1,h2*60+m2+R,1);
			sced.push_back(t);
		}
		sort(sced.begin(),sced.end());
		priority_queue<int> train[2];
		int ans[2]; ans[0]=0; ans[1]=0;
		for (i=0; i<sced.size(); i++) {
			int type=sced[i].type;
			if (train[type].empty() || -train[type].top()>sced[i].start) {
				ans[type]++;
			}
			else {
				train[type].pop();
			}
			train[1-type].push(-sced[i].dest);
		}
		printf("Case #%d: %d %d\n",t,ans[0],ans[1]);
	}
	return 0;
}