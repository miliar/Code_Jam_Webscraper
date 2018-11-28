#include <algorithm>
#include <functional>
#include <iostream>
using namespace std;

bool sortR;
struct stud
{
	int idx;
	int r;
	int x, y;
	bool operator<(const stud& rhs) const
	{
		if (sortR)
			return r > rhs.r;
		else
			return idx < rhs.idx;
	}
};
struct point
{
	int y;
	int x;
};
point points[10002];
stud s[10000];

int main()
{
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int n, w, h;
		cin >> n >> w >> h;
		for (int i = 0; i < n; ++i)
		{
			s[i].idx = i;
			cin >> s[i].r;
		}
		sortR = true;
		sort(s, s+n);

		int y = 0;
		int x = 0;
		int p = 0;
		points[0].x = 0;
		points[0].y = 0;
		for (int i = 0; i < n; ++i)
		{
			// Place at bottom left
			for (;;)
			{
				bool hasRoom;
				if (x == 0)
					hasRoom = true;
				else
					hasRoom = (x + s[i].r <= w);
				if (hasRoom)
					break;
				// Go back and up one level
				x = points[p].x;
				y = points[p].y;
				if (p == 0)
					break;
				--p;
			}
			// Check the vertical space
			int top = (y == 0 ? s[i].r : y + 2*s[i].r);
			int right = (x == 0 ? s[i].r : x + 2*s[i].r);
			// If over the top of previous limiting point, don't use that point any more
			while (p > 0 && top > points[p].y)
				--p;
			// Place the box and add a corner
			if (top > points[0].y)
				points[0].y = top;
			// Create a corner
			if (top < points[p].y)
			{
				++p;
				points[p].y = top;
				points[p].x = x;
			}
			x = right;
			// Print result
			s[i].x = (right - s[i].r);
			s[i].y = (top - s[i].r);
		}
		sortR = false;
		sort(s, s+n);
		cout << "Case #" << (t+1) << ":";
		for (int i = 0; i < n; ++i)
			cout << ' ' << s[i].x << ' ' << s[i].y;
		cout << endl;
	}
	return 0;
}
