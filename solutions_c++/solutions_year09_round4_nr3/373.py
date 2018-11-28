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
int process(int);
int choose(int, int);
void out(void);

const int MaxN = 16;
const int MaxK = 25;
int Prices[MaxN + 1][MaxK + 1];
int Matrix[MaxN + 1];
int D[1 << MaxN];
int K;
int N;
int ans;

int main(void){
	int T;
	cin >> T;
	FOR(i, 1, T){
		ans = 0;
		set(D, -1);
		init();
		ans = D[0] = process(0);
		out();
		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}

bool inter(int i1, int i2){
	if(Prices[i1][1] == Prices[i2][1]) return true; else if(Prices[i1][1] > Prices[i2][1]){
		FOR(j,1, K){
			if(Prices[i1][j] <= Prices[i2][j]) return true;
		}
		return false;
	} else return inter(i2, i1);
}

void init(void){
	set(Matrix, 0);
	cin >> N >> K;
	FOR(i ,1 , N){
		FOR(j, 1, K){
			cin >> Prices[i][j];
		}
	}
	FOR(i, 1, N){
		FOR(j, i + 1, N){
			bool cross = inter(i, j);
			if(cross){
				Matrix[i] |= (1<<(j-1));
				Matrix[j] |= (1<<(i-1));
			}
		}
	}
}

int choose(int subset, int inter, int i){
	int ret = N;
	if(i > N){
		D[subset] = process(subset);
		ret = D[subset] + 1;
	} else{
		ret = choose(subset, inter, i+1);
		if( !(subset & (1 << (i - 1))) && 
			!(inter & (1 << (i - 1)))){
			int tmp = choose(subset | (1 << (i - 1)), inter | Matrix[i], i + 1);
			ret = min(ret, tmp);
		}
	}
	return ret;
}

int process(int subset){
	if(D[subset] != -1) return D[subset];
	int ret = 0;
	FOR(i, 1, N){
		if(!(subset & (1 << (i - 1)))){
			ret = choose(subset | (1 << (i - 1)), Matrix[i], i + 1);
			break;
		}
	}
//	cerr << subset << ' ' << ret << endl;
	return ret;
}

void out(void){
}
