#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <list>
#include <bitset>
#include <queue>
#include <stack>
#include <cmath>
#include <valarray>
#include <ctime>
#include <set>
#include <sstream>

using namespace std;

typedef pair<int, int> PII;
typedef unsigned long long ULL;

int ans[26] = {0, 0, 1, 2, 3, 5, 8, 14, 24, 43, 77, 140, 256, 472, 874, 1628, 3045, 5719, 10780, 20388, 38674, 73562, 140268, 268066, 513350, 984911};

const int mod = 100003;

void brute(int tstNum){
	int n = tstNum;
	int res = 0;
	for (int i = 1; i < (1 << (n - 2)); i++){
		vector<int> s;
		for (int j = 0; j < n - 2; j++){
			if ((i >> j) & 1){
				s.push_back(j + 2);
			}
		}
		s.push_back(n);
		int curr = s.size();
		int cnt = 1;
		while (curr != 1 && binary_search(s.begin(), s.end(), curr)){
			curr = lower_bound(s.begin(), s.end(), curr) - s.begin() + 1;
			++cnt;
		}

		if (curr == 1){
			++res;
			//for (int i = 0; i < s.size(); i++){
			//	printf("%d ", s[i]);
			//}
			//printf("\n");
		}
	}
	printf("%d, ", res + 1);
}

void solution(int tstNum){
	int n;
	scanf("%d", &n);
	printf("Case #%d: %d\n", tstNum + 1, ans[n] % mod);
}

int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	//freopen("A-large.in", "rt", stdin);
	//freopen("A-large.out", "wt", stdout);

	//freopen("B-small.in", "rt", stdin);
	//freopen("B-small.out", "wt", stdout);

	//freopen("B-large.in", "rt", stdin);
	//freopen("B-large.out", "wt", stdout);


	freopen("C-small.in", "rt", stdin);
	freopen("C-small.out", "wt", stdout);

	//freopen("C-large.in", "rt", stdin);
	//freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}


	return 0;
}