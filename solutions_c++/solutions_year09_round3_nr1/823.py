#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include <fstream>

using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (int i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (int var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

#define INF 1000000

LL sval[1000];

LL getVal(LL base, string s)
{
	LL res = 0;
	LL temp = 1;
	int len = s.length();
	REP(i, len){
//		cout<< "sval["<< s[i]<< "] = "<< sval[s[i]]<< endl;
		res += sval[s[len-i-1]]*temp;
		temp *= base;
	}

	return res;
}



int main (int argc, char * const argv[]) {
	ifstream ifile("A-large.in");
	ofstream ofile("output2");
	int caseCount;
	ifile>>caseCount;

	string s;
	int base;

	REP(c, caseCount){
		ifile >> s;

		REP(i, 256){
			sval[i] = -1;
		}
		base = 0;

		REP(i, s.length()){
			if(sval[s[i]] == -1){
				if(base == 0){
					sval[s[i]] = 1;					
				}else if(base == 1){
					sval[s[i]] = 0;
				}else{
					sval[s[i]] = base;
				}
				base++;
			}
		}
		if(base < 2)
			base = 2;
		
		ofile<< "Case #"<< c+1<< ": "<< getVal(base, s)<< endl;
	}

	ifile.close();
	return 0;
}
