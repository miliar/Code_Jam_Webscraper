#include <cstdio>
#include <vector>
#include <deque>
using namespace std;

vector<int> sieve(1001,0);
int A,B,P;

void dosieve() {
	sieve[1] = 1;
	for (int i=2; i<=1000; i++) {
		if (sieve[i]==0) {
			sieve[i] = i;
			for (int j = i+i; j<=1000; j += i) sieve[j] = i;
		}
	}
}

bool con(int a, int b) {
	if (sieve[a]==sieve[b]) return sieve[a]>=P;
	if (max(a,b)==1) return 1>=P;
	if (a>b) return con(a/sieve[a], b);
	else return con(a,b/sieve[b]);
}

void search(int v, vector<bool> &vis) {
	deque<int> f;
	f.push_back(v); vis[v] = true;
	//fprintf(stderr, "%d ", v);
	while (!f.empty()) {
		int v2 = f.front(); f.pop_front();
		for (int i=A; i<=B; i++) {
			//fprintf(stderr, "con(%d,%d)==%d\n", v2, i, con(v2,i));
			if (!vis[i] && con(v2,i)) {
				//fprintf(stderr, "%d ", i);
				vis[i] = true;
				f.push_back(i);
			}
		}
	}
}

int main() {
	dosieve();
	int C;
	scanf("%d", &C);
	for (int ixc=0; ixc<C; ixc++) {
		scanf("%d %d %d", &A, &B, &P);
		vector<bool> vis(1001, false);
		int result = 0;
		for (int i=A; i<=B; i++) {
			if (!vis[i]) {
				result++;
				search(i, vis);
				//fprintf(stderr, "\n");
			}
		}
		printf("Case #%d: %d\n", ixc+1, result);
	}

	return 0;
}
