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

const int64 MOD = 1000000007;
int n,bas;

inline int bit(int k){
	return (1 << k);
}

string a[128];
string b[128];
char buf[1 << 10];

int64 go(int cnt, int sum, int from){
	if (sum == n){
		return 1;
	}
	int64 res = 0;
	for (int i = from; sum+i <= n; i++){
		b[cnt] = a[i];
		bool ok = true;
		for (int j = 0; ok && j < b[cnt].size(); j++){
			int was = 0;
			for (int k = 0; k <= cnt; k++) if (b[k].size() > j){
				char x = b[k][j]-'0';
				if (was&bit(x)){
					ok = false;
					break;
				}
				was |= bit(x);
			}
		}
		if (!ok) continue;
		res = (res+go(cnt+1,sum+i,i+1))%MOD;
	}
	return res;
}

int main(){
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		printf("Case #%d: ",_+1);
		cin >> n >> bas;
		for (int i = 1; i <= n; i++){
			memset(buf,0,sizeof(buf));
			int j = i;
			for (int cnt = 0;j;cnt++,j/=bas){
				buf[cnt] = '0'+(j%bas);
			}
			a[i] = buf;
		}
		int64 res = go(0,0,1);
		cout << res << endl;
	}
	return 0;
}

