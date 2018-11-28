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

int Cs[1001];

int dist (int n1, int C) {
    return Cs[n1%C];
}

int boost (ll T, ll t, ll d) {
    if (T > t) return d;
    if (T+2*d < t) return 2*d;
    return ((t-T) + (d-(t-T)/2));
}

int main (void) {
    int T = 0;
    cin >> T;

    for (int c = 1; c<=T; ++c) {
	ll L, t, N, C;
	cin >> L >> t >> N >> C;
	for (int i = 0; i<C; ++i)
	    cin >> Cs[i];
	
	ll space[1001][1001];
	for (int i = 0; i<C; ++i) {
	    for (int j = 0; j<=L; ++j) {
		space[i][j] = 1e12;
	    }
	}
	for (int l = 0; l<=L; ++l) 
	    space[0][l] = 0;

	for (int i = 1; i<=N; ++i) {
	    for (int l = 0; l<=i and l<=L; ++l) {
		space[i][l] = space[i-1][l] + 2*dist(i-1,C);
		if (l > 0) {
		    int boosted = space[i-1][l-1] + boost(space[i-1][l-1],t,
						      dist(i-1,C));
		    if (boosted < space[i][l]) space[i][l] = boosted;
		}
	    }
	}
/*
	for (int i = 1; i<=N; ++i) {
	    cout<<"Star "<<i<<", d(i-1,i)="<<dist(i-1,C)<<":";
	    for (int l = 0; l<=i and l<=L; ++l) {
		cout<<" "<<space[i][l];
	    }
	    cout<<endl;
	}
*/
	printf("Case #%d: %Ld\n",c,space[N][L]);
    }

    return 0;
}
