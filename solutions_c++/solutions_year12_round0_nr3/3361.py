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

#define QUEST "C"
#define MY_SHOW(x)		cout  << #x << endl;
#define MY_DEBG(x)		cout  << "DEBUG: " #x " = " << x << endl;
#define DOLOG
#ifdef DOLOG
	#define MY_LOG(x)		(#x)<<"\t\t = "<<(x)<<endl;
#else
	#define MY_LOG(x)		"";
	#define lgstring cout
#endif

#define SZ(v)					((int)(v).size())
#define FOR(i,a,b)				for(int i=(a);i<(b);++i)
#define REP(i,n)				FOR(i,0,n)
#define FORE(i,a,b)				for(int i=(a);i<=(b);++i)
#define REPE(i,n)				FORE(i,0,n)
#define FORSZ(i,a,v)			FOR(i,a,SZ(v))
#define REPSZ(i,v)				REP(i,SZ(v))
#define MY_FIND(F,S)	(S.find(S) == S.string::npos)

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

			MY_SHOW(==== PREAMBLE)

	string instring (string(QUEST)+"-small-attempt"); instring += argv[2]; instring += ".in";
	#ifdef DOLOG
	string lgstring (string(QUEST)+"-small-attempt"); lgstring += argv[2]; lgstring += ".log";
	#endif
	string oustring (string(QUEST)+"-small-attempt"); oustring += argv[2]; oustring += ".out";
	MY_DEBG(instring)
	#ifdef DOLOG
	MY_DEBG(lgstring)
	#endif
	MY_DEBG(oustring)
	ifstream infile;
	ofstream lgfile;
	ofstream oufile;

			MY_SHOW(== VARIABLES DECLARATION)
	
		//INPUT
	int T, A, B; //N, S, p;
		//COMPUTING
	int sizeab;
	int piece1, piece2, shift, m;
	deque<int> usedm;
	bool troll;
		//OUTPUT
	deque <int> Comp;
	deque <string> Out;
		//DEBUG
	string helper;


			MY_SHOW(== MAIN)

	infile.open(instring.c_str());
	#ifdef DOLOG
	lgfile.open(lgstring.c_str());
	#endif
	infile >> T;
	MY_DEBG(T)
	lgfile << MY_LOG(T);
	REP(i,T) {
		Comp.push_back(0);
		Out.push_back("");
		infile >> A >> B;
		lgfile << "Case #" << itoa(i+1) << ": " << endl;
		lgfile << MY_LOG(A);
		lgfile << MY_LOG(B);
		sizeab = log10(A)+1;
		lgfile << MY_LOG(sizeab);
		if (sizeab != (int) log10(B) + 1) {
			lgfile << MY_LOG((int) log10(A));
			lgfile << MY_LOG((int) log10(B));
			MY_SHOW(ERROR: lenth of A != lenth of B)
			cin >> helper;
		}
		usedm.resize(sizeab,-1);//OBS: I could have used "sizeab-1" in stead of sizeab, but the memory economy didn't worth the extra work.
		FOR(n,A,B) {
			lgfile << "\t" << MY_LOG(n);
			FOR(k,1,sizeab) {
				shift = pow(10, k);
				piece1 = n/shift;
				piece2 = (n%shift)*pow(10,sizeab)/shift;
				usedm[k] = m = piece1 + piece2;
				lgfile << "\t" << "\t" << MY_LOG(shift);
				lgfile << "\t" << "\t" << MY_LOG(piece1);
				lgfile << "\t" << "\t" << MY_LOG(piece2);
				lgfile << "\t" << "\t" << MY_LOG(m);
				troll = false;
				FOR(l,1,k) {
					if (m == usedm[l]) {troll = true;	break;}
					lgfile << "\t" << "\t" << "\t" << MY_LOG(m == usedm[l]);
				}
				if ((!troll) && (A <= n) && (n < m) && (m <= B)) {//Long Live BRUTE FORCE!
					Comp[i]++;
				}
				lgfile << "\t" << "\t" << MY_LOG((!troll) && (A <= n) && (n < m) && (m <= B));
				lgfile << "\t" << "\t" << MY_LOG(Comp[i]);
			}
			lgfile << "\t" << "\t" << MY_LOG(Comp[i]);
		}
		lgfile << "\t" << "\t" << MY_LOG(Comp[i]);
	}
	infile.close();
	lgfile.close();

			
			MY_SHOW(== Output File Writting)
	oufile.open(oustring.c_str());
	REP(i,T) {
		Out[i] += ("Case #" + itoa(i+1) + ": ");
		Out[i] += itoa(Comp[i]);
		Out[i] += "\n";
		oufile << Out[i];
		//~ MY_DEBG(Out[i])
	}
	oufile.close();

			MY_SHOW(==== End of Program)
	return 0;
}

