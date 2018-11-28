#include <stdio.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <memory.h>
#include <queue>
#include <string>
#include <string.h>
#include <cmath>
#include <utility>
#include <time.h>


typedef long long LL;
typedef unsigned long long ULL;

#define PI 3.1415926535897932384626433832795
#define sqr(x) ((x)*(x))
#define OUT_RT cerr << (float(clock()) / CLOCKS_PER_SEC) << endl

using namespace std;

int T;


int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		int sum = 0, mi = (int)2e9, hash = 0, n, x;

		cin >> 	n;
		for(int i=0;i<n;i++){
			cin >> x;
			hash ^= x;
			mi = min(x, mi);
			sum += x;
		}
		
		printf("Case #%d: ",_);
		if(hash == 0) cout << sum - mi << endl;else
				cout << "NO\n";
	}
	return 0;
}
