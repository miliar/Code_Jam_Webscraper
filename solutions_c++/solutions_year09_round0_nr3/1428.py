//Arash Rouhani

#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <string>
#include <math.h>
#include <fstream>
#include <numeric>

using namespace std;

typedef pair < int, int > II;
typedef vector < int > VI;
typedef vector < II > VII;
typedef vector < VI > VVI;
typedef vector < string > VS;
typedef vector < VS > VVS;
typedef vector < char > VC;
typedef vector < VC> VVC;
typedef long long  LL;
#define all(c) c.begin(), c.end()
#define tr(c, it) for(typeof((c).begin()) it = (c).begin(); it!=(c).end(); it++)
#define sfor(type, e, start, stop) for(type e=start; e<stop; e++)


int main(){
	const int MV = 10000;
	const string S = "welcome to code jam";
	int ntestcases;
	cin >> ntestcases;
	cin.ignore(1000,'\n');
	sfor(int, testcase, 1, ntestcases+1){
		string input;
		getline(cin, input);
		VI occpos(S.length());

		sfor(int, i, 0, input.length()){
			sfor(int, j, 0, S.length()){
				if(S[j]==input[i]){
					if(j==0){
						occpos[0]++;
						occpos[0]%=MV;
					}
					else{
						occpos[j]+=occpos[j-1];
						occpos[j]%=MV;
					}
				}
			}
		}
		stringstream ss;
		ss << "0000";
		ss << *(occpos.end()-1);
		string o = ss.str();
		o = string(o.end()-4, o.end());

		cout << "Case #" << testcase << ": " << o << endl;
	}
}
