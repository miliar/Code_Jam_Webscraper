#include <numeric>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <vector>
#include <map>
#include <cmath>
#include <iomanip>
#include <string>
#include <cctype>
#include <stdio.h>
#include <cstdlib>
#include <memory.h>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

int t, n, ans, k;
int w[100];

bool prov(int x) {
	while (x != 1 && w[x] != 0) x = w[x];

	return (x == 1);
}

void rec(int x) {
	if (x == n) {
		w[x] = k;
		if (prov(n)) ans = (ans + 1) % 100003;
		return;
	}
	else {
		w[x] = k;
		k++;
		rec(x + 1);
		k--;
		w[x] = 0;
		rec(x + 1);
	}
}

int main()            
{
	in >> t;
	for (int tt = 0; tt < t; ++tt) {
		in >> n;
		memset(w, 0, sizeof(w));
		ans = 0;
		k = 1;
		rec(2);
		out << "Case #" << tt + 1 << ": " << ans << endl;
	}

	return 0;
}
