#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>
#include <iterator>
#include <vector>
#include <algorithm>

using namespace std;

enum match {
	WON,
	LOST,
	NOMATCH
};

int numteams;
enum match *a;

char read_char();

#define MATCH_RESULT(ta, tb) (a[((ta * numteams) + tb)])
double cwp(int team, int discard) {
	double won = 0;
	double games = 0;
	for(int i = 0; i < numteams; ++i) {
		enum match res = MATCH_RESULT(team, i);
		if(i != discard && res != NOMATCH) {
			++games;
			if(res == WON) {
				++won;
			}
		}
	}
	return (won / games);
}

double cowp(int team, int discard) {
	double owp = 0;
	double fought = 0;
	for(int sub = 0; sub < numteams; ++sub) {
		if(MATCH_RESULT(team, sub) != NOMATCH) {
			owp += cwp(sub, team);
			++fought;
		}
	}
	return owp / fought;
}

double coowp(int team) {
	double oowp = 0;
	double fought = 0;
	for(int sub = 0; sub < numteams; ++sub) {
		if(MATCH_RESULT(team, sub) != NOMATCH) {
			oowp += cowp(sub, team);
			++fought;
		}
	}
	return oowp / fought;
}
			
int main(int argc, char **argv) {
	cout.precision(12);
	
	int cases;
	cin >> cases;
	for(int cas = 1; cas <= cases; ++cas) {
		cin >> numteams;
		
		cout << "Case #" << cas << ":" << endl;
		
		a = new match[numteams * numteams];
		
		for(int i = 0; i < (numteams * numteams); ++i) {
			char inp = read_char();
			a[i] = (inp == '.' ? NOMATCH : (inp == '0' ? LOST : WON));
		}
		
		for(int team = 0; team < numteams; ++team) {
			double wp = 0;
			double owp = 0;
			double oowp = 0;
			
			// Calculate played & WP
			wp = cwp(team, team);
			owp = cowp(team, team);
			oowp = coowp(team);
		
			// RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP
			double rpi = (0.25 * wp) + (0.50 * owp) + (0.25 * oowp);
			cout << rpi << endl;
		}

		
		delete[] a;
	}
}

char read_char() {
	char chr;
	while(cin.good() && !cin.eof() && cin.get(chr)) {
		if(chr != '\n' && chr != ' ' && chr != '\0') {
			return chr;
		}
	}
	return '\0';
}

