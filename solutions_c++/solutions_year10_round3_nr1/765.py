#include <cstdio>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <list>
#include <ctype.h>
#include <string.h>
#include <math.h>
#include <algorithm>
using namespace std;

struct pt 
{
	int x, y;
};
 
struct seg
{
	pt a,  b;
};
int square (pt a, pt b, pt c) 
{
	return a.x * (b.y - c.y) + b.x * (c.y - a.y) + c.x * (a.y - b.y);
}
 
bool intersect_1 (int a, int b, int c, int d) 
{
	return max (a, b) >= min (c, d) && max (c, d) >= min (a, b);
}
 
bool intersect (pt a, pt b, pt c, pt d) {
	int s11 = square (a, b, c);
	int s12 = square (a, b, d);
	int s21 = square (c, d, a);
	int s22 = square (c, d, b);
	if (s11 == 0 && s12 == 0 && s21 == 0 && s22 == 0)
		return intersect_1 (a.x, b.x, c.x, d.x)
			&& intersect_1 (a.y, b.y, c.y, d.y);
	else
		return (s11 * s12 <= 0) && (s21 * s22 <= 0);
}

int main()
{
	int t;
	freopen("test.in", "a+", stdin);
	freopen("test.out", "w", stdout);
	cin >> t;
	int n;
	for (int k = 0; k < t; ++k)
	{
		cout << "Case #" << k+1 << ": ";
		cin >> n;
		int y1, y2;
		pt a, b;
		seg s;
		vector <seg> segment;
		for (int i = 0; i < n; ++i)
		{
			cin >> y1 >> y2;
			a.x = 0;
			a.y = y1;
			b.x = 5;
			b.y = y2;
			s.a = a;
			s.b = b;
			segment.push_back(s);
		}

		int cnt = 0;
		for (int i = 0; i < n-1; ++i)
		{
			for (int j = i +1 ; j < n; ++j)
			{
				if (intersect(segment[i].a, segment[i].b, segment[j].a, segment[j].b))
					++cnt;
			}
		}
		cout << cnt << endl;
	}
	return 0;
}