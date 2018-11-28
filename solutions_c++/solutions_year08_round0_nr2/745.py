#include <stdio.h>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

pair<int, int> getpair()
{
	int h1, m1, h2, m2;
	scanf("%d:%d %d:%d", &h1, &m1, &h2, &m2);
	return make_pair(h1*60+m1, h2*60+m2);
}


int main(void)
{
	//freopen("b-sample.in", "rt", stdin);
	int TC;
	scanf("%d", &TC);
	for (int tc = 1; tc <= TC; tc++) {
		printf("Case #%d: ", tc);
		int t;
		int na, nb;
		pair<int, int> sa[128], sb[128];
		scanf("%d%d%d", &t, &na, &nb);
		//
		for (int i = 0; i < na; i++) {
			sa[i] = getpair();
		}
		for (int i = 0; i < nb; i++) {
			sb[i] = getpair();
		}
		sort(sa, sa + na);
		sort(sb, sb + nb);
		priority_queue<int> ea, eb;
		//
		int i = 0, j = 0;
		int needa = 0, needb = 0;
		while (i < na || j < nb) {
			if (i < na && (j == nb || sa[i] < sb[j])) {
				if (ea.empty() || -ea.top() > sa[i].first) {
					needa++;
				} else {
					ea.pop();
				}
				eb.push(-( sa[i].second + t ) );
				i++;
			} else {
				if (eb.empty() || -eb.top() > sb[j].first) {
					needb++;
				} else {
					eb.pop();
				}
				ea.push(-( sb[j].second + t ) );
				j++;
			}
		}
		printf("%d %d\n", needa, needb);
	}
	return 0;
}
