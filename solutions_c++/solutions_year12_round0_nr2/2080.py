#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <climits>
//#define NDEBUG
#include <cassert>
using namespace std;
#define memsetz(NAME) memset(NAME, 0, sizeof(NAME))
typedef long long i64;

int main()
{
	int n; cin >> n;
	for (int T = 1; T <= n; T++) {
		printf("Case #%d: ", T);
		int N, S, P, x;
		int res = 0, yes_num = 0;
		cin >> N >> S >> P;
		for (int i = 0; i < (int)N; i++) {
			cin >> x;
			int r = x % 3;
			int avg = x / 3;
			if (x / 3 >= P) {
				res++;
				continue;
			}
			if (r == 0) {
				if (x > 0 && avg + 1 >= P)
					yes_num++;
			} else if (r == 1) {
				if (avg + 1 >= P)
					res++;
			} else  {
				if (avg + 1 >= P)
					res++;
				else if (avg + 2 >= P) 
					yes_num++;
			}
		}
		cout << res + min(yes_num, S) << endl;
	}
	return 0;
}
