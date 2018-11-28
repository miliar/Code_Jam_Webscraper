#include <cstdio>
#include <algorithm>

using namespace std;


struct node {
	int len, w;
} list[1000000];

int CaseN, X, S, R, t, N, M;
int B[1002], E[1002], w[1002];

bool cmp(const node& A, const node& B) {
	return A.w < B.w;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	scanf("%d", &CaseN);
	for (int CaseID = 1; CaseID <= CaseN; CaseID++) {
		scanf("%d %d %d %d %d", &X, &S, &R, &t, &N);
		for (int i = 1; i <= N; i++) {
			scanf("%d %d %d", &B[i], &E[i], &w[i]);
		}
		for (int i = 1; i <= N; i++)
			for (int j = i + 1; j <= N; j++)
				if (B[i] > B[j]) {
					swap(B[i], B[j]);
					swap(E[i], E[j]);
					swap(w[i], w[j]);
				}
		int now = 0, p = 1, beforeLong = 0;
		M = 0;
		while (now < X) {
			if (p <= N && B[p] == now) {
				if (beforeLong) {
					list[M].len = beforeLong;
					list[M].w = 0;
					M++;
					beforeLong = 0;
				}
				list[M].len = E[p] - B[p];
				list[M].w = w[p];
				now = E[p];
				p++; M++;
			} else {
				beforeLong += 1;
				now++;
			}
		}
		if (beforeLong) {
			list[M].len = beforeLong;
			list[M].w = 0;
			M++;
			beforeLong = 0;
		}
		
		sort(list, list + M, cmp);
		
		p = 0;
		double tt = t, ans = 0;
		while (p < M) {
			double use = 1.0 * list[p].len / (list[p].w + R);
			if (use <= tt) {
				ans += use;
				tt -= use;
				p++;
			} else {
				ans += tt;
				double dd = tt * (list[p].w + R);
				ans += ((double)list[p].len - dd) / (list[p].w + S);
				p++;
				break;
			}
		}
		while (p < M) {
			ans += 1.0 * list[p].len / (list[p].w + S);
			p++;
		}
		printf("Case #%d: %lf\n", CaseID, ans);
	}
	
	return 0;
}
