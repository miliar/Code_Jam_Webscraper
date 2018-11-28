#include <algorithm>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <bitset>
#include <cstring>
#include <climits>
#include <deque>
#include <utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>
#include <ctime>

using namespace std;

typedef vector<string> vstr;
typedef vector<int> vint;
typedef vector<pair<int, int> > vpair;
typedef pair<int, int> pint;
typedef vector<vector<int> > v_vint;

#define oo (int)1<<28
#define mp make_pair
#define pb push_back
#define ll long long
#define sz(v) (int)v.size()

int main() {
	freopen("out.txt", "wt", stdout);
	int n;
	scanf("%d", &n);
	int k = 0;
	while (n--) {
		k++;
		int A, B;
		scanf("%d%d", &A, &B);
		int cnt = 0;
		for (int n = A; n <= B; ++n) {
			string str;
			stringstream s;
			s << n;
			s >> str;
			for (int i = 1; i < sz(str); ++i) {
				string str1 = str.substr(i);
				str1 += str.substr(0, i);
				int x;
				stringstream s3;
				s3 << str1;
				s3 >> x;
				if (x > n && x <= B)
					cnt++;
			}
		}
		cout << "Case #" << k << ": " << cnt << endl;
	}
	return 0;
}
