#include<stdio.h>

int group[1010];
int n;
__int64 round, volume;

__int64 feesum[1010];
__int64 seq[1010];

__int64 solve()
{
	int i, j, k;
	__int64 nowp, nowround, lastp;
	__int64 nowvolume;
	__int64 totalfee;
	__int64 lastround;

	for (i = 0; i < n; i ++) {
		seq[i] = -1;
	}

	nowp = 0;
	feesum[0] = 0;
	for (nowround = 1; nowround <= round ; nowround ++) {
		if (seq[nowp] >= 0) {
			break;
		}

		seq[nowp] = nowround;
		nowvolume = 0;
		lastp = nowp;
		while (nowvolume + group[nowp] <= volume) {
			nowvolume += group[nowp];
			nowp = (nowp + 1) % n;
			if (nowp == lastp) break;
		}

		feesum[nowround] = feesum[nowround - 1] + nowvolume;
	}

	if (nowround > round) {
		return feesum[round];
	}
	else {
		lastround = seq[nowp];
		totalfee = feesum[nowround - 1] - feesum[lastround - 1];
		totalfee *= (round - nowround + 1) / (nowround - lastround) + 1;
		totalfee += feesum[lastround + (round - nowround + 1) % (nowround - lastround) - 1] - feesum[lastround - 1];
		totalfee += feesum[lastround - 1];

		return totalfee;
	}
}

int main()
{
	int i, j, k;
	int t, nowt;

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	scanf("%d", &t);
	nowt = 0;
	while (t --) {
		nowt ++;
		scanf("%I64d%I64d%d", &round, &volume, &n);
		for (i = 0; i < n; i ++) {
			scanf("%d", &group[i]);
		}

		printf("Case #%d: %I64d\n", nowt, solve());
	}

	return 0;
}



