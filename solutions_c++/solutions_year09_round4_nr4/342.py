#include<cstdio>
#include<climits>
#include<cstring>
#include<cstdlib>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<sstream>
#include<cassert>
#include<complex>

#define FOR(a , b , c) for(int a = (int)b; a<=(int)c; a++)
#define FORD(a , b , c) for(int a = (int)b; a>=(int)c; a--)
#define pb push_back
#define mk make_pair
#define sz(v) ((int)(v).size())
#define all(v) v.begin() , v.end()
#define set(x, with) memset(x , with , sizeof(x))
#define same(a,b) (fabs((a)-(b))<0.000000001)
#define even(a) ((a) % 2 == 0)
#define odd(a) ((a) % 2 == 1)

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef pair<int , int> ii;

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

void init(void);
void process(void);
void out(void);

const int Maxn = 3;
int group[Maxn + 1];
double X[Maxn + 1];
double Y[Maxn + 1];
double R[Maxn + 1];
int N;
double ans;

int main(void){
	int T;
	cin >> T;
	FOR(i, 1, T){
		init();
		process();
		out();
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}

void init(void){
	cin >> N;
	FOR(i, 1, N){
		cin >> X[i] >> Y[i] >> R[i];
	}
}

void process(void){
	if(N == 1){
		ans = R[1];
	} else if(N == 2){
		ans = max(R[1] , R[2]);
	} else{
	double r;
	//001
	r = max(R[3] , (R[1] + R[2] + hypot(X[1] - X[2] , Y[1] - Y[2])) / 2);
	ans = r;

	//010
	r = max(R[2] , (R[1] + R[3] + hypot(X[1] - X[3] , Y[1] - Y[3])) / 2);
	ans = min(ans , r);

	//011
	r = R[1];
	r = max(R[1] , (R[2] + R[3] + hypot(X[2] - X[3] , Y[2] - Y[3])) / 2);
	ans = min(ans , r);
	}
}

void out(void){
}
