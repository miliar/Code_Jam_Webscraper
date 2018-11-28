#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

int T, n;
vector <int> a;
char s[1000];
bool issqr(long long a)
{
	return ((long long)sqrt(a + eps)) * ((long long)sqrt(a + eps)) == a;
}
int main()
{
	freopen("d.in", "r", stdin);
	freopen("d.out", "w", stdout);
	int ca = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%s", &s);
		n = strlen(s);
		long long del = 0, r = 1;
		a.clear();
		for (int i = 0; i < n; i++) {
			if (s[i] == '?')
				a.PB(i);
			else
				del += (s[i] - '0') * (1LL << (n - i - 1));
		}
		int x = a.size();
		for (int i = 0; i < (1 << x); i++) {
			long long O = 0;
			for (int j = 0; j < x; j++)
				if ((1 << j) & i)
					O += (1LL << (n - a[j] - 1));
			if (issqr(O + del)) {
				for (int j = 0; j < x; j++)
					if ((1 << j) & i)
						s[a[j]] = '1';
					else
						s[a[j]] = '0';
				break;
			}
		}
		printf("Case #%d: ", ++ca);
		puts(s);
	}
}
