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
#include <cstdlib>
#include <cctype>
#include <stdio.h>
#include <cstdlib>

using namespace std;

ifstream in("1.in");
ofstream out("1.out");

const int N = 1000;

int p, q, t, x;
long long ans;
vector<int> a;
bool w[N];

int main()
{
	in >> t;
	for (int tt = 0; tt < t; tt++) {
		out << "Case #" << tt + 1 << ": ";
		in >> p >> q;
		a.clear();
		for (int i = 0; i < q; i++) {
			in >> x;
			a.push_back(x);
		}
		ans = 999999999;
		sort(a.begin(), a.end());
		do {
			memset(w, 0, sizeof(w));
			long long tek = 0;
			for (int i = 0; i < q; i++) {
				x = a[i] + 1;
				while (!w[x] && x <= p) {x++; tek++;}
				x = a[i] - 1;
				while (!w[x] && x > 0) {x--; tek++;}
				w[a[i]] = true;
			}
			ans = min(ans, tek);
		} while (next_permutation(a.begin(), a.end()));
		out << ans << endl;
	}

	return 0;
}
