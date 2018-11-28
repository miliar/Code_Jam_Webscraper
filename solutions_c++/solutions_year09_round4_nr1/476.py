#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cassert>

using namespace std;

#define Eo(x) { cerr << #x << " = " << (x) << endl; }

typedef long long int64;
typedef double real;

static const int inf = 0x3f3f3f3f;
static const real eps = 1e-6;

const int maxn = 64;

char a[maxn][maxn];
int b[maxn];

int main(){
	int T; cin >> T;
	for (int _ = 0; _ < T; _++){
		int n; cin >> n;
		for (int i = 0; i < n; i++){
			cin >> a[i];
			b[i] = 0;
			for (int j = 0; j < n; j++){
				if (a[i][j] == '1')
					b[i] = j;
			}
		}
		int cnt = 0;
		while (1){
			int firstbad = -1;
			for (int i = 0; i < n; i++){
				if (b[i] > i){
					firstbad = i;
					break;
				}
			}
			if (firstbad < 0) break;
			int good = -1;
			for (int i = firstbad + 1; i < n; i++){
				if (b[i] <= firstbad){
					good = i;
					break;
				}
			}
			assert(good >= 0);
			swap(b[good],b[good-1]);
			cnt++;
		}
		printf("Case #%d: %d\n",_+1,cnt);
	}
	return 0;
}
