#include <iostream>
using namespace std;

int qlist[110];
int res[110][110];

int minCost(int h, int e)
{
	if(e<h) return 0;

	if(res[h][e] != -1) return res[h][e];

	int min = INT_MAX, cost, i;
	for(i=h; i<=e; i++){
		cost = (qlist[e+1]-1) - (qlist[h-1]+1);
		cost += minCost(h, i-1);
		cost += minCost(i+1, e);

		if(cost < min) min = cost;
	}

	res[h][e] = min;

	return min;
}

int main()
{
	freopen("C-large.in.txt", "r", stdin);
	freopen("C-large.out.txt", "w", stdout);

	int N, P, Q, C;
	int X, i;

	scanf("%d", &N);
	X = 0;
	while (N--) {
		memset(res, -1, sizeof(res));
		scanf("%d%d", &P, &Q);

		for(i=1; i<=Q; i++){
			scanf("%d", &qlist[i]);
		}
		qlist[0] = 0;
		qlist[Q+1] = P+1;

		///
		C = minCost(1, Q);

		printf("Case #%d: %d\n", ++X, C);
	}
	
	fclose(stdin);
	fclose(stdout);

	return 0;
}