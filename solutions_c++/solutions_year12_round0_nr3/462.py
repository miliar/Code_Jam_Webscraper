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

bool t[2000000];
int l,A,B;

int calcPair(int cu)
{
	t[cu] = true;
	int count = 1;
	for(int i = 10; i <=cu; i *= 10)
	{
		if((cu / (i / 10)) % 10 == 0)
			continue;

		int a = cu / i;
		int b = (cu % i);
		int next = b * (l / i) + a;
		if(A > next || next > B || t[next]) continue;

		count++;
		t[next] = true;
	}
	return count * (count-1) / 2;
}

int main(){
	ll ans;
	int T;
	cin>>T;
	FOR(i,T){
		memset(t,0,sizeof(t));
		ans = 0;
		cin>>A>>B;
		l = 1;
		for(int j = 1; j < B; j *= 10) l *= 10;

		for(int cu = A;cu <= B;cu++){
			if(t[cu]) continue;
			ans += calcPair(cu);
		}
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
	return 0;
}