#define _GLIBCXX_DEBUG
//Arash Rouhani
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
#include <map>
#include <bitset>

using namespace std;

typedef long long LL;
typedef pair < LL, LL > II;
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

template <class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template <class T> string vectorToString(vector < T > v, string seperator){
	ostringstream oss;
	tr(v, e)
	oss << *e << seperator;
	oss.flush();
	return oss.str();
}


VI x;
VI v;
LL n, k, b, t;

int willReach(int ix){
	return (v[ix]*t + x[ix] >= b);
}

int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		cin >> n >> k >> b >> t;
		x = VI(n);
		v = VI(n);
		tr(x, it) cin >> *it;
		tr(v, it) cin >> *it;

		if(k == 0){
			cout << "Case #" << testCase << ": " << 0 << endl;
			continue;
		}
		reverse(all(x));
		reverse(all(v));

		VI stored(n, -123);

		int sum = 0;
		int count = 0;
		bool fail = true;
		foru(i, n){
			if(willReach(i)){
				int punish = 0;
				int bel = i-1;
				while(true){
					if(bel < 0){
						break;
					}
					else{
						if(stored[bel]==-1){
							punish++;
						}
						else{
							punish += stored[bel];
							break;
						}
					}
					bel--;
				}
				stored[i] = punish;
				sum += punish;
				count++;
				if(count >= k){
					fail = false;
					break;
				}
			}
			else{
				stored[i] = -1;
			}
		}
		LL bestSoFar = -1;
		tr(stored, it){
			//if((bestSoFar > *it) && (*it >= 0)) throw;
			bestSoFar = max(bestSoFar, *it);
		}

		if(fail){
			cout << "Case #" << testCase << ": " << "IMPOSSIBLE" << endl;
		}
		else{
			cout << "Case #" << testCase << ": " << sum << endl;
		}
	}
}











