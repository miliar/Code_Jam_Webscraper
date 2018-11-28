#include <map>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cstring>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	for (int qn = 1; qn <= T; ++qn)
	{
		printf("Case #%d: ", qn);
		int n;
		scanf("%d", &n);
		map<int, int> mmap;

		for (int i = 0; i < n; ++i)
		{
			int x, y;
			scanf("%d %d", &x, &y);
			mmap[x] = y;
		}

		int turn = 0;
		while (true)
		{
			map<int, int>::iterator it;
			bool isok = true;
			
			for (it = mmap.begin(); it != mmap.end(); ++it)
			{
				if ((*it).second > 1)
				{
					isok = false;
					mmap[(*it).first] -= 2;
					mmap[(*it).first + 1]++;
					mmap[(*it).first - 1]++;
					break;
				}
			}
			if (isok) break; else turn++;
		}
		printf("%d\n", turn);
	}
}

