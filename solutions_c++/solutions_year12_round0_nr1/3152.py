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
	MY_DEBG(argv[0])
	MY_DEBG(argv[1])
	MY_DEBG(argv[2])
	string instring ("A-small-attempt"); instring += argv[2]; instring += ".in";
	string oustring ("A-small-attempt"); oustring += argv[2]; oustring += ".out";
	MY_DEBG(instring)
	MY_DEBG(oustring)
	ifstream infile;
	ofstream oufile;
	infile.open(instring.c_str());

	MY_SHOW(== Variables Declaration)
	int T;
	string helper;
	#define MYK ((int) 'a')
                          //26 SPACES HERE...
	string EtoG("                          ");//...that go here...
	string GtoE("                          ");//...and here.
	string buffer("teste");
	int buffersize;
	deque<string> ret;
	const string GSample("ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv");
	const string ESample("ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup");

	MY_SHOW(== Calibration)
	int samplesize = GSample.size();
	int Gindex, Eindex;
	REP(i,samplesize) {
		Gindex = (int) GSample[i] - MYK;
		Eindex = (int) ESample[i] - MYK;
		GtoE[Gindex] = ESample[i];
		EtoG[Eindex] = GSample[i];
	}
	//For direct inspetion, I have verified that the only missing letters are 'q' and 'z', so that I inffer that it is possible to do:
	GtoE[(int) 'q' - MYK] = 'z';
	EtoG[(int) 'q' - MYK] = 'z';
	GtoE[(int) 'z' - MYK] = 'q';
	EtoG[(int) 'z' - MYK] = 'q';
	
	MY_DEBG(GtoE)
	MY_DEBG(EtoG)
	
	MY_SHOW(== Substituition)
	infile >> T;
	REP(i,T) {
		ret.push_back("");
	}
	getline(infile,buffer);
	//MY_DEBG(T)
	REP(i,T) {
		//MY_DEBG(buffer)
		getline(infile,buffer);
		//~ MY_DEBG(buffer)
		buffersize = buffer.size();
		ret[i] = ("Case #" + itoa(i+1) + ": ");
		REP(j,buffersize){
			ret[i] += ((buffer[j] == ' ')?(' '):(GtoE[(int) buffer[j] - MYK]));
		}
		ret[i] += "\n";
		//~ MY_DEBG(ret[i])
	}
	infile.close();

	MY_SHOW(== Output File Writting)
	oufile.open(oustring.c_str());
	REP(i,T) {
		oufile << ret[i];
	}
	oufile.close();

	MY_SHOW(==== End of Program)
	return 0;
}
