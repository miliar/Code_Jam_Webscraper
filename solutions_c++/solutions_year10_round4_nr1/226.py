//Arash Rouhani
#define _GLIBCXX_DEBUG
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>
#include <set>
#include <queue>
#include <stack>
#include <bitset>

using namespace std;

typedef long long LL;
typedef pair < int, int > II;
typedef pair < int, II > I_II;
typedef vector < LL > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < VII > VVII;
typedef vector < VVI > VVVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC > VVC;
typedef stringstream SS;
typedef set < int > SI;

#define sz(c) (int((c).size()))
#define all(c) (c).begin(), (c).end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)
#define sford(type, e, start, stop) for(type e=start; e>=stop; e--)
#define foru(var, stop) sfor(int, var, 0, stop)
#define ford(var, start) sford(int, var, start, 0)
#define mp make_pair
#define error(msg) {cout << msg << endl; throw;}
#define assert(cond) if(!(cond)){error(#cond);}

template <class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template <class T> string vectorToString(vector < T > v, string seperator){
	ostringstream oss;
	tr(v, e)
	oss << *e << seperator;
	oss.flush();
	return oss.str();
}

template <class T1, class T2> std::ostream& operator << ( std::ostream& out,
                        const std::pair< T1, T2 >& rhs )
{
    out << "(" << rhs.first << ", " << rhs.second << ")";
    return out;
}


VVI diamond;
VVVI diamonds;
int h, w;

int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		int k;
		cin >> k;
		diamond = VVI(k, VI(k));
		foru(i, k){
			int y = i;
			int x = 0;
			while(y >= 0){
				cin >> diamond[y][x];
				y--;
				x++;
			}
		}

		foru(i, k){if(i==0) continue;
			int y = k-1;
			int x = i;
			while(y >= i){
				cin >> diamond[y][x];
				y--;
				x++;
			}
		}

		diamonds = VVVI(4, VVI(k, VI(k)));
		diamonds[0] = diamond;

		sfor(int, i, 1, 4){
			VVI &d0 = diamonds[i-1];
			VVI &d  = diamonds[i];
			foru(y0, k){
				foru(x0, k){
					int y = x0;
					int x = k - y0 - 1;
					d[y][x] = d0[y0][x0];
				}
			}
		}
		/*
		tr(diamonds, it2){
			tr(*it2, it){
				cout << vectorToString(*it, " ") << endl;
			}
			cout << endl << endl;
		}
		*/
		int ans = 1234567890;
		tr(diamonds, it){
			VVI &d = *it;
			int yExpand = -123;
			int xExpand = -123;
			foru(xE, 100){
				bool works = true;
				foru(y0, k){
					foru(x0, k){
						int delta = y0-x0;
						int moves = delta+xE;
						int y = y0-moves;
						int x = x0+moves;
						if(0 <= y && y < k && 0 <= x && x < k){
							works &= d[y][x] == d[y0][x0];
						}
					}
				}
				if(works){
					xExpand = xE;
					break;
				}
			}
			foru(yE, 100){
				bool works = true;
				foru(y0, k){
					foru(x0, k){
						int delta = (k-x0-1)-y0;
						int moves = delta+yE;
						int y = y0+moves;
						int x = x0+moves;
						if(0 <= y && y < k && 0 <= x && x < k){
							works &= d[y][x] == d[y0][x0];
						}
					}
				}
				if(works){
					yExpand = yE;
					break;
				}
			}
			int tot = k + yExpand + xExpand;
			int now = tot*tot - k*k;
			ans = min(ans, now);
		}
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}











