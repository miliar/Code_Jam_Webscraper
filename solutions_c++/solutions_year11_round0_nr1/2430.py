#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
#include <algorithm>

using namespace std;


int sign(int a)
{
	return a > 0 ? 1 : a < 0 ? -1 : 0;
}

int main()
{
	freopen("out.txt", "w", stdout);
	int N, T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		scanf("%d", &N);
		vector<pair<int, int> > orange, blue;
		for (int i = 0; i < N; i++)
		{
			char s[10];
			int a;
			scanf("%s%d", s, &a);
			a--;
			if (s[0] == 'O')
				orange.push_back(make_pair(a, i));
			else
				blue.push_back(make_pair(a, i));
		}
		int bIndex = 0, oIndex = 0;
		int oPos = 0;
		int bPos = 0;
		int res = 0;
		while (bIndex < blue.size() && oIndex < orange.size())
		{
			if (blue[bIndex].second < orange[oIndex].second)
			{
				int time = abs(blue[bIndex].first - bPos) + 1;
				bPos = blue[bIndex].first;
				int t2 = abs(orange[oIndex].first - oPos);
				if (t2 <= time)
					oPos = orange[oIndex].first;
				else
					oPos += sign(orange[oIndex].first - oPos) * time;
				bIndex++;
				res += time;
			}
			else
			{
				int time = abs(orange[oIndex].first - oPos) + 1;
				oPos = orange[oIndex].first;
				int t2 = abs(blue[bIndex].first - bPos);
				if (t2 <= time)
					bPos = blue[bIndex].first;
				else
					bPos += sign(blue[bIndex].first - bPos) * time;
				oIndex++;
				res += time;
			}
		}
		while (bIndex < blue.size())
		{
			int time = abs(blue[bIndex].first - bPos) + 1;
			bPos = blue[bIndex].first;
			res += time;
			bIndex++;
		}
		while (oIndex < orange.size())
		{
			int time = abs(orange[oIndex].first - oPos) + 1;
			oPos = orange[oIndex].first;
			res += time;
			oIndex++;
		}
		printf("Case #%d: %d\n", t+1, res);
	}
	return 0;
}