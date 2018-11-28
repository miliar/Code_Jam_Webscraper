#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

typedef unsigned int uint;
typedef long long int64;
typedef unsigned long long uint64;

#define FOI(i, A, B) for(i=A; i<=B; i++)
#define FOD(i, A, B) for(i=A; i>=B; i--)
#define PI		acos(-1.0)
#define INF		1<<30
#define EPS		1e-9
#define sqr(x)	(x)*(x)

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, t;
	cin >> T;
	FOI(t, 1, T){
		int R, C;
		cin >> R >> C;
		string mat[R];
		int i, j;
		FOI(i, 0, R-1)
			cin >> mat[i];
		bool possible = true;
		FOI(i, 0, R-2){
			FOI(j, 0, C-2){
				if (mat[i][j] == '#'){
					if (mat[i+1][j] == '#' && mat[i+1][j+1] == '#' && mat[i][j+1] == '#'){
						mat[i][j]     = '/';
						mat[i][j+1]   = '\\';
						mat[i+1][j]   = '\\';
						mat[i+1][j+1] = '/';
					}
				}
			}
		}
		FOI(i, 0, R-1)
			FOI(j, 0, C-1)
				if (mat[i][j] == '#'){
					possible = false;
					break;
				}
		cout << "Case #" << t << ":\n";
		if (!possible)
			cout << "Impossible\n";
		else{
			FOI(i, 0, R-1)
					cout << mat[i] << endl;
		}
	}
	return 0;
}

