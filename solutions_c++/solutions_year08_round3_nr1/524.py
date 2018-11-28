#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
#define dbg if (false) 

const ll MAXL = 1001;
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

ll i, j, k, m, n, l, t, ans;

ll let[MAXL], molt[MAXL];

ll swap(ll* M, ll j, ll k){
    ll a = M[j];
    M[j] = M[k];
    M[k] = a;
} 

void sortVect(ll* M, ll m) {
    for (int j = 0; j < m; j++)
        for (int k = j; k < m; k++)    
            if (M[k]>M[j]) swap(M,j,k); 
}


int main() {
	freopen("A-large.in", "r", stdin);
	//freopen("inp.txt", "r", stdin);
	freopen("A-large.out", "w", stdout);

	ll tt, tn; cin >> tn;
	F1(tt,tn) {


		ll P, K, L;
		cin >> P >> K >> L ;

		F0(i,L) cin >> let[i];
		sortVect(let, L);
		
		k = 1;
		t = 1;
		F0(i,L) {
          molt[i] = k;
          if (t>=K) t = 1, k++;
          else t++;
        }     
        
        dbg F0(i,L) cout << molt[i];
        dbg cout << endl;   
		dbg F0(i,L) cout << let[i];
		
		ans = 0;
		F0(i,L) ans+= molt[i]*let[i];
		cout << "Case #" << tt << ": " << ans<< endl;
	}
	
	return 0;
}
