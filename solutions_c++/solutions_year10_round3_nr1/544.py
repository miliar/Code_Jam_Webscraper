#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define MAX_WIRES 1024

int wires[MAX_WIRES][2];

bool wiresIntersect(int i, int j)
{
	return (wires[i][0] > wires[j][0]) ^ (wires[i][1] > wires[j][1]);
}

int main(int argc, char* argv[])
{
	int t;
	cin >> t;

	for (int cs = 1; cs <= t; cs++)
	{
		int n;
		cin >> n;

		for (int i = 0; i < n; i++)
		{
			cin >> wires[i][0];
			cin >> wires[i][1];
		}

		int intersections = 0;
		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < i; j++)
			{
				if (wiresIntersect(i, j))
					intersections++;
			}
		}

		printf("Case #%d: %d\n", cs, intersections);
	}
}

