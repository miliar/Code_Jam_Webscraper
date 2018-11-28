#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <ctime>
using namespace std;
typedef long long LL; 
typedef pair<int, int> PII;
typedef vector<int> VI;
#define PB push_back
#define MP make_pair
#define FOR(i, n) for(int i = 0; i < (n); i++)
#define REP(i, a, b) for(int i = (a); i <= (b); i++)
#define CLR(x, a) memset(x, a, sizeof(x))
//#define L(x) ((x) << 1)
#define R(x) (((x) << 1) + 1)
#define LB(x) ((x)&(-(x)))
#define SL(x) (1 << (x))
#define X first
#define Y second
const int MAXN = 5;

char gp[MAXN][MAXN];

int main(){

	int T; cin >> T; getchar();
	FOR(cas, T){
		printf("Case #%d: ", cas + 1);
		FOR(i, 4){
			gets(gp[i]);
			// cout << gp[i] << endl;
		}
		int w = -2;
		FOR(i, 4)FOR(j, 4){
			if(gp[i][j] == '.'){
				w = -1;
				break;
			}
		}
		FOR(i, 4){
			if(gp[i][0] != '.'){
				bool found = true;
				char c;
				FOR(j, 4){
					if(gp[i][j] != gp[i][0] && gp[i][j] != 'T'){
						found = false;
						break;
					}
					if(gp[i][j] != 'T')c = gp[i][j];
				}
				if(found){
					if(c == 'X')w = 0;
					else w = 1;
				}
			}
			if(gp[0][i] != '.'){
				bool found = true;
				char c;
				FOR(j, 4){
					if(gp[j][i] != gp[0][i] && gp[j][i] != 'T'){
						found = false;
						break;
					}
					if(gp[j][i] != 'T')c = gp[j][i];
				}
				if(found){
					if(c == 'X')w = 0;
					else w = 1;
				}
			}
		}
		bool found = true;
		char c;
		if(gp[0][0] != '.'){
			FOR(j, 4){
				if(gp[j][j] != gp[0][0] && gp[j][j] != 'T'){
					found = false;
					break;
				}
				if(gp[j][j] != 'T')c = gp[j][j];
			}
			if(found){
				if(c == 'X')w = 0;
				else w = 1;
			}
		}
		
		found = true;
		if(gp[0][3] != '.'){
			FOR(j, 4){
				if(gp[j][3 - j] != gp[0][3] && gp[j][3 - j] != 'T'){
					found = false;
					break;
				}
				if(gp[j][3 - j] != 'T')c = gp[j][3 - j];
			}
			if(found){
				if(c == 'X')w = 0;
				else w = 1;
			}
		}
		if(w == 0){
			cout << "X won" << endl;
		}else if(w == 1){
			cout << "O won" << endl;
		}else if(w == -1){
			cout << "Game has not completed" << endl;
		}else{
			cout << "Draw" << endl;
		}
		getchar();
	}
}