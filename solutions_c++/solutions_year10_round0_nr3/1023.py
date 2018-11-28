#include<stdio.h>
#include<string.h>
typedef __int64 int64;

int64 R, K, N;
int64 a[1009], ss[1009];
int h[1009];

int64 getSub(int &s)
{
	int64 ret = a[s];
	while (ret <= K){
		s ++;
		if ( s >= N ) s = 0;
		ret += a[s];
	}
	ret -= a[s];
	return ret;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int T, cas;
	scanf("%d", &T);
	for (cas = 1; cas <= T; cas ++){
		scanf("%I64d%I64d%I64d", &R, &K, &N);
		memset(h, 0, sizeof(h));
		memset(ss, 0, sizeof(ss));
		int i, j;
		int64 sum = 0, sub = 0, tim, left;

		for (i=0;i<N;i++){
			scanf("%d", &a[i]);
			sub += a[i];
		}

		if (sub <= K){
			printf("Case #%d: %I64d\n", cas, sub * R);
			continue;
		}

		i = 1;
		int s = 0, pre;
		while (i <= R){
			pre = s;
			sub = getSub(s);
			ss[i] = sub;
			h[pre] = i++;
			sum += sub;

			if (h[s]){
				tim = (R - i + 1) / (i - h[s]);
				left = (R - i + 1) % (i - h[s]);
				sub = 0;
				for (j = h[s]; j < i; j++)
					sub += ss[j];
				sum += sub * tim;
				for (j = h[s]; j < h[s] + left; j++)
					sum += ss[j];
				i = R + 1;
			}

		}
		printf("Case #%d: %I64d\n", cas, sum);
	}
	return 0;
}
