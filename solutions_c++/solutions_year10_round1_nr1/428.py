#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <list>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <queue>

using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define all(c) (c).begin(), (c).end()
#define pb push_back
#define mp make_pair

typedef long long int tint;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;

const int maxn = 50 + 10;
char tab[maxn][maxn];
int n, K;
int dx[4] = {1, 0, 1, 1};
int dy[4] = {0, 1, -1, 1};

bool red, blue;

inline bool isin(int a, int b){ return (a>=0 && a<n && b>=0 && b<n); }

void check(){
	blue = red = false;

	forn(i, n) forn(j, n){
		if(tab[i][j] == '.') continue;
		if(tab[i][j] == 'R' && red) continue;
		if(tab[i][j] == 'B' && blue) continue;
		forn(k, 4){
			int tmp = 0;
			int u = i, v = j; //se puede optimizar
			do{
				tmp++;
				u = u+dx[k], v = v+dy[k];
			}while(isin(u, v) && tab[u][v] == tab[i][j]);
			if(tmp >= K){
				if(tab[i][j] == 'R') red = true;
				else blue = true;
			}
		}
	}
}

void voltea(){
	char tab2[maxn][maxn];
	forn(i, n) forn(j, n) tab2[j][n-1-i] = tab[i][j];
	forn(i, n) forn(j, n) tab[i][j] = tab2[i][j];
}

void cae(){
	for(int i=n-1; i>=0; i--){
		forn(j, n){
			int u = i, v = j;
			while(tab[u][v]!='.' && u<n-1 && tab[u+1][v] == '.'){
				tab[u+1][v] = tab[u][v]; tab[u][v] = '.';
				u++;
			}
		}
	}
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);

	int NC; cin >> NC;
	forn(nc, NC){
		cin >> n >> K;
		forn(i, n) forn(j, n) cin >> tab[i][j];

//		forn(i, n){ forn(j, n) cout << tab[i][j]; cout << endl; }
//		cout << endl;

		voltea();

//		forn(i, n){ forn(j, n) cout << tab[i][j]; cout << endl; }
//		cout << endl;

		cae();

//		forn(i, n){ forn(j, n) cout << tab[i][j]; cout << endl; }
//		cout << endl;

		check();
		cout << "Case #" << nc+1 << ": ";
		if(blue && red) cout << "Both";
		else if(blue) cout << "Blue";
		else if(red) cout << "Red";
		else cout << "Neither";
		cout << endl;
	}

	return 0;
}
