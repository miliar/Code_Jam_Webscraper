#include<stdio.h>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;

int price[20][2000];
int p;
int sat[2000];

int ptree[20][20][2000];
int ptreemaxsat[20][20][2000];

int solve()
{
	int i, j, k;
	int round;


	round = 0;
	for (i = 0; i < p; i ++) {
		for (j = 0; j < (1<<(p-i-1)); j ++) {
			ptree[round][i][j] = 0;
			ptreemaxsat[round][i][j] = 0;
		}
	}

	for (round = 1; round <= p; round ++) {
		for (i = 0; i < p; i ++) {
			for (j = 0; j < (1<<(p-i-1)); j ++) {
				if (i == 0) {
					if (sat[j*2] - (p - round) > 0 || sat[j*2+1] - (p - round) > 0) {
						ptree[round][i][j] = price[i][j];

					}
					else {
						ptree[round][i][j] = 0;
					}

					ptreemaxsat[round][i][j] = max(sat[j*2] - (p - round), sat[j*2+1] - (p - round));
				}
				else {
					ptreemaxsat[round][i][j] = max(ptreemaxsat[round][i-1][j*2], ptreemaxsat[round][i-1][j*2+1]);

					if (ptreemaxsat[round][i-1][j*2] <= i && ptreemaxsat[round][i-1][j*2+1] <= i) {
						ptree[round][i][j] = min(price[i][j] + ptree[round-1][i-1][j*2] + ptree[round-1][i-1][j*2+1], ptree[round][i-1][j*2] + ptree[round][i-1][j*2+1]);
					}
					else {
						ptree[round][i][j] = price[i][j];
						if (ptreemaxsat[round][i-1][j*2] <= i + 1) {
							ptree[round][i][j] += ptree[round-1][i-1][j*2];
						}
						else {
							ptree[round][i][j] += ptree[round][i-1][j*2];
						}

						if (ptreemaxsat[round][i-1][j*2+1] <= i + 1) {
							ptree[round][i][j] += ptree[round-1][i-1][j*2+1];
						}
						else {
							ptree[round][i][j] += ptree[round][i-1][j*2+1];
						}
					}

				}
				//printf("round %d, i %d, j %d, ptreemaxsat %d, ptree %d\n", round, i, j, ptreemaxsat[round][i][j], ptree[round][i][j]);
			}
		}
	}

	return ptree[p][p-1][0];
}


int main()
{
	int i, j, k;
	int t, nowt;

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;

		scanf("%d", &p);

		for (i = 0; i < (1<<p); i ++) {
			scanf("%d", &sat[i]);
			sat[i] = p - sat[i];
		}
		for (i = 0; i < p; i ++) {
			for (j = 0; j < (1<<(p - i - 1)); j ++) {
				scanf("%d", &price[i][j]);
			}
		}

		printf("Case #%d: %d\n", nowt, solve());
	}

	return 0;
}
