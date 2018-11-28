#include <cstdio>
#include <set>
using namespace std;

int main()
{
	int N;
	scanf("%d", &N);
	for (int c = 0; c < N; ++c) {
		int T, NA, NB;
		scanf("%d%d%d", &T, &NA, &NB);

		multiset<int> t1,t2,t3,t4;
		int tmp1, tmp2;
		for (int i = 0; i < NA; ++i) {
			scanf("%d:%d", &tmp1, &tmp2);
			t1.insert(tmp1 * 60 + tmp2);
			
			scanf("%d:%d", &tmp1, &tmp2);
			t2.insert(tmp1 * 60 + tmp2);
		}
		for (int i = 0; i < NB; ++i) {
			scanf("%d:%d", &tmp1, &tmp2);
			t3.insert(tmp1 * 60 + tmp2);
			
			scanf("%d:%d", &tmp1, &tmp2);
			t4.insert(tmp1 * 60 + tmp2);
		}

		int numa = 0, numb = 0;
		while (!t1.empty()) {
			if (!t4.empty() && *t4.begin() + T <= *t1.begin()) {
				t1.erase(t1.begin());
				t4.erase(t4.begin());
			} else {
				t1.erase(t1.begin());
				++numa;
			}
		}
		while (!t3.empty()) {
			if (!t2.empty() && *t2.begin() + T <= *t3.begin()) {
				t3.erase(t3.begin());
				t2.erase(t2.begin());
			} else {
				t3.erase(t3.begin());
				++numb;
			}
		}
		printf("Case #%d %d %d\n", c + 1, numa, numb);
	}
	return 0;
}

