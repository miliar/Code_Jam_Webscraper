#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <cctype>
#include <vector>
#include <queue>
#include <tr1/unordered_map>
#include <cmath>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> ii;
typedef long double real;

///////////////////////////////UTIL/////////////////////////////////
#define ALL(x) (x).begin(),x.end()
#define CLEAR(v) memset(v, 0, sizeof(v))
#define REP(i,n) for(int i = 0; i<n; i++)
#define REPP(i,a,n) for(int i = a; i<n; i++)
#define REPD(i,n) for(int i = n-1; i>-1; i--)
#define REPDP(i,a,n) for(int i = a; i>-1; i--)
/////////////////////////////NUMERICAL//////////////////////////////
#define MOD 100
#define INCMOD(a,b) a = (a+b)%MOD
#define DECMOD(a,b) a = (a+MOD-1)%mod
#define ROUNDINT(a) (int)((double)a + 0.5)
#define INF 2000000000
/////////////////////////////BITWISE////////////////////////////////
#define CHECK(S, j) (S & (1 << j))
#define CHECKFIRST(S) (S & (-S))  //PRECISA DE UMA TABELA PARA TRANSFORMAR EM INDICE
#define SET(S, j) S |= (1 << j)
#define SETALL(S, j) S = (1 << j)-1  //J PRIMEIROS
#define UNSET(S, j) S &= ~(1 << j)
#define TOOGLE(S, j) S ^= (1 << j)

int fatorial(int a){
	if(a < 2) return 1;
	return a*fatorial(a-1);
}

int erros(int n, int p){
	return (fatorial(n) / fatorial (n-p)); 
}

double res[5];

int main()
{
	int t, ca = 0, a, b, lim;
	double c[100000];
	scanf(" %d ", &t);
	while(t--){
		scanf(" %d %d ", &a, &b);
		REP(i, a) scanf(" %lf ", &c[i]);
		lim = (1 << a);
		int set = 0, num;
		double chance;
		REP(i, a+2) res[i] = 0.0;
		while(set != lim){
			chance = 1.0;
			//cout << "CHANCE EH " << chance;
			REP(i, a){
				if(CHECK(set, i)) chance *= (1.0 - c[i]);
				else chance *= c[i];
				//cout << "CHANCE EH " << chance;
			}
			//cout << "ERRANDO " << set << endl;
			REP(back, a+1){
				//cout << "BACKSPACES " << back << endl;
				int newset = set;
				//cout << "NEWSET EH " << newset << endl;
				REP(j, back){
					UNSET(newset, (a-1-j));
					//cout << "UNSETANDO " << (a-1-j) << endl;
				}
				//cout << "NEWSET EH " << newset << endl;
				if(newset){
					num = 2*back + (b - a) + 2 + b;
					//cout << "NUM EH " << num << endl;
				}
				else{
					num = 2*back + (b -a) + 1;
				}
				//cout << "NUM " << num << " CHANCE " << chance << endl;
				res[back] += num*chance;
				//cout << "RES " << back << " EH " << res[back] << endl << endl;
			}
			num = 2 + b;
			res[a+1] += num*chance;
			//cout << "NUM " << num << " CHANCE " << chance << endl;
			//cout << "RES " << a+1 << " EH " << res[a+1] << endl << endl;
			set++;
		}
		double m = 2000000000.00;
		REP(i, a+2){
			if(res[i] < m) m = res[i];
			//cout << "RES " << i << " EH " << res[i] << endl;
		}
		printf("Case #%d: %.6lf\n", ++ca, m); 
	}
}
