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
#include <bitset>
#include <stack>

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

template <class T> string toString(T n){ostringstream oss;oss<<n;oss.flush();return oss.str();}
template <class T> string vectorToString(vector < T > v, string seperator){
	ostringstream oss;
	tr(v, e)
	oss << *e << seperator;
	oss.flush();
	return oss.str();
}



int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		LL r, k, n;
		cin >> r >> k >> n;
		VI g(n);
		tr(g, it) cin >> *it;

		VI hist(n, -1);

		int pos = 0;
		LL round = 0;
		VI vStack;
		LL ans = 0;
		while(round < r){
			if(true && hist[pos] != -1){ // varit här förut
				LL delta = round - hist[pos];
				LL rem  = (r - round) % delta;
				LL kvot = (r - round) / delta;
				LL totsum  = accumulate(vStack.end()-delta, vStack.end(), LL());
				LL partsum = accumulate(vStack.end()-delta, vStack.end()-delta + rem, LL());
				ans += totsum * kvot + partsum;
				break;
			}
			hist[pos] = round;
			int pos1 = pos;
			LL dollars = 0;
			bool first = true;
			while(((pos1 != pos) || first) && dollars + g[pos1] <= k){
				first =false;
				dollars += g[pos1];
				pos1++;
				pos1 %= n;
			}
			pos=pos1;
			ans += dollars;
			vStack.push_back(dollars);
			round++;
		}

		cout << "Case #" << testCase << ": " << ans << endl;
	}
}











