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

int a[110];

int main(){
	int cas, ri;
	int i, j, k, m, n, l, h;
	freopen("C-small-attempt0 (3).in", "r", stdin);
	freopen("w.txt", "w", stdout);
	scanf("%d", &cas);
	for(int ri = 1; ri <= cas; ri++){
		printf("Case #%d: ", ri);
		scanf("%d%d%d", &n, &l, &h);
		for(i = 0; i < n; i++)
			scanf("%d", a + i);
		for(i = l; i <= h; i++){
			for(j = 0; j < n; j++)
				if(i % a[j] != 0 && a[j] % i != 0)
					break;
			if(j >= n)
				break;
		}
		if(i > h) puts("NO");
		else printf("%d\n", i);
	}
}
