#include <stdio.h>

#define N 3
#define LEN_MAX  (1 << N)
int T, A, B;
double P[N];

void gen(double p[], int w_pos[], int &idx, int pos, double cur_p, double wpos)
{
	float tmp = 0;
	if(pos == A)
	{
		p[idx] = cur_p;
//		if(p[idx] < 0.000000001) w_pos[idx] = A;
		w_pos[idx] = wpos;
		idx++;
		return;
	}
	tmp = cur_p * P[pos];
	gen(p, w_pos, idx, pos + 1, tmp, wpos);
	tmp = cur_p * (1 - P[pos]);
	if(wpos > pos) wpos = pos;
	gen(p, w_pos, idx, pos + 1, tmp, wpos);
}

void solve(int t)
{
	int LEN = 1 << A;
	double p[LEN_MAX];
	int w_pos[LEN_MAX];
	int idx = 0;
	for(idx = 0; idx < LEN_MAX; idx++)
	{
		p[idx] = 1;
		w_pos[idx] = A;
	}
	idx = 0;
	gen(p, w_pos, idx, 0, 1, A);
	double cnt_min = 999999999;
	double cnt = 0;
	// k backspace
	int k = 0;
	for(k = 0; k <= A; k++)
	{
		cnt = 0;
		for(idx = 0; idx < LEN; idx++)
		{
			if((A - k) > w_pos[idx])
				cnt += p[idx] * (B * 2 - A + k * 2 + 2);
			else
				cnt += p[idx] * (B - A + k * 2 + 1);
		}
		if(cnt < cnt_min) cnt_min = cnt;
	}
	cnt = 0;
	for(idx = 0; idx < LEN; idx++)
	{
		cnt += p[idx] * (B + 2);
	}
	if(cnt < cnt_min) cnt_min = cnt;
	printf("Case #%d: %.6lf\n", t, cnt_min);
}


int main()
{
	int i, j;
	scanf("%d", &T);
	for(i = 0; i < T; i++)
	{
		scanf("%d %d", &A, &B);
		for(j = 0; j < A; j++)
			scanf("%lf", &P[j]);
		solve(i + 1);
	}

	return 0;
}