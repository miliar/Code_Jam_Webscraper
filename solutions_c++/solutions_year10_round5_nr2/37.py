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

const int maxn = 1 << 20;
int a[maxn];
int b[maxn];

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		printf("Case #%d: ",_+1);
		int64 l; cin >> l;
		int n; cin >> n;
		for (int i = 0; i < n; i++) cin >> a[i];
		sort(a,a+n);
		memset(b,0x3f,sizeof(b));
		b[0] = 0;
		for (int i = 0; i < maxn; i++) if (b[i] != inf){
			for (int j = 0; j < n; j++) {
				if (i+a[j] >= maxn) break;
				b[i+a[j]] = min(b[i+a[j]],b[i]+1);
			}
		}
		int64 mn = 1e18;
		bool did = false;
		int big = a[n-1];
		for (int i = 0; i < maxn; i++) if (b[i] != inf){
			if (!((l-i)%big)){
				mn = min(mn,int64(b[i]+((l-i)/big)));
				did = true;
			}
		}
		if (!did) puts("IMPOSSIBLE");
		else printf("%lld\n",mn);
	}
	return 0;
}

