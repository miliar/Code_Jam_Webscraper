#include <stdio.h>
#include <string.h>
#include <map>
using namespace std;

map<pair<int, int>, int> hs;
int ten[10];

int calcLen(int x)
{
	int ret = 1;
	while (ten[ret] <= x) ret++;
	return ret - 1;
}

int Rotate(int x, int len)
{
	int t = x % 10;
	return t * ten[len] + x / 10;
}

void Solve()
{
	int a, b, i, t, len, cnt = 0;
	hs.clear();
	scanf("%d%d", &a, &b);
	len = calcLen(a);
	for (i = a; i <= b; i++)
	{
		//printf("i = %d\n", i);
		t = i;
		do {
			t = Rotate(t, len);
			//printf("t = %d\n", t);
			if (t == i)
				break;
			if (t <= b && t > a && t > i 
				&& hs.find(make_pair(i, t)) == hs.end())
			{
				//printf("%d %d\n", i, t);
				cnt++;
				hs[make_pair(i, t)] = 1;
			}
		} while (t != i);
	}
	printf("%d\n", cnt);
}

int main()
{
	int cas;
	for (cas = 2, ten[1] = 1; cas < 10; cas++)
		ten[cas] = ten[cas - 1] * 10;
	scanf("%d", &cas);
	for (int i = 1; i <= cas; i++)
	{
		printf("Case #%d: ", i);
		Solve();
	}
	return 0;
}
