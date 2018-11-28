#include<cstdio>

int main()
{
	int Z, T;
	scanf("%d", &T);
	for(Z = 1; Z <= T; Z ++)
	{
		__int64 R, K, N;
		__int64 i, j, k, l, S[2];
		__int64 p[1001], rec[1001];
		int used[1001];
		scanf("%I64d %I64d %I64d", &R, &K, &N);
		for(i = 0; i < N; i ++)
		{
			scanf("%I64d", &p[i]);
			used[i] = -1;
		}
		j = l = 0;
		while( used[l] == -1 )
		{
			rec[j] = 0;
			used[l] = j;
			for(i = 0; i < N; i ++)
			{
				if(rec[j] > K - p[l])break;
				rec[j] += p[l];
				l = (l+1)%N;
			}
			j ++;
			//printf("%I64d %I64d\n", j, l);
		}

		S[0] = S[1] = 0;
		l = used[l];
		for(i = 0; i < j; i ++)
		{
			if(i < R && i < l+((R-l)%(j-l)))S[0] += rec[i];
			if(i >= l)S[1] += rec[i];
		}
		S[1] *= ((R-l)/(j-l));
		//printf("%I64d %I64d %I64d\n", S[0], S[1], l);
		printf("Case #%d: %I64d\n", Z, S[0]+S[1]);
	}
	return 0;
}
