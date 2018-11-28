#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <string>
#include <sstream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <ctime>
#include <cctype>

using namespace std;
typedef long long int64;
const int inf = 0x3f3f3f3f;
typedef double real;
const real eps = 1e-6;
typedef pair<int,int> pip;
#define Eo(x) { cerr << #x << " = " << (x) << endl; }

inline int bit(int k){
	return (1 << k);
}

int main(){
	int T; scanf("%d",&T);
	for (int _ = 0 ; _ < T; _++){
		printf("Case #%d: ",_+1);
		int n,k; cin >> n >> k;
		int m = bit(n)-1;
		bool ok = (k&m) == m;
		puts(ok ? "ON" : "OFF");
	}
	return 0;
}

