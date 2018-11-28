#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;

#define FOI(i, A, B) for(i=A; i<=B; i++)
#define FOD(i, A, B) for(i=A; i>=B; i--)
#define PI		acos(-1.0)
#define INF		1<<30
#define EPS		1e-9
#define sqr(x)	(x)*(x)

int64 GCD(int64 A, int64 B){
	if (B > A)
		return GCD(B, A);
	if (B == 0)
		return A;
	return GCD(B, A%B);
}

bool check(int64 F, int64 vec[], int64 N){
	int i;
	FOI(i, 0, N-1){
		if (vec[i] % F != 0 && F % vec[i] != 0)
			return false;
	}
	return true;
}

int main(){
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int T, t, i;
	cin >> T;
	FOI(t, 1, T){
		int64 N, L, H;
		cin >> N >> L >> H;
		int64 vec[N], F;
		FOI(i, 0, N-1){
			cin >> vec[i];
		}
		bool possible = false;
		FOI(F, L, H){
			if (check(F, vec, N)){
				possible = true;
				break;
			}
		}
		cout << "Case #" << t << ": ";
		if (possible)
			cout << F << endl;
		else
			cout << "NO" << endl;
	}
	return 0;
}

