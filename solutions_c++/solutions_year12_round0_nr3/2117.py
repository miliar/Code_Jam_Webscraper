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
	int N; cin >> N;
	for (int T = 1; T <= (int)N; T++) {
		int x, y, res = 0;
		cin >> x >> y;
		for (int v = x; v <= y; v++) {
			char str[15], dup[8];
			sprintf(str, "%d", v);

			strcpy(dup, str);
			strcat(str, dup);
			int len = strlen(dup);

			set<int> si;
			for (int i = 1; i < len; i++) {
				if (str[i] == '0') continue;
				char temp[8];
				strncpy(temp, str + i, len);
				int val;
				temp[len] = '\0';
				sscanf(temp, "%d", &val);
				if (val > v && val <= y && si.find(val) == si.end()) {
					res++;
					si.insert(val);
				}
			}
		}
		printf("Case #%d: %d\n", T, res);
		cerr << T << endl;
	}
		
	return 0;
}
