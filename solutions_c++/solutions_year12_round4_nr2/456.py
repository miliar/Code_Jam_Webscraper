#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <set>
#include <iostream>

using namespace std;
typedef pair <int, int> pii;
typedef pair <long long, long long> pll;
typedef long long ll;

struct Sq
{
	int x, y, w;
	inline bool intersect(Sq &otherSq)
	{
		return (abs(x - otherSq.x) < w + otherSq.w) && (abs(y - otherSq.y) < w + otherSq.w);
	}
};


int W, H;
Sq placedSq[2000];

inline int getx(int w, int i, int s)
{
	if (i == -1)
		return 0;
	else return placedSq[i].x + s*placedSq[i].w + w;
}

inline int gety(int w, int i, int s)
{
	if (i == -1)
		return 0;
	else return placedSq[i].y + s*placedSq[i].w + w;
}

//bool check(int i, int j)
//{
//	if (placedSq[i].intersect
//}

void test(int testNo)
{
    printf("Case #%d: ", testNo+1);
    
	int n;
	scanf("%d", &n);
	int w, h;
	scanf("%d%d", &w, &h);
	W = w;
	H = h;

	int rs[2000];
	
	for (int i = 0; i < n; i++)
		scanf("%d", rs+i);

	int curX, curY, curR;
	for(int i = 0; i < n; i++)
	{
		Sq &curSq = placedSq[i];
		curR = rs[i];
		curSq.w = curR;
		bool good = false;
		for(int j = -1; j < i && !good; j++)
		{
			for (int tt = 1; tt < 6 && !good; tt++)
			{
				int s1=-1, s2=-1;
				if (tt >= 2)
					s1 = 1;
				if (tt & 1)
					s2 = 1;
				if (tt == 4)
				{
					s1 = -1;
					s2 = 1;
				}
				curX = getx(curR, j, s1);
				if (tt == 4)
					curX -= 2*curR;
				if (curX > W)
					curX = W;
				if(curX < 0)
					curX = 0;

				if(tt == 5)
				{
					s1 = 1;
					s2 = -1;
				}
				curY = gety(curR, j, s2);
				if(tt == 5)
					curY -= 2*curR;
				if (curY > H)
					curY = H;
				if (curY < 0)
					curY = 0;

				curSq.x = curX;
				curSq.y = curY;
				good = true;
				for(int l = 0; l < i && good; l++)
					good = !curSq.intersect(placedSq[l]);
				if (j == -1)
					break;
			}
		}
		if (!good)
			throw 1;
		printf("%d.0 %d.0 ", curSq.x, curSq.y);
	}

	printf("\n");
}

int main()
{
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
    int TC;
    scanf("%d", &TC);
    
    for (int i = 0; i < TC; i++)
        test(i);
    
    return 0;
}