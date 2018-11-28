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

int main()
{
	freopen("A_large.txt", "rt", stdin);
	ofstream out("A_large.out");
	int T, j;
	gets(strin);
	sscanf(strin, "%d", &T);
	cout << T << endl;
	int P, K, L, f, i, counter;
	VI freq;
	for (j = 1; j <= T; j++) {
		long long rez = 0;
		counter = 1;
		freq.clear();
		gets(strin);
		sscanf(strin, "%d %d %d", &P, &K, &L);
		gets(strin);
		istringstream in(strin);
		for (i = 0; i < L; i++) {
			in >> f;
			freq.PB(f);
		}
		sort(ALL(freq));
		reverse(ALL(freq));
		for (i = 0; i < freq.size(); i++) {
			if (i % K == 0 && i != 0) counter++;
			rez += (long long)counter * (long long)freq[i];
		}
		out << "Case #" << j << ": " << rez << endl;
	}
	return 0;
}
