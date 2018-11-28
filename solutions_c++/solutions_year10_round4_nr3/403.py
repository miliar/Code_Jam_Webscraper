#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <cstring>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pii> vpii;
typedef vector<vector<pii> > vvpii;

#define DEBUG 0
#define forn(i, n) for(int i = 0; i < n; i++)
#define fors(i, c) for(int i = 0; i < (c).size(); i++)
#define tr(i, c) for((typeof (c).begin()) i = (c).begin(); i != (c).end(); i++)
#define all(c) (c).begin(), (c).end()

char m[128][128];
char c[128][128];
int x1, y1, x2, y2;
int R;

int main(){
	int C;
	cin >> C;
	forn(cc, C){
		cin >> R;
		int cont = 0;
		memset(m, 0, sizeof m);
		for(int i = 0; i < R; i++){
			cin >> x1 >> y1 >> x2 >> y2;
			for(int a = x1; a <= x2; a++)
				for(int b = y1; b <= y2; b++){
					if (!m[a][b]) cont ++;
					m[a][b] = 1;
				}
		}
		
		int k = 0;
		while (cont != 0){
			memset(c, 0, sizeof c);
			if (DEBUG){
				cout << cont << endl;
				for(int i = 0; i < 10; i++){
					for(int j = 0; j < 10; j++){
						if (m[i][j]) cout << "1 ";
						else cout << "  ";
					}
					cout << endl;
				}
				cin.get();
			}
			for(int a = 1; a <= 100; a++)
			for(int b = 1; b <= 100; b++){
				if (!m[a][b] && m[a][b-1] && m[a-1][b])
				{
					cont++;
					c[a][b] = 1;
				}
			}
			for(int a = 1; a <= 100; a++)
			forn(b, 101){
				if (m[a][b] && !m[a][b-1] && !m[a-1][b]){
					c[a][b] = -1;
					cont--;
				}
			}
			forn(a, 101)
			forn(b, 101){
				if (c[a][b] == 1)
				{
					m[a][b] = 1;
				}
				if (c[a][b] == -1)
				{
					m[a][b] = 0;
				}
			}
			k++;
		}
		cout << "Case #" << cc+1 << ": " << k << endl;
	}
}