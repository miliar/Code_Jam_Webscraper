#include <sstream>
#include <iomanip>
#include <iostream>
#include <stdlib.h>
#include <cmath>
#include <deque>
#include <vector>
#include <iostream>
#include <fstream>
#include <fstream>
#include <string>
using namespace std;

#define MY_SHOW(x)		cout  << #x << endl;
#define MY_DEBG(x)		cout  << "DEBUG: " #x " = " << x << endl;
#define MY_FIND(F,S)	(S.find(S) == S.string::npos)

#define SZ(v)					((int)(v).size())
#define FOR(i,a,b)				for(int i=(a);i<(b);++i)
#define REP(i,n)				FOR(i,0,n)
#define FORE(i,a,b)				for(int i=(a);i<=(b);++i)
#define REPE(i,n)				FORE(i,0,n)
#define FORSZ(i,a,v)			FOR(i,a,SZ(v))
#define REPSZ(i,v)				REP(i,SZ(v))

string itoa (int i) {
	string ret ("");
	do {
		ret = ((char) ((i%10) + '0')) + ret;
		i /= 10;
	} while (i);
	return ret;
}

int main (int argc,char *argv[]) {
	system("clear");
	MY_SHOW(==== int main ())
	string instring ("B-large"); //instring += argv[2]; 
	instring += ".in";
	string oustring ("B-large"); //oustring += argv[2]; 
	oustring += ".out";
	MY_DEBG(instring)
	MY_DEBG(oustring)
	ifstream infile;
	ofstream oufile;
	infile.open(instring.c_str());

	MY_SHOW(== VARIABLES DECLARATION)
	
	//INPUT
	int T, N, S, p;
	//COMPUTING
	//~ deque <int> t;
	//~ deque <deque <int> > hscore;
	int t;
	#define P3 (3*p)
	#define DF ((t) - (P3))
	int uspz;
	//OUTPUT
	deque <int> ret;
	deque <string> os;
	//DEBUG
	string helper;


	MY_SHOW(== MAIN)

	infile >> T;
	MY_DEBG(T)
	cin >> helper;
	REP(i,T) {
		ret.push_back(0);
		os.push_back("");
		infile >> N >> S >> p;
		uspz = 0;
		REP(j,N) {
			infile >> t;
			if (t >= p) {
				if (DF >= -2) {
					ret[i]++;
				} else {
					if (DF >= -4) {
						if (uspz < S) {
							ret[i]++;
							uspz++;
						}
					}
				}
			}
		}
	}
	infile.close();

	MY_SHOW(== Output File Writting)
	oufile.open(oustring.c_str());
	REP(i,T) {
		os[i] += ("Case #" + itoa(i+1) + ": ");
		os[i] += itoa(ret[i]);
		os[i] += "\n";
		oufile << os[i];
		MY_DEBG(os[i])
	}
	oufile.close();

	MY_SHOW(==== End of Program)
	return 0;
}
