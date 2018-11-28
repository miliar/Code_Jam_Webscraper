#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <set>
#include <math.h>
#include <map>
#include <list>
#include <queue>
#include <algorithm>
#include <fstream>
#include <cstdio>

using namespace std;

typedef vector <int> VI;
#define REP(i, n) for (int i = 0; i < (n); ++i)
#define REPV(i, a, b) for (int i = (a); i <= (b); ++i)
#define PB push_back
#define ALL(x) x.begin(),x.end()

char strin[10000];

bool prim(int a)
{
	if (a == 2) return true;
	for (int i = 2; i*i <= a; i++) 
		if (a % i == 0) return false;
	return true;
}

int test(int a, int b)
{
	int rez = -1;
	for (int i = 2; i <= min(a, b); i++)
		if (a % i == 0 && b % i == 0 && prim(i)) rez = i;
	return rez;
}

int main()
{
	freopen("B_small.txt", "rt", stdin);
	ofstream out("B_small.out");
	int T, j;
	gets(strin);
	sscanf(strin, "%d", &T);
	cout << T << endl;
	int set[10000];
	vector <int> auxBuf;
	for (j = 1; j <= T; j++) {
		auxBuf.clear();
		gets(strin);
		int rez = 1;
		int A, B, P;
		sscanf(strin, "%d %d %d", &A, &B, &P);
		for (int v = A; v <= B; v++) set[v] = v;
		for (int i = A; i <= B; i++) 
			for (int k = i+1; k <= B; k++)
				if (set[i] != set[k])
					if (test(i, k) >= P)
						for (int w = A; w <= B; w++) 
							if (set[w] == set[k])
								set[w] = set[i];
		for (int y = A; y <= B; y++) auxBuf.PB(set[y]);
		sort(ALL(auxBuf));
		for (int h = 1; h < auxBuf.size(); h++) 
			if (auxBuf[h] != auxBuf[h-1]) 
				rez++;
		out << "Case #" << j << ": " << rez << endl;
	}
	return 0;
}
