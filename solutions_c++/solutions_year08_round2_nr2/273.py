/*
 *  Google Code Jam 2008
 *  Round 1B - Problem B - Number Sets
 */


#include <stdio.h>
#include <vector>
#include <map>
#include <string.h>

#define INPUT_FILE	"input.txt"
#define OUTPUT_FILE	"output.txt"


using namespace std;

int T;
__int64 A, B, P, Cnt = 0;
bool Ciur[100000];
vector<__int64> Prime;
bool Flag[1001];

int Parent[1001], Rang[1001];


int Find(__int64 x)
{
	if (x != Parent[x])
		Parent[x] = Find(Parent[x]);
	return Parent[x];
}

void Join(int x, int y)
{
	if (Rang[x] > Rang[y])
		Parent[y] = x;
	else
	{
		Parent[x] = y;
		if (Rang[x] == Rang[y])
			Rang[y]++;
	}
}

void Rejoin(int x, int y)
{
	Join(Find(x), Find(y));
}


void Solve()
{
	__int64 i, j;


	for (i = A; i <= B; i++)
	{
		Flag[i] = true;
		Rang[i] = 0;
		Parent[i] = i;
	}

	for (i = 0; i < Prime.size(); i++)
	{
		if (Prime[i] < P)
			continue;

		if (Prime[i] > B)
			break;

		int p = Prime[i];

		int cnt = 0, first;
		for (j = A; j <= B; j++)
			if (j % p == 0)
			{
				if (cnt == 0)
				{
					first = j;
				} else
				{
					Rejoin(Find(j), Find(first));
				}
				cnt++;
			};
	}

	for (i = A; i <= B; i++)
		Find(i);

	Cnt = 0;
	for (i = A; i <= B; i++)
	{
		if (Flag[Parent[i]] == true)
		{
			Cnt++;
			Flag[Parent[i]] = false;
		}
	}
}

void ComputeEratos()
{
	int i, j;

	int n = 1001;

	for (i = 2; i < n; i++)
		for (j = 2; i * j < n; j++)
			Ciur[i * j] = true;


	Prime.clear();

	for (i = 2; i < n; i++)
		if (Ciur[i] == false)
			Prime.push_back(i);
}

int main()
{
	int i;

	ComputeEratos();

	freopen(INPUT_FILE, "rt", stdin);
	freopen(OUTPUT_FILE, "wt", stdout);

	scanf("%d", &T);

	for (i = 1; i <= T; i++)
	{
		scanf("%I64d %I64d %I64d", &A, &B, &P);

		Cnt = 0;
		Solve();

		printf("Case #%d: %I64d\n", i, Cnt);
	}

	fclose(stdout);
	fclose(stdin);


	return 0;
}
