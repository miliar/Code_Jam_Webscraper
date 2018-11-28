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
#include<time.h>

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
typedef complex<int> pnt;

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

FILE *in = fopen("a.in" , "r");
FILE *op = fopen("a.out" , "w");

void init(void);
void process(void);
void out(void);

const int pn = 4;
const pnt pv[pn] = {
	pnt (0 , -1),
	pnt (0 , 1),
	pnt (-1 , 0),
	pnt (1 , 0)
};

const int Maxn = 5000;

struct PREF{
	int a , b , c;
} Pre[Maxn + 1];
int n;
int A[Maxn + 1];
int B[Maxn + 1];
int C[Maxn + 1];
int check[Maxn + 1];
int ans;

int main(void){
	int K;
	fscanf(in , "%d" , &K);
	FOR(i , 1 , K){
		clock_t st = clock();
		init();
		process();
		out();
		fprintf(op , "Case #%d: %d\n" , i , ans);
	clock_t en = clock();
	printf("%lf\n" , double(en - st) / CLOCKS_PER_SEC);
	}
	fclose(in);
	fclose(op);
	return 0;
}

bool PA(int a , int b){
	return (Pre[a].a < Pre[b].a);
}

bool PB(int a , int b){
	return (Pre[a].b < Pre[b].b);
}

bool PC(int a , int b){
	return (Pre[a].c < Pre[b].c);
}

void init(void){
	ans = INT_MIN;
	fscanf(in , "%d" , &n);
	FOR(i ,1  , n){
		fscanf(in , "%d %d %d" , &Pre[i].a , &Pre[i].b , &Pre[i].c);
		A[i] = i;
		B[i] = i;
		C[i] = i;
	}
	sort(&A[1] , &A[n + 1] , PA);
	sort(&B[1] , &B[n + 1] , PB);
	sort(&C[1] , &C[n + 1] , PC);
}

void process(void){
	int cnt;
	int a , b , c , ib , ic;
	for(a=0; a<=10000; a++){
		cnt = 0;
		FOR(i , 1 , n){
			check[A[i]] = 4;
			if(Pre[A[i]].a <= a){
				check[A[i]] |= 1;
			}
		}
		ib = 0;
		ic = n;
		for(b=0, c=10000-a; c>=0; b++,c--){
			while(ib <= n && Pre[B[ib]].b <= b){
				check[B[ib]] |= 2;
				if(check[B[ib]] == 7){
					cnt++;
				}
				ib++;
			}
			while(ic >= 1 && Pre[C[ic]].c > c){
				if(check[C[ic]] == 7){
					cnt--;
				}
				check[C[ic]] &= 3;
				ic--;
			}
			ans = max(ans , cnt);
		}
	}
}

void out(void){
}
