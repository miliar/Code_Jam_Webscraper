#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <string>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define EPS 1e-9
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )

using namespace std;

typedef long long ll;
typedef long double ld;


int main() {
    int T; scanf("%d",&T);
    FR(i,T) {
        printf("Case #%d: ",i+1);
        int N,K;
        scanf("%d %d",&N,&K);
        if(K%( (1<<N))== ((1<<N)-1 ) ) printf("ON\n");
        else printf("OFF\n");
    }
}