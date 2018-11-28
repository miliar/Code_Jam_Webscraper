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


int main(){

	//freopen("A-small.in", "rt", stdin);
	//freopen("A-small.out", "wt", stdout);

	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);

	int t = 0;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		int k, n;
		scanf("%d%d", &n, &k);
		if ((k % (1 << n) == (1 << n) - 1)){
			printf("Case #%d: ON\n", i + 1);
		}else{
			printf("Case #%d: OFF\n", i + 1);
		}
	}



	return 0;
}