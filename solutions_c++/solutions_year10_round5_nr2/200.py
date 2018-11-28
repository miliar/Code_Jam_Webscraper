//Arash Rouhani
#define _GLIBCXX_DEBUG
#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <cmath>
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


int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		LL L;
		int n;
		cin >> L >> n;
		VI boards(n);
		tr(boards, it ) cin >> *it;
		sort(all(boards));
		LL m =  boards.back();


		//check if impossible
		LL gcd = boards[0];
		tr(boards, it){
			gcd = __gcd(gcd, *it);
		}
		if(L%gcd != 0){
			cout << "Case #" << testCase << ": " << "IMPOSSIBLE" << endl;
			continue;
		}

		LL l = L;
		LL ans = 0;
		VI pots;
		pots.push_back(1);
		foru(i, 14) pots.push_back(pots.back() * 10LL);
		reverse(all(pots));

		tr(pots, it){
			LL pot = *it;
			while(pot * m < l - (m*m+100*m)){
				l -= pot*m;
				ans += pot;
			}
		}


		VI stored(l+1);
		stored[0] = 1;

		LL rounds = 0;
		bool hit = false;
		while(rounds < l){
			rounds++;
			ford(i, l){
				foru(j, n){
					int w = boards[j];
					if(i - w >= 0 && stored[i-w]){
						stored[i] = 1;
						if(i == l){
							ans += rounds;
							hit = true;
							break;
						}
					}
					if(hit)break;
				}
				if(hit)break;
			}
			if(hit)break;
		}

		if(!hit){
			cout << "Case #" << testCase << ": " << "IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << testCase << ": " << ans << endl;
		}
	}
}











