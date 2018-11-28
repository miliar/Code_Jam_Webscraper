#include <vector>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <map>
#include <set>
#include <iostream>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define SZ(u) ((int)u.size())
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<ll> vll;

inline bool isDigit(char a) { return '0' <= a && a <= '9'; }

int P, N;
vll M, price;
vi level;
vector<vll> D;

void pre_process();
void input();
void process();

int main()
{
	int t, T;
	//scanf("%d", &T);
	cin >> T;
	pre_process();

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
		fflush(stdout);
	}
	return 0;
}

void pre_process() {
}
void input() {
	int i, j;
	cin >> P;
	N = (1<<P);
	
	M = vll(N, 0);
	price = vll(N, 0);
	level = vi(N, 0);
	
	fr (i, N) {
		scanf("%d", &M[i]);
		M[i] = P-M[i];
	}
	
	for (i = P-1; i >= 0; i--) {
		for (j = (1<<i); j < (1<<(i+1)); j++) {
			scanf("%d", &price[j]);
			level[j] = i;
		}
	}
}

void process() {
	int i, j;
	D = vector<vll>(N, vll(P, -2));
	for (i = N-1; i >= 1; i--) {
		fr (j, (level[i]+1)) {
			D[i][j] = -1;
			if (level[i] == P-1) {
				if (j >= M[i*2-N] && j >= M[i*2-N+1]) D[i][j] = 0;
				else if (j+1 >= M[i*2-N] && j+1 >= M[i*2-N+1]) D[i][j] = price[i];
				else D[i][j] = -1;
			} else {
				if (D[i*2][j] != -1 && D[i*2+1][j] != -1) {
					D[i][j] = D[i*2][j] + D[i*2+1][j];
				}
				
				if (D[i*2][j+1] != -1 && D[i*2+1][j+1] != -1) {
					if (D[i][j] == -1 || D[i][j] > price[i] + D[i*2][j+1] + D[i*2+1][j+1]) {
						D[i][j] = price[i] + D[i*2][j+1] + D[i*2+1][j+1];
					}
				}
			}
		}
	}
	
	printf("%lld\n", D[1][0]);
}