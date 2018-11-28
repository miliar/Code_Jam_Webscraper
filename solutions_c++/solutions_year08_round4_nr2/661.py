
#include <stdio.h>
#include <algorithm>

using namespace std;

int prob, nprob;
int N, M, A;
struct XY {
	int x, y, v;
} lst[3000];
int nlst;

bool cmp(const XY &a, const XY &b) {
	return a.v < b.v;
}

int main() {
//	freopen("b.in", "r", stdin);
//	freopen("b.out", "w", stdout);
	
	scanf("%d", &nprob);
	for (prob = 1; prob <= nprob; prob++) {
		scanf("%d%d%d", &N, &M, &A);
		nlst = 0;
		for (int i = 0; i <= N; i++)
			for (int j = 0; j <= M; j++)
				lst[nlst].x = i, lst[nlst].y = j, lst[nlst++].v = i * j;
				
		sort(lst, lst + nlst, cmp);
		
		int p = 0, q = 0, flag = 0;
		while (q < nlst) {
			if (lst[q].v == lst[p].v + A) {
				int x1, y1, x2, y2;
				
				if (lst[p].v == 0) {
					x1 = 0; y2 = M;
				} else {
					x1 = lst[p].x;
					y2 = lst[p].y;
				}

				x2 = lst[q].x;
				y1 = lst[q].y;				

				flag = 1;
				printf("Case #%d: 0 0 %d %d %d %d\n", prob, x1, y1, x2, y2);
				
				break;
			} else if (lst[q].v > lst[p].v + A) {
				p++;
			} else {
				q++;
			}
		}
		
		if (!flag) {
			printf("Case #%d: IMPOSSIBLE\n", prob);
		}
	}
	
	return 0;
}
