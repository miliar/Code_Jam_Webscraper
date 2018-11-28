#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <map>

using namespace std;

const int MAXN = 1005;

int N, T;

int main() {
	cin >> T;
	for(int t = 1 ; t <= T ; t++) {
		cin >> N;
		int ans = 0;
		for(int a, i = 1 ; i <= N ; i++) {
			cin >> a;
			if (a != i) {ans++;}			
		}		
		printf("Case #%d: %d.000000000\n",t,ans);		
	}
	return 0;
}
