#include <cstdio>
#include <cmath>
#include <queue>

const int MAX_C = 1010;
using namespace std;
int caseAmt;

int dist[MAX_C];
int amt[MAX_C];
priority_queue< pair<int, int> > pq;
void solve(int caseNum) {
	printf("Case #%d: ", caseNum);
	int L, T, N, C;
	scanf("%d %d %d %d", &L, &T, &N, &C);
	for(int i = 0; i < C; i++) {
		scanf("%d", &dist[i]);
	}
	int ind = 0;
	int d = 0;
	while(d < T / 2) {
		d += dist[ind % C];
		ind++;
		if(ind > N) {
			printf("%d\n", d * 2);
			return;
		}
	}
//	printf("d = %d, ind = %d", d, ind);
	if(d > T / 2) {
		pq.push(make_pair(d - (T / 2), 1));
	}
	while(ind < N) {
		amt[ind % C]++;
		ind++;
	}
	for(int i = 0; i < C; i++) {
		if(amt[i] > 0) {
			pq.push(make_pair(dist[i], amt[i]));
		}
	}

	int amtLeft = L;
	int savedTime = 0;
	if(L > 0) {
	while(true) {
		if(pq.empty()) break;
		pair<int, int> X = pq.top();
		pq.pop();
//		printf("popped %d %d\n", X.first, X.second);
		if(X.second > amtLeft) {
			savedTime += amtLeft * X.first;
			break;
		} else {
			savedTime += X.second * X.first;
			amtLeft -= X.second;
		}
	}
	}
//	printf("savedTime = %d\n", savedTime);
	while(!pq.empty()) {
//		pair<int, int> X = pq.top();
		pq.pop();
//		printf("[%d, %d], ", X.first, X.second);
	}
	int total = 0, j = 0;
	for(int i = 0; i < N; i++, j++) {
		if(j == C) j = 0;
		total += dist[j];
	}
	total = total * 2;
//	printf("totalTime = %d\n", total);
	total -= savedTime;
	printf("%d\n", total);
	for(int i = 0; i <= C; i++) dist[i] = amt[i] = 0;
	return;
}

int main() {
	freopen("small.txt", "r", stdin);
	freopen("smallout.txt", "w", stdout);
	scanf("%d", &caseAmt);
	for(int i = 1; i <= caseAmt; i++) solve(i);

//	freopen("large.txt", "r", stdin);
//	freopen("largeout.txt", "w", stdout);
//	scanf("%d", &caseAmt);
//	for(int i = 1; i <= caseAmt; i++) solve(i);
	return 0;
}
