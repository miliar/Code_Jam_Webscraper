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

FILE *in = fopen("d.in" , "r");
FILE *op = fopen("d.out" , "w");

void init(void);
void process(void);
void out(void);

const int pn = 4;
const int py[pn + 1] = {0 , -1 , 1 , 0 , 0};
const int px[pn + 1] = {0 , 0 , 0 , -1 , 1};

const int MaxFn = 1000;
const int Maxn = 30;

int n , m;

int Fn;
int Fp[MaxFn + 1][2];
int Dis[MaxFn + 1][MaxFn + 1];
int D[MaxFn + 1];
bool V[MaxFn + 1];

int Map[Maxn + 1][Maxn + 1];
ii Bfs[Maxn + 1][Maxn + 1];

int ans;

int main(void){
	int K;
	fscanf(in , "%d" , &K);

	FOR(i , 1 , K){
		ans = 0;
		init();
		process();
		out();
		fprintf(op , "Case #%d: %d\n" , i , ans);
	}
	fclose(in);
	fclose(op);
	return 0;
}

void init(void){
	fscanf(in , "%d %d" , &n , &m);
	Fn = 0;
	FOR(i , 1 , n){
		FOR(j , 1 , m){
			char c;
			fscanf(in , "%c" , &c);
			while(c == '\n' || c == ' '){
				fscanf(in , "%c" , &c);
			}
			if(c == 'T'){
				Map[i][j] = 1;
				Fn++;
				Fp[Fn][0] = i;
				Fp[Fn][1] = j;
			} else if(c == '#'){
				Map[i][j] = 2;
			} else{
				Map[i][j] = -1;
			}
			if(Map[i][j] > 0){
				Bfs[i][j].first = INT_MAX;
			} else{
				Bfs[i][j].first = 0;
			}
			Bfs[i][j].second = 0;
		}
	}
}

void dobfs(int sy , int sx , int f){
	Bfs[sy][sx].first = 0;
	Bfs[sy][sx].second = f;
	queue<ii> Q;
	Q.push(mk(sy , sx));
	while(sz(Q)){
		ii now = Q.front();
		ii b = Bfs[now.first][now.second];
		Q.pop();
		FOR(i , 1 , pn){
			ii to = now;
			to.first += py[i];
			to.second += px[i];
			if(to.first > 0 && to.first <= n && 
				to.second > 0 && to.second <= m && 
				Map[to.first][to.second] > 0 &&
				Bfs[to.first][to.second].first > b.first + 1){

				Bfs[to.first][to.second] = b;
				Bfs[to.first][to.second].first++;
				Q.push(to);
			}
		}
	}
}

void finddis(int sy , int sx , int f){
	FOR(i , 1 , n){
		FOR(j , 1 , m){
			if(Bfs[i][j].second == f){
				int d1 = Bfs[i][j].first;
				FOR(k , 1 , pn){
					ii to;
					to.first = i + py[k];
					to.second = j + px[k];
					if(to.first > 0 && to.first <= n && 
						to.second > 0 && to.second <= m &&
						Map[to.first][to.second] > 0 && 
						Bfs[to.first][to.second].second != f){
						
						int d2 = Bfs[to.first][to.second].first;
						int f2 = Bfs[to.first][to.second].second;
						int cost = ((d2+1) * (d1 + 1 + d1 + d2+1)) / 2 - 
							(d2 * (d2 + 1)) / 2;
						Dis[f][f2] = min(Dis[f][f2] , cost);
					}
				}
			}
		}
	}
}

void prim(void){
	D[1] = 0;
	V[1] = false;
	FOR(i , 2 , Fn){
		D[i] = INT_MAX;
		V[i] = false;
	}
	FOR(T , 1 , Fn){
		int md = INT_MAX, mi = 0;
		FOR(i , 1 , Fn){
			if(!V[i] && md > D[i]){
				md = D[i];
				mi = i;
			}
		}
		assert(md != INT_MAX);
		V[mi] = true;
		ans += md;
		FOR(j , 1 , Fn){
			if(!V[j] && Dis[mi][j] < D[j]){
				D[j] = Dis[mi][j];
			}
		}
	}
}

void process(void){
	FOR(i ,1 , Fn){
		dobfs(Fp[i][0] , Fp[i][1] , i);
	}
	FOR(i , 1 , n){
		FOR(j , 1 , m){
			ans += Bfs[i][j].first;
			fprintf(stderr , "%d " , Bfs[i][j].first);
		}
		fprintf(stderr , "\n");
	}
	FOR(i , 1 , Fn){
		FOR(j , i + 1 , Fn){
			Dis[i][j] = Dis[j][i] = INT_MAX;
		}
		Dis[i][i] = 0;
	}
	FOR(i , 1 , Fn){
		finddis(Fp[i][0] , Fp[i][1] , i);
	}
	prim();
}

void out(void){
}
