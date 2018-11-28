#include <iostream>
#include <fstream>
#include <cstdio>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>

using namespace std;

int n, k;

void Load()
{
	scanf("%d%d", &n, &k);
}

int state[40];

void Solve()
{
	/*memset(state, 0, sizeof(state));
	cerr << "Test\n";
	int i, j;
	for (i = 0; i < n; i++) state[i] = 0;
	for (i = 0; i < k; i++)
	{
		for (j = 0; j < n; j++)
		{
			if (state[j] == 1) state[j] = 0;
			else break;
		}
		state[j] = 1;
		for (j = 0; j < n; j++) cerr << state[j];
		cerr << "\n";
	}
	for (i = 0; i < n; i++)
	{
		if (state[i] == 0) 
		{
			printf("OFF");
			return;
		}
	}
	printf("ON");*/
	if (((k + 1) % (1 << n)) == 0) printf("ON");
	else printf("OFF");
}

int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int nt, it;
	scanf("%d", &nt);
	for (it = 0; it < nt; it++)
	{
		printf("Case #%d: ", it + 1);
		Load();
		Solve();
		printf("\n");
	}
	return 0;
}