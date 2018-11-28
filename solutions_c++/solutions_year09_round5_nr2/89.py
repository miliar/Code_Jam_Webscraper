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
void process(int, int);
void out(int);

string E;
const int MaxT = 5;
string Terms[MaxT + 1];
int K;
int Tn;
const int Maxn = 20;
string S[Maxn + 1];
int N;
int F[500];
const int MaxK = 5;
int Ans[MaxK + 1];
int ans;
int Visit[Maxn + 1];
int coef;

int main(void){
	int T;
	cin >> T;
	FOR(i, 1, T){
		init();
		coef = 1;
		FOR(j, 1, K){
			ans = 0;
			coef *= j;
			process(1, j);
			Ans[j] = ans;
		}
		out(i);
	}
	return 0;
}

void init(void){
	cin >> E >> K;
	cin >> N;
	FOR(i, 1, N){
		cin >> S[i];
	}
	{
		Tn = 0;
		stringstream ss;
		ss << E;
		char tmp[1000];
		ss >> tmp;
		char *p = strtok(tmp, "+");
		while(p){
			stringstream ss;
			ss << p;
			ss >> Terms[++Tn];
			p = strtok(NULL, "+");
		}
	}
}

int fac(int i){
	if(i == 0) return 1; else return i * fac(i - 1);
}

void evaluate(void){
	int tmp = 0;
	FOR(i, 1, Tn){
		int tmp2 = 1;
		FOR(j, 0, sz(Terms[i]) - 1){
			tmp2 *= F[Terms[i][j]];
			tmp2 %= 10009;
		}
		tmp += tmp2;
		tmp %= 10009;
	}
	int tmp1 = coef;
	FOR(i, 1, N){
		tmp1 /= fac(Visit[i]);
	}
	tmp1 %= 10009;
	ans += tmp * tmp1;
	ans %= 10009;
}

void process(int i , int k){
	if(i == N + 1){
		if(k == 0)evaluate();
	} else{
		if(k > 0){
			FOR(j, 0, sz(S[i]) - 1){
				F[S[i][j]]++;
			}
			Visit[i]++;
			process(i, k - 1);
			Visit[i]--;
			FOR(j, 0, sz(S[i]) - 1){
				F[S[i][j]]--;
			}
		}
//		if(N-i >= k){
			process(i + 1, k);
//		}
	}
}

void out(int C){
	printf("Case #%d:" , C);
	FOR(i, 1, K){
		printf(" %d", Ans[i] % 10009);
	}
	printf("\n");
}
