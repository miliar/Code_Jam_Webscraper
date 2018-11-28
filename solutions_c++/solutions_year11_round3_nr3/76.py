#include <cstdio>
#include <vector>

using namespace std;

int N, L, H;

void solve() {
	scanf("%d%d%d", &N, &L, &H);

	vector<int> notes;
	for(int i = 0; i < N; ++i) {
		int inp;
		scanf("%d", &inp);
		notes.push_back(inp);
	}

	for(int i = L; i <= H; ++i) {
		bool flag = true;
		for(int j = 0; j < notes.size(); ++j) {
			if (notes[j] % i != 0 && i % notes[j] != 0) {
				flag = false;
				break;
			}
		}

		if (flag) {
			printf("%d\n", i);
			return;
		}
	}
	printf("NO\n");
}

int main() {
	freopen("C:\\Users\\kiheon\\Downloads\\C-small-attempt0.in", "r", stdin);
	freopen("C:\\workspace\\GCJ\\output.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		solve();
	}

	return 0;
}
