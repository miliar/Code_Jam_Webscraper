#include <iostream>
#include <vector>
#include <utility>
#include <string>

#define rep(i, n) for(int i=0; i<(n); i++)

using namespace std;

typedef pair<int, int> pii;

int go(vector<pii> &v) {
	int count=0;
	int resp=0;
	sort(v.begin(), v.end());
	rep(i, v.size()) {
		if(v[i].second == 1) {
			if (count == 0) resp++;
			else count--;
		} else {
			count++;
		}
	}
	return resp;
}

int main(void) {
	int N, T, NA, NB;
	int h1, m1, h2, m2;

	scanf("%d", &N);
	rep(k, N) {
		vector<pii> A, B;
		scanf("%d", &T);
		scanf("%d %d", &NA, &NB);
		rep(i, NA) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			A.push_back(pii(h1*60+m1, 1));
			B.push_back(pii(h2*60+m2+T, 0));
		}
		rep(i, NB) {
			scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
			B.push_back(pii(h1*60+m1, 1));
			A.push_back(pii(h2*60+m2+T, 0));
		}
		printf("Case #%d: %d %d\n", k+1, go(A), go(B));
	}

}
