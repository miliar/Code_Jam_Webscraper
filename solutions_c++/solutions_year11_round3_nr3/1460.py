#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <math.h>
#include <map>
#include <set> 
#include <queue>
#define  rep(i,a,b) for ( long long i = a; i<=b; i++ )
const double EPS = 1E-8; 
const double PI  = 3.14159265; 
const int dx[4]={0,1,0,-1};
const int dy[4]={1,0,-1,0};

using namespace std; 

typedef  vector<int> VI; 
typedef  vector<VI>  VV; 
typedef  string      SS; 
typedef  vector<SS> VS; 
typedef  long long   LL;
typedef  map<int,int>MII;
typedef  priority_queue<int> maxpq; 
typedef  priority_queue<int,VI, greater<int>> minpq;

int T; 
LL N, L, H, F[20000]; 
LL ans; 
bool flag; 

LL UCLN(LL x, LL y) {
	if (x==y) return x;
	if (x==0) return y; 
	if (y==0) return x; 
	if (x>y) {
		return UCLN(x%y,y); 
	}
	else {
		return UCLN(y%x,x); 
	}
}
LL GCD( LL x, LL y){
	return (x/UCLN(x,y))*y; 
}

LL UC(LL x, LL y){
	LL kq; 
	kq = 1; 
	rep(i,x,y){
		kq=GCD(kq,F[i]); 
			if (kq>H) {
				return -1; 
			}
	}
	return kq; 
}

LL lamtron(LL kq) {
	if (ans == -1) return -1; 
	if (kq>=L && kq <=H) return kq; 
	if (kq<L) {
		kq = ((L-1)/kq+1)*kq; 
		if (kq<=H) return kq; 
		else return -1; 
	}
	if (kq>H) return -1; 
}

void main(){
	freopen("C-small-attempt5.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin >> T; 
	LL min=10E17; 

	rep(test_number, 1, T){
		min=10E17; 
		cin >> N >> L >> H; 
		memset(F,0,sizeof(F)); 
		rep(i,0,N-1) cin >> F[i]; 
		sort(F,F+N); 
		rep(i,L,F[0]) {
			ans = i; 
			rep(j,0,N-1){
				if (F[j]%i!=0) {
					ans = -1; 
					break; 
				}
			}
			if (ans>0) {
				min = ans; 
				flag = true; 
				break; 
			}
		}

		flag = false; 
		rep(i,0,N-1) {
			ans = UC(0,i);
			if (ans ==1 ) {
				ans = L; 
				if (ans == 1 ) ans = 2; 
				bool ok = false; 
				while (ans <= H && !ok ) {
					ok = true; 
					rep(x,i+1,N-1) {
						if (F[x]%ans!=0) ok = false; 
					}
					if (!ok) ans++; 
				}

			} else {
				ans = lamtron(ans); 
			}
			if (ans>0) {
				rep(j,i+1,N-1) {
					if (F[j]%ans!=0) {
						ans = -1; 
						break; 
					}
				}
			}
			if (ans>0) {
				if (ans<min) {
					min = ans; 
					flag = true; 
				}						
			}
		}
		if (min<10E17) {
			printf("Case #%d: ", test_number); 
			cout << min << endl; 
		}else {
			printf("Case #%d: NO\n", test_number); 
		}
	}
}