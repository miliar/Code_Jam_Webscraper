#include <stdio.h>
#include <cassert>
#include <memory.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <math.h>
#include <algorithm>
#include <string>
#include <iostream>
#include <sstream>

using namespace std;

#define pb push_back
#define mp make_pair

typedef long long lint;
typedef unsigned long long ull;

const int INF = 1000000000;
const lint LINF = 1000000000000000000LL;
const double eps = 1e-8;

void prepare()
{
	freopen("input.txt", "r", stdin);
#ifndef _DEBUG
	freopen("output.txt", "w", stdout);
#endif
}

int CASE;

int n;
char tmp[10];

queue< pair<int, int> > orange, blue;
int orangePos, bluePos;

bool solve()
{
	CASE++;

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		int pos;
		scanf("%s%d", tmp, &pos);
		if (tmp[0] == 'O')
			orange.push( mp(pos, i) );
		else
			blue.push( mp(pos, i) );
	}

	orangePos = bluePos = 1;

	int time = 0;
	while (!orange.empty() || !blue.empty())
	{
		time++;

		int nextOrangePos = orangePos;
		int nextBluePos = bluePos;
		int priorOrange = INF, priorBlue = INF;
		if (!orange.empty())
		{
			nextOrangePos = orange.front().first;
			priorOrange = orange.front().second;
		}
		if (!blue.empty())
		{
			nextBluePos = blue.front().first;
			priorBlue = blue.front().second;
		}

		if (nextOrangePos < orangePos)
			orangePos--;
		else if (nextOrangePos > orangePos)
			orangePos++;
		else
		{
			if (priorOrange < priorBlue)
			{
				if (orangePos == nextOrangePos)
					orange.pop();
			}
		}

		if (nextBluePos < bluePos)
			bluePos--;
		else if (nextBluePos > bluePos)
			bluePos++;
		else
		{
			if (priorOrange > priorBlue)
			{
				if (bluePos == nextBluePos)
					blue.pop();
			}
		}
	}

	printf("Case #%d: %d\n", CASE, time);

	return false;
}

int main()
{
	prepare();
	int tn;
	CASE = 0;
	for (scanf("%d", &tn); tn; tn--)
		solve();
	return 0;
}