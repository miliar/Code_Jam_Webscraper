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
long long n;

int main(void){
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d\n",&T);
	for(int _=1;_<=T;_++){
		
		int p,q,good = false;
		cin >> n >> p >> q;

		if(p == 0) good = true;

		for(int i=1;i<=n;i++)
			if( ((LL)i * p) % 100 == 0 ){
				good = true;
				break;
			}

		if(q == 100 && p != 100) good = false;
		if(q == 0 && p != 0) good = false;
					
		printf("Case #%d: ",_);
		if(good) cout << "Possible\n";else cout << "Broken\n";
	}
	return 0;
}
