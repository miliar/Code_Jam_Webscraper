#include <functional> 
#include <numeric> 
#include <sstream> 
#include <iostream> 
#include <iterator> 
#include <algorithm> 
#include <utility> 

// container 
#include <vector> 
#include <string> 
#include <set> 
#include <map> 

// C-style 
#include <cmath> 
#include <cstdio> 
#include <cstdlib> 

using namespace std;

#define FOR(_I,_A,_B) for(int _I=(_A);(_I)<(_B);_I++)
#define FORE(_I,_A,_B) for(int _I=(_A);(_I)<=(_B);_I++) 
#define REP(_I,_B) for(int _I=(0);(_I)<(_B);_I++) 

typedef long long ll;
typedef long double ld;

ll x[100000], y[100000];
ll n, A, B, C, D, M;
ll N;
ll c[3][3];

int main(void) {
	freopen("A-small.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> N;
	FORE(tc, 1, N) {
		cin >> n >> A >> B >> C >> D >> x[0] >> y[0] >> M;

		int X=x[0], Y=y[0];
		for(int i=1;i<=n-1;i++) {
			X = (A*X+B)%M;
			Y = (C*Y+D)%M;
			x[i]=X;
			y[i]=Y;
		}
		memset(c, 0, sizeof(c));
		for(int i=0;i<n;i++) {
			c[x[i]%3][y[i]%3]++;
		}

#define EQ(a, b) (cx[(a)]==cx[(b)] && cy[(a)]==cy[(b)])
		int cx[3], cy[3];
		ll res=0;
		for(cx[0]=0; cx[0]<3; cx[0]++) for(cy[0]=0; cy[0]<3; cy[0]++)
			for(cx[1]=0; cx[1]<3; cx[1]++) for(cy[1]=0; cy[1]<3; cy[1]++)
				for(cx[2]=0; cx[2]<3; cx[2]++) for(cy[2]=0; cy[2]<3; cy[2]++)  if((cx[0]+cx[1]+cx[2])%3==0 && (cy[0]+cy[1]+cy[2])%3==0) {
					if(EQ(0, 1) && EQ(1,2)) 
						res+= c[cx[0]][cy[0]]*(c[cx[1]][cy[1]]-1)*(c[cx[2]][cy[2]]-2);
					else if(!EQ(0, 1) && !EQ(1,2) && !EQ(2,1)) 
						res+=(c[cx[0]][cy[0]]*c[cx[1]][cy[1]]*c[cx[2]][cy[2]]);
					else if(EQ(0, 1)) {
						res+=(c[cx[0]][cy[0]]*(c[cx[1]][cy[1]]-1)*c[cx[2]][cy[2]]);
					}
					else if(EQ(1, 2)) {
						res+=(c[cx[0]][cy[0]]*c[cx[1]][cy[1]]*(c[cx[2]][cy[2]]-1));
					}
					else if(EQ(2, 0)) {
						res+=((c[cx[0]][cy[0]]-1)*c[cx[1]][cy[1]]*c[cx[2]][cy[2]]);
					}
				}
		printf("Case #%d: %lld\n", tc, res/6LL);
	}
}