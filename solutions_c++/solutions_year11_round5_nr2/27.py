#include <stdio.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <assert.h>
#include <math.h>
using namespace std;

#define FOREACH(it,vec) for(typeof((vec).begin()) it = (vec).begin(); it != (vec).end(); it++)
#define MOD(a,b) (((a)%(b)+(b))%(b))

const int MAX = 20000;

int T;
int N;
int anz[MAX];
int nanz[MAX];

bool geht(int r) {
	priority_queue<int> en;
	int aktiv = 0, muss = 0;
	for (int i = 0; i < MAX; i++) {
		while(!en.empty() && en.top() == -i) {
			en.pop();
			muss--;
		}
		if (aktiv < anz[i]) {
			for (int k = 0; k < anz[i]-aktiv; k++)
				en.push(-i-r);
			muss += anz[i]-aktiv;
			aktiv = anz[i];
		}
		if (anz[i] < muss)
			return false;
		if (anz[i] < aktiv) {
			aktiv = anz[i];
		}
	}
	if (muss > 0)
		return false;
	return true;
}

int main() {
	scanf("%d", &T);
	for (int test = 0; test < T; test++) {
		fprintf(stderr, "Test %d/%d\n", test+1, T);
		printf("Case #%d: ", test+1);
		scanf("%d", &N);
		for (int i = 0; i < MAX; i++)
			anz[i] = 0;
		for (int i = 0; i < N; i++) {
			int a;
			scanf("%d", &a);
			anz[a]++;
		}
		if (N == 0)
			printf("0\n");
		else {
			int s = 1, e = N+1;
			while(s < e-1) {
				int m = (s+e)/2;
				if (geht(m))
					s = m;
				else
					e = m;
			}
			printf("%d\n", s);
		}
	}
	return 0;
}
