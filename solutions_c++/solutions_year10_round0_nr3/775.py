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

int vals[1000];
ULL sums[1000];
int ds[1000];

void solution(int tstNum){
	memset(sums, 0, sizeof(sums));
	memset(ds, 0, sizeof(ds));
	int r, k, n;
	scanf("%d%d%d", &r, &k, &n);
	for (int i = 0; i < n; i++){		
		scanf("%d", &vals[i]);
	}

	for (int i = 0; i < n; i++){
		ULL tsum = 0;
		int j;
		for (j = 0; j < n; j++){
			int id = (i + j) % n;
			if (tsum + vals[id] > k){
				--j;
				break;
			}
			tsum += vals[id];
		}
		ds[i] = (i + j) % n;
		sums[i] = tsum;
	}
	ULL res = 0;
	int curr = 0;
	for (int i = 0; i < r; i++){
		int nxt = ds[curr];
		res += sums[curr];
		curr = (ds[curr] + 1) % n;
	}
	printf("Case #%d: %llu\n", tstNum + 1, res);
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


	//freopen("C-small.in", "rt", stdin);
	//freopen("C-small.out", "wt", stdout);

	freopen("C-large.in", "rt", stdin);
	freopen("C-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int tt = 0; tt < t; tt++){
		solution(tt);
	}

	return 0;
}