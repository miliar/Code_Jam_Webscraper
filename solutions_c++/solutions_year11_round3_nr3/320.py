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

int n;
long long h[10010];
set<long long> sll;
long long L, H;

int read(){
	cin >> n >> L >> H;
	sll.clear();
	for(int i = 0; i < n; i++){
		cin >> h[i];
		sll.insert(h[i]);
	}
	return 1;
}

long long gcd(long long a, long long b){ return a == 0 ? b : gcd(b%a, a); }

long long lcm(long long a, long long b){ return (a/gcd(a,b))*b; }
void process(){
	long long amigao = 1;
	for(int i = 0; i < n; i++){
		amigao = lcm(amigao, h[i]);
	}
	sort(h, h+n);
	for(long long i = L; i <= H; i++){
		int ok = 1;
		int j;
		for(j = 0; h[j] < i && j < n; j++){
			if(i%h[j] != 0)ok = 0;
		}
		
		if(!ok)continue;
		for(; j < n; j++){
			if(h[j]%i != 0){
				ok = 0;
			}
		}
		if(ok){
			cout << i << endl;
			return;
		}
	}
	cout << "NO" << endl;
}

// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		fprintf(stderr, "i(%d)\n", i);
		printf("Case #%d: ", i);
		process();
	}
	return 0;
}
// END CUT HERE 
