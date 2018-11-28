#include <cstdio>

using namespace std;

static inline int abs(int x) {
	return x >= 0 ? x : -x;
}

int main(int argc, char **argv) {

	int n,t;
	int p;
	int sol;
	int curo,curb;
	int time;
	char last,c;
	int tmp;

	scanf("%d",&t);
	for (int i=0; i<t; ++i) {
		curo = curb = 1;
		sol = 0;
		time = last = 0;

		scanf("%d",&n);
		for (int j=0; j<n; ++j) {
			scanf(" %c %d",&c,&p);
			if (c=='O') {
				tmp = abs(p-curo)+1;
				curo = p;
			}
			else {
				tmp = abs(p-curb)+1;
				curb = p;
			}
			if (last != c) {
				tmp = (tmp > time ? tmp-time : 1);
				time = tmp;
			}
			else
				time += tmp;

			sol += tmp;
			last = c;
		}
		printf("Case #%d: %d\n",i+1,sol);
	}


	return 0;
}

