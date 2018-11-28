#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <queue>
#include <assert.h>
#include <hash_map>
#define rep(x,n) for(int x=0;x<n;x++)
#define mem(a, b) memset(a, b, sizeof(a))
#define mp(x,y) make_pair(x,y)
#define getBit(code, i) (code & (1 << i))
#define setBit(code, i) (code | (1 << i))
#define resetBit(code, i) (code & ~(1 << i))
#define PI acos(-1.0)
using namespace std;
using namespace  stdext;


void gcjSolve()
{
	int n, l, h;
	cin >> n >> l >> h;
	int vals[101];
	rep(i, n) cin >> vals[i];

	int sol = INT_MAX;
	bool f = true;

	for(int i = l; i <= h; i++){
		f = true;
		rep(j, n){
			if(i % vals[j] == 0 || vals[j] % i == 0) continue;
			else{
				f = false;
				break;
			}
		}
		if(f)
		{
			sol = i;
			break;
		}
	}
	if(f)
		cout << sol << endl;
	else
		cout << "NO" << endl;
}

int main(){

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	int t;
	cin >> t;
	rep(kase, t){
		printf("Case #%d: ", kase + 1);
		gcjSolve();
	}
	return 0;
}