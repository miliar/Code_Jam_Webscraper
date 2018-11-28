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
#include "Primelist.h"

using namespace std;

typedef pair < int, int > II;
typedef vector < int > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC > VVC;
typedef stringstream SS;
typedef set < int > SI;
typedef long long  LL;

#define all(c) (c).begin(), (c).end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)


int main(){
	int T;
	cin >> T;
	sfor(int, testcase, 1, T+1){
		cout << "Case #" << testcase << ": ";
		string s;
		cin >> s;
		s = "0" + s;
		next_permutation(all(s));
		if(s[0]!='0')
			cout << s << endl;
		else
			cout << string(s.begin()+1, s.end()) << endl;
	}
	return 0;
}







