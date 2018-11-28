/*
ID: ahaigh1
PROG: A
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <queue>
#include <utility>
#include <memory>
#include <set>
#include <stack>
#include <string>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <limits>
#include <map>
#include <bitset>
#include <ctime>
using namespace std;

#define REP(i, n) for(int i = 0; i < n; i++)
#define CL(x) memset(x, 0, sizeof(x))
#define eps (1e-10)
#define inf (1<<30)
#define ll long long
#define MP make_pair

int gcd(int a, int b) { return (b)?gcd(b, a % b):a; } //gcd

ll t, n, l, h, x[10001];

bool does_divide(ll a, ll b) { 
	if (a % b == 0 || b % a == 0) return true; else return false;
}

int main() {
	cin >> t;
	REP(i, t) { 
		cin >> n >> l >> h;
		REP(j, n) cin >> x[j];
		
		ll sln = -1;
		for(ll z = l; z <= h && sln == -1; z++) { 
			bool flag = true;
			for(int j = 0; j < n; j++) if (!does_divide(x[j],z)) flag = false;
			//if (flag) cout << z << endl;
			if (flag) sln = z;
		}
		
		if (sln == -1) { 
			cout << "Case #" << (i+1) << ": NO" << endl;
		} else { 
			cout << "Case #" << (i+1) << ": " << sln << endl;
		}
	}
}