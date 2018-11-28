#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
int solve()
{
	int N;
	scanf ("%d ", &N);
	vector<int> O, B;
	vector<int> posl;
	char c;
	int pos;
	for (int i = 0; i < N; ++i)
	{
		scanf ("%c %d ", &c, &pos);
		if (c == 'O')
		{
			O.push_back(pos);
			posl.push_back(0);
		}
		else
		{
			B.push_back(pos);
			posl.push_back(1);
		}
	}
	O.push_back(0);
	B.push_back(0);
	int ans = 0;
	int curO = 0, curB = 0;
	int posO = 1, posB = 1;
	int time;
	for (int i = 0; i < N; ++i)
	{
		if (posl[i] == 0)
		{
			time = labs(posO - O[curO]) + 1;
			posO = O[curO];
			++curO;
			ans += time;
			if (time >= labs(posB - B[curB]))
			{
				posB = B[curB];
			}
			else
			{
				if (posB > B[curB])
				{
					posB -= time;
				}
				else
				{
					posB += time;
				}
			}
		}
		else
		{
			time = labs(posB - B[curB]) + 1;
			posB = B[curB];
			++curB;
			ans += time;
			if (time >= labs(posO - O[curO]))
			{
				posO = O[curO];
			}
			else
			{
				if (posO > O[curO])
				{
					posO -= time;
				}
				else
				{
					posO += time;
				}
			}
		}
	}
	return ans;
}
int main()
{
	freopen("test.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	scanf ("%d", &T);
	for (int i = 0; i < T; ++i)
	{
		printf ("Case #%d: %d\n", i + 1,  solve());
	}
	return 0;
}