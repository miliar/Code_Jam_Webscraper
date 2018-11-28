#include <iostream>
#include <cmath>
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

map<pip,char> all;

bool good(int a, int b){
	if (a > b) swap(a,b);
	if (all.count(pip(a,b))) return all[pip(a,b)];
	if (!(b%a)){
		return all[pip(a,b)] = 1;
	}
	for (int k = 1; ;k++){
		int c = a-b*k;
		if (c <= 0) break;
		if (!good(b,c)){
			return (all[pip(a,b)] = 1);
		}
	}
	for (int k = 1; ;k++){
		int c = b-a*k;
		if (c <= 0) break;
		if (!good(a,c)){
			return (all[pip(a,b)] = 1);
		}
	}
	return (all[pip(a,b)] = 0);
}

const int maxn = 1 << 20;
int start[maxn];

int main(){
	real z = sqrt(5.);
	real phi = (1+z)*0.5;
	for (int i = 1; i < maxn; i++){
		start[i] = 1+int(i*phi);
	}
	int T; cin >> T;
	for (int  _ = 0; _ < T; _++){
		int a1,a2,b1,b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int64 res = 0;
		for (int64 a = a1; a <= a2; a++){
			int64 s = start[a];
			if (b2 >= s){
				res += b2-s+1;
			}
			if (b1 > s){
				res -= b1-s;
			}
			if (start[b1] > a) continue;
			if (b1 >= a) continue;
			int64 l= b1;
			int64 r = a+10;
			for (;r-l > 1;){
				int64 m =(l+r)/2;
				if (m > b2 || m >= a) {
					r = m;
					continue;
				}
				if (start[m] <= a){
					l = m;
				} else {
					r = m;
				}
			}
			res += l-b1+1;
		}
		printf("Case #%d: %lld\n",_+1,res);
	}
	return 0;
}

