#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <functional>

#define all(v) (v).begin(), (v).end()

using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

ll gcd (ll a, ll b) {
    while (b > 0) {
        ll m = a % b;
        a = b; b = m;
    }
    return a;
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	int N;
	ll L, H;
	cin >> N >> L >> H;
	ll G = 0;
	vector<ll> vl;
	for (int i = 0; i<N; ++i) {
	    ll F;
	    cin >> F;
	    vl.push_back(F);
	    if (G == 0) {
		G = F;
	    } else {
		G = gcd(F,G);
	    }
	}
	
	bool possible = false;
	for (ll i = L; i<=H; ++i) {
	    bool good = true;
	    for (int j = 0; j<N; ++j) {
		if (!((vl[j] % i) == 0 or (i % vl[j]) == 0)) {
		    good = false; break;
		}
	    }
	    if (good) {
		printf("Case #%d: %Ld\n",c,i);
		possible = true;
		break;
	    }
	}
	if (!possible) {
	    printf("Case #%d: NO\n",c);
	}
    }

    return 0;
}
