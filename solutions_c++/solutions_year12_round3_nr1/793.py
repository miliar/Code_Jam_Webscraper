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

bool sign[1005];
int main()
{
	int T; cin >> T;
	for (int caseNum = 1; caseNum <= (int)T; caseNum++) {
		vector<vector <int> > vii;
		vector<int> vi;
		vii.push_back(vi);
		int n; cin >> n;
		for (int i = 0; i < (int)n; i++) {
			int num; cin >> num;
			vi.clear();
			for (int j = 0; j < (int)num; j++) {
				int temp; cin >> temp;
				vi.push_back(temp);
			}
			/**/ vii.push_back(vi);
		}

		bool find = false;
		for (int i = 1; i <= (int)n; i++) {
			memsetz(sign);
			queue<int> qi;
			qi.push(i);
			while (!qi.empty()) {
				int cur = qi.front();
				qi.pop();
				int size = vii[cur].size();
				for (int j = 0; j < (int)size; j++)
					if (sign[vii[cur][j]]) {
						find = true;
						break;
					} else  {
						sign[vii[cur][j]] = 1;
						qi.push(vii[cur][j]);
					}
				if (find) break;
			}
		}
			
		printf("Case #%d: ", caseNum);
		if (find) puts("Yes");
		else puts("No");
	}
		
	return 0;
}
