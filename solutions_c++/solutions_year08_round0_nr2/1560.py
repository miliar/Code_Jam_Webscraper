#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

#define MAXN 256

vector<pair<int, int> > A, B;

bool cmp1(pair<int, int> a, pair<int, int> b)
{
	return a.first < b.first;
}

bool cmp2(pair<int, int> a, pair<int, int> b)
{
	return a.second < b.second;
}

void readAndSolve()
{
	int N;

	scanf("%d", &N);
	for (int t = 0; t < N; t++)
	{
		int T;
		scanf("%d", &T);
		int NA, NB;
		scanf("%d %d", &NA, &NB);

		A.clear();
		B.clear();
		for (int i = 0; i < NA; i++)
		{
			int starth, startm, endh, endm;
			scanf("%d:%d %d:%d", &starth, &startm, &endh, &endm);
			int start = starth * 60 + startm;
			int end = endh * 60 + endm;

			A.push_back(make_pair(start, end));
		}

		for (int i = 0; i < NB; i++)
		{
			int starth, startm, endh, endm;
			scanf("%d:%d %d:%d", &starth, &startm, &endh, &endm);
			int start = starth * 60 + startm;
			int end = endh * 60 + endm;

			B.push_back(make_pair(start, end));
		}

		int resA = 0, resB = 0;

		sort(A.begin(), A.end(), cmp2);
		sort(B.begin(), B.end(), cmp1);
		int indb = -1;
		for (int i = 0; i < NA && indb + 1 < NB; i++)
		{
			while (indb + 1 < NB && A[i].second + T > B[indb + 1].first)
				resB++, indb++;
			indb++;
		}
		resB += NB - indb;
		if (indb < NB)
			resB--;

		sort(B.begin(), B.end(), cmp2);
		sort(A.begin(), A.end(), cmp1);
		int inda = -1;
		for (int i = 0; i < NB && inda + 1 < NA; i++)
		{
			while (inda + 1 < NA && B[i].second + T > A[inda + 1].first)
				resA++, inda++;
			inda++;
		}
		resA += NA - inda;
		if (inda < NA)
			resA--;

		printf("Case #%d: %d %d\n", t + 1, resA, resB);
	}
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	readAndSolve();

	return 0;
}