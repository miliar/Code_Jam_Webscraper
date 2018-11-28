#include <stdio.h>
#include <memory.h>

struct interval_s
{
	int st;
	int ed;
} fromA[101], fromB[101];

int fromAN, fromBN;
int turn;

int matrix[201][201];
int vertexN;
int from[201];
int did[201];

int ansA, ansB;

int __flow(int pl)
{
	if (did[pl])
		return false;
	did[pl] = true;

	int i;
	for (i = 0;i < vertexN;i++)
	{
		if (!matrix[pl][i])
			continue;
		if (from[i] == -1)
		{
			from[i] = pl;
			return true;
		}
		if (__flow(from[i]))
		{
			from[i] = pl;
			return true;
		}
	}
	return false;
}

int flow(int pl)
{
	memset(did, 0, sizeof(did));
	return __flow(pl);
}

int read_one()
{
	int h, m;
	scanf("%d:%d", &h, &m);
	return h * 60 + m;
}

int main()
{
	int t, ti;
	int i, j;
	scanf("%d", &t);
	for (ti = 1;ti <= t;ti++)
	{
		scanf("%d %d %d", &turn, &fromAN, &fromBN);
		for (i = 0;i < fromAN;i++)
		{
			fromA[i].st = read_one();
			fromA[i].ed = read_one();
		}

		for (i = 0;i < fromBN;i++)
		{
			fromB[i].st = read_one();
			fromB[i].ed = read_one();
		}

		vertexN = fromAN + fromBN;
		memset(matrix, 0, sizeof(matrix));
		memset(from, 0xFF, sizeof(from));

		for (i = 0;i < fromAN;i++)
			for (j = 0;j < fromBN;j++)
				if (fromA[i].ed + turn <= fromB[j].st)
					matrix[fromAN + j][i] = true;

		for (i = 0;i < fromBN;i++)
			for (j = 0;j < fromAN;j++)
				if (fromB[i].ed + turn <= fromA[j].st)
					matrix[j][fromAN + i] = true;

		ansA = ansB = 0;
		for (i = 0;i < fromAN;i++)
			if (!flow(i))
				ansA++;
		for (i = 0;i < fromBN;i++)
			if (!flow(fromAN + i))
				ansB++;

		printf("Case #%d: %d %d\n", ti, ansA, ansB);
	}
	return 0;
}