#include <cstdio>
int S;

bool check(int n, int p) {
	//check if the num can be divided in the form reqd
	int tmp = n/3;
	if(tmp < p-2) 
		return false;
	int gap = n-tmp*3;
	int req = p-tmp;
	if(req <= 0) {
		return true;

	}
	if(req == 1) {
		if(gap >= 1) {
			return true;
		} else {
			if(S && tmp) {
				S--;
				return true;
			}
		}
	} else if(req == 2) {
		if(gap == 2 && S>0) {
			S--;
			return true;
		}
	}
	return false;
}

int main() {
	int t;
	int i;
	scanf("%d", &t);
	int tp;
	int count;
	int N, p, ti;
	for(tp=1; tp<=t; ++tp) {
		count = 0;
		scanf("%d%d%d", &N, &S, &p);
		for(i=0; i<N; ++i) {
			scanf("%d", &ti);
			if(check(ti, p)) {
//				printf(">> %d\n", ti);
				count ++;
			}
		}

		printf("Case #%d: %d\n", tp, count);
	}
	return 0;
}
