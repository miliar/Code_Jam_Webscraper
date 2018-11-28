#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cfloat>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define NDEBUG

#if defined(NDEBUG)
#define DBG_CODE(cb...)
#else
#define DBG_CODE(cb...) cb
#endif

#define WRITE(x) DBG_CODE(cout << x << endl)
#define WATCH(x) DBG_CODE(cout << #x << "=" << x << endl)

//[a, b) incrementando
#define FORN(i, a, b) for(typeof(b) i = (a); i < (b); i++)
//(a, b] decrementando
#define FORR(i, a, b) for(typeof(a) i = (a) - 1; i >= (b) && i < (a) ; i--)

#define ALL(x) x.begin(), x.end()
#define FOREACH(i, c) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define FOREACHR(i, c) for(typeof((c).rbegin()) i = (c).rbegin(); i != (c).rend(); i++)

int gcd(int a, int b){
	if (b == 0) return a;
	else return gcd(b, a % b);
}

int lcm(int a, int b){
	return (a*b)/gcd(a,b);
}

int main(){
	//Descomente para acelerar cin
	//ios::sync_with_stdio(false);
	int tst;
	int m, n;
	
	cin >> tst;
	FORN(tc, 1, tst+1){
		cin >> m >> n;
		vector<vector<char> > input(m, vector<char>(n, '.'));
		FORN(i, 0, m){
			FORN(j, 0, n){
				cin >> input[i][j];
			}
			string tmp;
			getline(cin, tmp);
		}

		FORN(i, 0, m-1){
			FORN(j, 0, n-1){
				
				bool tst = true;
				FORN(ii, 0, 2)
					FORN(jj, 0, 2)
						tst = tst and input[i+ii][j+jj] == '#';

				if (tst){
					input[i][j] = '/';
					input[i+1][j] = '\\';
					input[i][j+1] = '\\';
					input[i+1][j+1]= '/';
				}
				DBG_CODE(
				FORN(ii, 0, m){
					FORN(jj, 0, n){	
						cout << (ii == i and jj == j ? 'm' : input[ii][jj]);
					}
					cout << endl;
				}
				cout << endl;
				)
			}
		}
		
		bool solved = true;
		FORN(i, 0, m)
			FORN(j, 0, n)
				solved = solved and input[i][j] != '#';
		
		cout << "Case #" << tc << ":" << endl;
		if (solved){
			FORN(i, 0, m){
				FORN(j, 0, n){
					cout << input[i][j];
				}
				cout << endl;
			}
		} else {
			cout << "Impossible" << endl;
		}
	}
	
}
