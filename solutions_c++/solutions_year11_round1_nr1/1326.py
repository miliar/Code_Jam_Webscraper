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

int p[] = {1, 2, 4, 5, 10, 25, 50, 100};

int main(){
	int i, j, k, m, cas, re, pd, pg, d, g, x, y, a, b;
	LL n;
	freopen("A-small-attempt0.in","r",stdin);freopen("w.txt","w",stdout);
	scanf("%d", &cas);
	for(re = 1; re <= cas; re++){
		printf("Case #%d: ", re);
		scanf("%lld%d%d", &n, &pd, &pg);
		if(pg * (100 - pd) > pd * (100 - pg)){
			b = 100 - pg;
			a = 100 - pd;
		}else{
			b = pg;
			a = pd;
		}
		if(b == 0 && a > 0){
			puts("Broken");
			continue;
		}
		//printf("%d %d\n", a, b);
		for(i = 0; i < 8; i++)
			if((a * p[i]) % 100 == 0)
				break;
		if(p[i] > n){
			puts("Broken");
			continue;
		}
		puts("Possible");
	}
} 
