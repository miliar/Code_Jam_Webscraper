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
typedef complex<int> pnt;

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

FILE *in = fopen(".in" , "r");
FILE *op = fopen(".out" , "w");

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

int main(void){
	init();
	process();
	out();
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
}

void process(void){
}

void out(void){
}
