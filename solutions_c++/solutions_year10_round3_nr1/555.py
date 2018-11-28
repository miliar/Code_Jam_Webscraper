#include <cstdio>
#include <algorithm>
#include <vector>
#define X first
#define Y second
using namespace std;

int T, N;
vector<pair<int, int> > V;

int main() {
	int a, b, cnt;
	scanf("%d", &T);
	for(int i = 0; i < T; i++) {
		V = vector<pair<int, int> >();
		scanf("%d", &N);
		for(int j = 0; j < N; j++) {
			scanf("%d%d", &a, &b);
			V.push_back(pair<int, int>(a, b));
		}
		sort(V.begin(), V.end());
		cnt = 0;
		for(int j = 0; j < V.size(); j++) {
			for(int k = j+1; k < V.size(); k++) {
				cnt += V[k].Y < V[j].Y;
			}
		}
		printf("Case #%d: %d\n", i+1, cnt);
	}
	return 0; 
}
