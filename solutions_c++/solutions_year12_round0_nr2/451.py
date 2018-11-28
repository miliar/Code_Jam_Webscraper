#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <stdlib.h>
#include <stdio.h>
#include <numeric>
#include <string.h>
#include <cassert>

#ifdef _DEBUG
#define typeof(X) std::identity<decltype(X)>::type //C++0x (for vs2010)
#else
#define typeof(X) __typeof__(X) // for gcc
#endif

#define sz(a)  int((a).size())
#define FOREACH(it, c) for (typeof((c).begin()) it=(c).begin(); it != (c).end(); ++it)
#define FOR(i,count) for (int i = 0; i < count; i++)
#define V_CIN(v) do{for(int i = 0; i < sz(v); i++) cin >> v[i];}while(0)
#define all(c) (c).begin(),(c).end()

using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
const int MODULO = 1000000007;

//BEGIN!!!

int T,N,S,p;
int t[100];

int main(){
	cin >> T;
	FOR(i,T){
		cin >> N >> S >> p;
		FOR(j,N) cin >> t[j];
		int ans = 0;
		FOR(j,N){
			int h = t[j] / 3 + (t[j] % 3 == 0 ? 0 : 1);
			if(h >= p){ ans++; continue;}
			if(t[j] <= 1 || t[j] >= 28) continue;
			if(h == p-1 && S > 0 && t[j] % 3 != 1){
				S--;
				ans++;
				continue;
			}
		}

		printf("Case #%d: %d\n",i+1,ans);
	}
	return 0;
}