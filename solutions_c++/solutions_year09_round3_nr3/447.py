#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
int cell[100];
int P, Q;
bool prison[110];

int acc(int cut)
{
	int i = cut-1, ret = 0;
	while (i > 0 && prison[i]) {
		++ret; --i;
	}
	i = cut + 1;
	while (i <= P && prison[i]) {
		++ret; ++i;
	}
	return ret;
}

int do_sim()
{
	int i, ret = 0;
	for (i=0; i<Q; ++i) {
		prison[cell[i]] = false;
		ret += acc(cell[i]);
	}
	return ret;
}

int main()
{
	freopen("c-small.in", "r", stdin);
	freopen("c-small.out", "w", stdout);
	//ifstream fin("c-small.in");
	//ofstream fout("c-small.out");
	int test_case;
	scanf("%d", &test_case);
	for (int tt=1; tt<=test_case; ++tt) {
		int i, t;
		scanf("%d%d", &P, &Q);
		for (i=0; i<Q; ++i) {
			scanf("%d", &t);
			cell[i] = t;
		}
		int min = 100000000;
		sort(cell, cell + Q);
		do {
			memset(prison, true, sizeof prison);
			int ans = do_sim();
			if (ans < min) min = ans;
		} while (next_permutation(cell, cell + Q));
		printf("Case #%d: %d\n", tt, min);
	}
	
	return 0;
}