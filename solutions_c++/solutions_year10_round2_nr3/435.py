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
const int mod = 100003;
bool works(const SI& si, int p){
	if(p <= 0) throw;
	else if(p == 1) return true;
	else{
		if(si.count(p)){
			int next = 0;
			tr(si, it){
				if(*it <= p){
					next++;
				}
			}
			return works(si, next);
		}
		else{
			return false;
		}
	}
}

int brute(int n){
	// the values stored below are pre-calculated!
	if(n == 17) return 5719;
	if(n == 18) return 10780;
	if(n == 19) return 20388;
	if(n == 20) return 38674;
	if(n == 21) return 73562;
	if(n == 22) return 40265;
	if(n == 23) return 68060;
	if(n == 24) return 13335;
	if(n == 25) return 84884;
	int sum = 0;
	foru(i, 1<<(n-1)){
		if(i){
			SI si;
			bitset < 26 > bs(i);
			foru(j, 26){
				if(bs[j]){
					si.insert(j+2);
				}
			}
			if(works(si, n)){
				sum++;
				sum%=mod;
				VI vi(all(si));
				//cout << vectorToString(vi, " ") << endl;
			}
		}
	}
	return sum;
}

int solve(int n){
	return brute(n);
}
int main(){
	int nTestCases;
	cin >> nTestCases;
	sfor(int, testCase, 1, nTestCases+1){
		int n;
		cin >> n;

		int ans = solve(n);
		cout << "Case #" << testCase << ": " << ans << endl;
	}
}











