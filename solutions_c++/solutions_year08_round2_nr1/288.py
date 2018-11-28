/*
 *  Google Code Jam 2008
 *  Round 1B - Problem A - Crop Triangles
 */


#include <stdio.h>
#include <string>
#include <vector>

#define INPUT_FILE	"input.txt"
#define OUTPUT_FILE	"output.txt"

using namespace std;

int T, N, A, B, C, D, M;
__int64 X0, Y0;
__int64 Cnt;
vector<pair<int, int> > V;
vector<pair<int, int> > S;

long Count[9];

void back(int lev)
{
	int i;

	if (lev == 3)
	{
		int s1 = 0, s2 = 0;

		int v[3];
		for (i = 0; i < 3; i++)
		{
			s1 += S[i].first, s2 += S[i].second;
			v[i] = S[i].first * 3 + S[i].second;
		}

		if (s1 % 3 || s2 % 3)
			return;

		__int64 cnt;
		if (v[0] == v[1] && v[0] == v[2])
		{
			cnt = ((__int64)Count[v[0]] * (__int64)(Count[v[0]] - 1) * (__int64)(Count[v[0]] - 2)) / 6;
		} else
		{
			cnt = (__int64)Count[v[0]] * (__int64)Count[v[1]] * (__int64)Count[v[2]];
		}

		Cnt += (__int64)cnt;

		//printf("\n");
	} else
	{
		int num = (lev == 0) ? 0 : (S[lev - 1].first * 3 + S[lev - 1].second);

		for (i = num; i < 9; i++)
		{
			pair<int, int> p;
			p.first = i / 3;
			p.second = i % 3;

			S.push_back(p);

			back(lev + 1);

			S.pop_back();
		}
	}
}

void Solve()
{
	int i;
	long cnt;


	Cnt = 0;
	memset(Count, 0, sizeof(Count));

	for (i = 0; i < V.size(); i++)
	{
		int num = V[i].first * 3 + V[i].second;

		Count[num]++;
	}

	back(0);
}


int main()
{
	int i, j;


	freopen(INPUT_FILE, "rt", stdin);
	freopen(OUTPUT_FILE, "wt", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		scanf("%d %d %d %d %d %I64d %I64d %d ", &N, &A, &B, &C, &D, &X0, &Y0, &M);

		V.clear();

		pair<__int64, __int64> p;

		p.first = X0 % 3;
		p.second = Y0 % 3;
		V.push_back(p);

		for (j = 1; j <= N - 1; j++)
		{
			X0 = ((__int64)A * X0 + B) % M;
			Y0 = ((__int64)C * Y0 + D) % M;

			p.first = X0 % 3;
			p.second = Y0 % 3;
			V.push_back(p);
		}

		Solve();

		printf("Case #%d: %I64d\n", i, Cnt);
	}

	fclose(stdout);
	fclose(stdin);


	return 0;
}
