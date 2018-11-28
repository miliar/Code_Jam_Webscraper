#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define mp make_pair
#define f first
#define s second

vector<pair<int, int> > in;
bool cmp (const pair<int, int> &a, const pair<int, int> &b) {
	if (a.f == b.f) {
		return a.s < b.s;
	}
	return a.f > b.f;
}

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int ti=0; ti<t; ti++) {
		int n;
		scanf("%d", &n);
		in.clear();
		for (int i=0; i<n; i++) {
			int tmp;
			scanf("%d", &tmp);
		}
		for (int i=0; i<n; i++) {
			int prob;
			scanf("%d", &prob);
			in.push_back(mp(prob, i));
		}
		sort(in.begin(), in.end(), cmp);
		printf("Case #%d: ", ti+1);
		for (int i=0; i<in.size(); i++) {
			printf("%d ", in[i].s);
		}
		printf("\n");
	}
	return 0;
}
	