#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

long long N, pd, pg;
int read(){
	cin >> N >> pd >> pg;
	return 1;
}

int gcd(int a, int b){ return a == 0 ? b : gcd(b%a, a); }
void process(){
	if((pg == 100 && pd != pg) || (pg == 0 && pd != pg)){
		cout << "Broken" << endl;
		return;
	}
	if(N >= 100){
		cout << "Possible" << endl;
		return;
	}
	int g = gcd(100, pd);
	pd /= g;
	if(100 <= N*g){
		cout << "Possible" << endl;
	}else cout << "Broken" << endl;
}
// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 
