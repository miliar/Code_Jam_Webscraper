#include <cstdio>
#include <algorithm>
#include <vector>

using namespace std;

int N, D;
vector <int> d, l;
vector <int> max_l;

int getAns(void) {
	max_l[0] = d[0];
	for (int i = 0; i < N; i++) {
		for (int j = i + 1; j < N; j++) {
			if (max_l[i] + d[i] < d[j])
				break;
			max_l[j] = max(max_l[j], min(d[j] - d[i], l[j]));
		}
		if (max_l[i] + d[i] >= D)
			return 1;
	}	
	return 0;
}

int main(void) {
	int testnum;
	scanf("%d", &testnum);
	for (int testcase = 1; testcase <= testnum; testcase++) {
	
		int ans = 0;
		
		scanf("%d", &N);
		d.clear();
		l.clear();
		max_l.clear();
		
		for (int i = 0; i < N; i++) {
			int tmp1, tmp2;
			scanf("%d %d", &tmp1, &tmp2);
			d.push_back(tmp1);
			l.push_back(tmp2);
			max_l.push_back(0);
		}
		scanf("%d", &D);
		
		ans = getAns();
	
		printf("Case #%d: %s\n", testcase, ans != 0 ? "YES" : "NO");	
	}

	return 0;
}