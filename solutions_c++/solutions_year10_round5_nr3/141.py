#pragma comment (linker, "/STACK:16000000")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

#define mii map<int, int>

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	scanf("%d", &testNum);
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		int n;
		scanf("%d", &n);
		mii a;
		for (int i = 0; i < n; i++)
		{
			int p, q;
			scanf("%d%d", &p, &q);
			a[p] = q;
		}
		int moves = 0;
		while (1)
		{
			mii::iterator f = a.end();
			for (mii::iterator iter = a.begin(); iter != a.end(); iter++)
				if (iter->second > 1)
				{
					f = iter;
					break;
				}
			if (f != a.end())
			{
				a[f->first - 1]++;
				a[f->first + 1]++;
				if (f->second == 2)
					a.erase(f);
				else
					a[f->first] -= 2;
				moves++;
			}
			else
				break;
		}
		printf("Case #%d: %d\n", testCount + 1, moves);
	}
	return 0;
}