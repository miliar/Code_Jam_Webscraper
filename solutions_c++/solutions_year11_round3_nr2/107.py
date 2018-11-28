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

typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;

int a[1001000], b[2000];

int main(){
	int ri, cas, i, j, k, m, n, L, N, C, x;
	long long t;
	freopen("B-large (2).in", "r", stdin);
	freopen("w.txt", "w", stdout);
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d: ", ri);
		scanf("%d%lld%d%d", &L, &t, &n, &C);
		for(i = 0; i < C; i++){
			scanf("%d", b + i);
			b[i] = b[i] << 1;
		}
		priority_queue<int> q;
		long long sum = 0, sum2 = 0;
		for(i = 0; i < n; i++){
			a[i] = b[i % C];
			if(sum >= t)
				q.push(a[i] / 2);
			else{
				q.push(0);
				sum += a[i];
				if(sum >= t)
					q.push((sum - t) / 2);
			}
			sum2 += a[i];
		}
		while(L--){
			sum2 -= q.top();
			q.pop();
		}
		printf("%lld\n", sum2);
	}
}
