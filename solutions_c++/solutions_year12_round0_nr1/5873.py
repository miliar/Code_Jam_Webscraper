#include <iostream>
#include <cstdio>
#include <cstdlib>

#include <algorithm>
#include <utility>
#include <cmath>
#include <cctype>
#include <sstream>
#include <ctime>
#include <numeric>
#include <functional>
#include <string.h>

#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <deque>
#include <bitset>
#include <string>

#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define forv(i, v) forn(i, v.size())
#define x_p first
#define y_p second
#define sqr(a) ((a) * (a))

using namespace std;


int main() {
#ifndef ONLINE_JUDGE
	freopen("bstsimple.in", "rt", stdin);
	freopen("bstsimple.out", "wt", stdout);
#endif	
	cin.sync_with_stdio(false);
	cout.sync_with_stdio(false);
	char dict[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	int n; string temp;
	cin >> n; getline(cin, temp);
	for (int i = 0; i < n; i++) {
		getline(cin, temp);
		cout << "Case #" << i + 1 << ": ";
		for (int j = 0; j < temp.size(); j++) {
			cout << (temp[j] == ' ' ? ' ' :dict[int(temp[j] - 'a')]);
		}
		cout << '\n';
	}
	return 0;
}
