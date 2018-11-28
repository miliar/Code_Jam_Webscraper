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

const int Maxn = 100;
int Matrix[Maxn + 1][Maxn + 1];
int Index[Maxn + 1];
int N;
int ans = 0;

int main(void){
	int T;
	cin >> T;
	FOR(i, 1, T){
		init();
		ans = 0;
		process();
		cout << "Case #" << i << ": " << ans << endl;
		out();
	}
	return 0;
}

void init(void){
	cin >> N;
	char c;
	FOR(i, 1, N){
		FOR(j, 1, N){
			cin >> c;
			while(c != '0' && c != '1'){
				cin >> c;
			}
			Matrix[i][j] = c - '0';
		}
	}
}

void process(void){
	FOR(i, 1, N){
		Index[i] = 1;
		FOR(j, 1, N){
			if(Matrix[i][j]){
				Index[i] = j;
			}
		}
	}
	ans = 0;
	FOR(i, 1, N){
		int j;
		for(j=i; j<=N; j++){
			if(Index[j] <= i){
				break;
			}
		}
		ans += (j - i);
		for(; j>i; j--){
			int t = Index[j];
			Index[j] = Index[j - 1];
			Index[j - 1] = t;
		}
	}
}

void out(void){
}
