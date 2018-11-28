#include <cstdio>
#include <cstring>

int N, M;
int queries[1200];
int mem[200][1200];
char eng[200][256];
char buf[256];
#define INF 1000000000
int F(int cureng, int query)
{
	int &r = mem[cureng][query];
	if (r != -1) return r;
	r = INF;
	for (int pos=query; pos<M; pos++)
	{
		if (queries[pos] != cureng) continue;

		for (int t=0; t<N; ++t)
			if (cureng != t)
			{
				int tmp = 1+F(t, pos);
				if (tmp < r)
					r = tmp;
			}
		break;
	}
	if (r == INF) return r = 0; else return r;
}
int main()
{
	int Q;
	scanf("%d\n", &Q);
	for (int q=0; q<Q; ++q)
	{
		gets(buf); sscanf(buf, "%d", &N);
		for (int i=0; i<N; ++i)
			gets(eng[i]);
		gets(buf);
		sscanf(buf, "%d", &M);
		for (int i=0; i<M; ++i)
		{
			gets(buf);
			for (int j=0; j<N; ++j)
				if (strcmp(buf, eng[j]) == 0)
				{
					queries[i] = j;
					break;
				}
		}

		for (int i=0; i<200; ++i)
			for (int j=0; j<1200; ++j)
				mem[i][j] = -1;

		int mini=INF;
		for (int i=0; i<N; ++i)
		{
			int tmp = F(i, 0);
			if (tmp < mini) mini = tmp;
		}
		printf("Case #%d: %d\n", q+1, mini);
	}
	return 0;
} 
