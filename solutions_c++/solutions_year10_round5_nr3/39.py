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

pip a[1 << 10];
const int maxn = 1 << 23;
const int SHIFT = maxn/2;
int b[maxn];

vector<int> prevs;
int64 solve(){
	prevs.clear();
	int64 res = 0;
	for (int i = 0; i < maxn; i++) {
		if (!b[i]) {
			prevs.push_back(i);
		} else if (b[i] == 1) {
			
		} else {
			int last = prevs[prevs.size()-1];
			b[i]--;
			b[i+1]++;
			b[last]++;
			res += (i-last);
			if (last < i-1){
				b[last+1] = 0;
				prevs[prevs.size()-1] = last+1;
			} else {
				b[i]--;
				prevs.resize(prevs.size()-1);
			}
			i--;
		}
	}
	return res;
}

int64 stupid(){
	int64 res = 0;
	for (int i = 0; i < maxn; i++) if (b[i] > 1){
		b[i] -= 2;
		b[i-1]++;
		b[i+1]++;
		res++;
		i -= 2;
	}
	return res;
}

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		Eo(_);
		printf("Case #%d: ",_+1);
		int n; cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i].first >> a[i].second;
		}
		memset(b,0,sizeof(b));
		for (int i = 0; i < n; i++){
			int ind = a[i].first+SHIFT;
			b[ind] = a[i].second;
		}
		int64 r1 = solve();
		cout << r1 << endl;
	}
	return 0;
}

