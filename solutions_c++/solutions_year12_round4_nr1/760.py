#include <cstdio>
#include <memory.h>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <vector>
#include <cctype>
#define pb push_back

using namespace std;
typedef long long ll;
const int N = 1000000;
struct State{
	ll dis, len, ans;
};

ll i, t, D, n, idx;
State a[N];


void Check(){
	for (i = 0; i < n; i++)
		if (a[i].dis + a[i].ans >= D){
			printf("YES\n");
			return ;
		}
	printf("NO\n");
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%lld",&t);
	for (int testcase = 1; testcase <= t; testcase++){
		printf("Case #%d: ", testcase);
		scanf("%lld",&n);
		for (i = 0; i < n; i++){
			scanf("%lld%lld",&a[i].dis, &a[i].len);
			a[i].ans = 0;
		}
		scanf("%lld",&D);
		a[0].ans = a[0].dis;
		idx = 1;
		for (i = 0; i < n; i++){
			if (a[i].ans == 0) continue;
			while (a[i].dis + a[i].ans >= a[idx].dis && idx < n){
				a[idx].ans = min(a[idx].dis - a[i].dis, a[idx].len);
				idx ++;
			}
		}
		Check();
	}
	return 0;
}