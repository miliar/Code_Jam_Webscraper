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
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;

int i, j, k, l, m;

int main() {
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("A-small-attempt0.out", "w", stdout);
	int tt, tn; cin >> tn;
	F1(tt,tn) {
  		int ans=0;
		int P, K, L;
		cin >> P >> K >> L;
		int f[L];
		int x;
		F0(i,L) {		
		     scanf("%d", &x);
		     f[i]=x;
		}
     	     	scanf("/n");
		if (L>P*K) {
			printf("Case #%d: Impossible\n", tt);	
		} else {
			vector<int> fv (f, f+L);        
			vector<int>::iterator it;
			sort (fv.begin(), fv.begin()+L); 

			int pr = 1;
			int ks = K;
			for(int i = L-1; i>=0; i--) {
				if (ks == 0) {
					ks = K; 
					pr++;
				}
				ans+=fv[i]*pr;
				ks--;		
			}
			printf("Case #%d: %d\n", tt, ans);
		}
	}
	return 0;
}
