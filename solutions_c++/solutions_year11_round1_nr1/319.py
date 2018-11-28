#include <stdio.h>
#include <algorithm>
#include <memory.h>
#include <queue>
#include <math.h>
#include <vector>
#include <map>
#include <stack>
#include <string.h>
#include <string>
#include <iostream>
#include <deque>
#include <stdlib.h>
#include <stack>
using namespace std;
typedef long long ll;
int _T;

ll gcd(ll x, ll y) {
	while (x && y)
		if (x > y) x %= y;
		else y %= x;
	return x+y;
}

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	
	scanf("%d",&_T);
	for (int _t=1;_t<=_T;_t++) {
		printf("Case #%d: ",_t);
		
		ll pd,pg,n;
		cin >> n >> pd >> pg;
		
		if (pd < 100 && pg == 100) {
			cout << "Broken" << endl;
			continue;
		}
		if (pd > 0 && pg == 0) {
			cout << "Broken" << endl;
			continue;
		}
		
		if (100/gcd(pd,100) > n) {
			cout << "Broken" << endl;
			continue;
		}
		
		
		
		cout << "Possible" << endl;
	}
	
	return 0;
}
