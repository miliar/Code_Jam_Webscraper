#include <iostream>
#include <cstdio>
#include <fstream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <map>

using namespace std;

const int MaxN = 1005;

struct R
{
	int x0, y0, x1, y1;
};

struct G
{
	int x, y;
};


int N;
int runs;
R rect[MaxN];
G group[MaxN];
int pre[MaxN];

bool intersect(int i, int j)
{
	if (rect[i].x0 > rect[j].x1+1 || rect[i].x1+1 < rect[j].x0 || rect[i].y0 > rect[j].y1+1 || rect[i].y1+1 < rect[j].y0)
		return false;
	return true;
}

int getroot(int x)
{
	if (pre[x] == x) return x;
	pre[x] = getroot(pre[x]);
	return pre[x];
}

void merge(int x, int y)
{
	pre[getroot(x)] = getroot(y);
}

int main()
{
	freopen("c-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);
	cin >> runs;
	for (int run = 1; run <= runs; ++run)
	{
		cin >> N;
		for (int i = 0; i < N; ++i)
		{
			pre[i] = i;
			group[i].x = group[i].y = -1;

			cin >> rect[i].x0 >> rect[i].y0 >> rect[i].x1 >> rect[i].y1;
			if (rect[i].x0 > rect[i].x1)
				swap(rect[i].x0, rect[i].x1);
			if (rect[i].y0 > rect[i].y1)
				swap(rect[i].y0, rect[i].y1);
		}
		//if (run != 5) continue;
	        //for (int i = 0; i < N; ++i)
		//	cout << rect[i].x0 << " " << rect[i].y0 << " " << rect[i].x1 << " " << rect[i].y1 << endl;

		for (int i = 0; i < N; ++i)
			for (int j = 0; j < N; ++j)
				if (getroot(i) != getroot(j) && intersect(i, j))
				{
					merge(i, j);
					//cout << i << " " << j << endl;
				}
		for (int i = 0; i < N; ++i)
		{
			if (rect[i].x1 > group[getroot(i)].x)
				group[getroot(i)].x = rect[i].x1;
			if (rect[i].y1 > group[getroot(i)].y)
				group[getroot(i)].y = rect[i].y1;
		}

		int max = -1;
		for (int i = 0; i < N; ++i)
		{
			//cout << i << " " << getroot(i) << endl;
			int tmp = abs(rect[i].x0 - group[getroot(i)].x) + abs(rect[i].y0 - group[getroot(i)].y);
		       	if (tmp > max) max = tmp;	
		}
		cout << "Case #" << run << ": " << max+1 << endl;
	}
}
