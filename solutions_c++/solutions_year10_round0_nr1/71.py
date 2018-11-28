#include <iostream>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <sstream>
using namespace std;

#define sz(A) (int)(A).size()
#define vs vector<string>
#define vi vector<int>
#define ll long long
#define FOR(A,B) for(int A=0; A < (int) (B);A++)
#define pb push_back
#define pii pair<int,int>
#define inf (1<<25)
#define infL 10000000000000000LL
#define F first
#define S second
#define all(x) x.begin() , x.end()

int main() {
	int T,n,k;
	scanf("%d", &T);
	FOR(t,T) {
		printf("Case #%d: " , t+1);
		scanf("%d %d", &n, &k);
		int ok = 1;
		for(int j =0; j <= n-1; j++) {
			if(! (( 1 << j ) & k ) ) ok = 0;
		}

		if(ok) printf("ON\n");
		else printf("OFF\n");
	}

    return 0;
}

