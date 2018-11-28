#include <vector>
#include <list>
#include <map>
#include <string>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <cstdlib>

using namespace std;

typedef unsigned long long huge;
#define abserr(n) setprecision(n) << fixed << showpoint
string getline();
template <typename T>
inline T get(istream &is = cin);

void solveCase(){
	stringstream line(getline());
	int N;
	line >> N;
	
	char games[N][N];
	
	for(int n=0; n<N; n++){
		stringstream line(getline());
		for(int m=0; m<N; m++)
			line >> games[n][m];
	}
	
	float NO[N], WP[N], OWP[N], OOWP[N];
	
	for(int n=0; n<N; n++){
		int w=0, t=0;
		for(int m=0; m<N; m++){
			if(games[n][m] == '1'){
				w++;
				t++;
			}else if(games[n][m] == '0'){
				t++;
			}
		}
		NO[n] = t;
		WP[n] = 1.0 * w / t;
	}
	for(int n=0; n<N; n++){
		float owp = 0;
		for(int m=0; m<N; m++){
			if(games[n][m] == '.') continue; // not my opponent
			
			float lowp = WP[m] * NO[m];
			
			if(games[n][m] == '0') // if he won me
				lowp -= 1;     // it's as if we didn't play
			
			owp += lowp / (NO[m]-1);
		}
		OWP[n] = owp / NO[n];
	}
	for(int n=0; n<N; n++){
		float oowp = 0;
		for(int m=0; m<N; m++){
			if(games[n][m] == '.') continue;
			oowp += OWP[m];
		}
		OOWP[n] = oowp / NO[n];
	}

	cout << endl;
	for(int n=0; n<N; n++)
		cout << abserr(7) << (0.25 * WP[n] + 0.50 * OWP[n] + 0.25 * OOWP[n]) << endl;
}

int main(int argc, char *argv[]){
	stringstream line(getline());
	unsigned int T;
	
	line >> T;
	
	for(unsigned int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		cerr << "Case #" << t << endl;
		solveCase();
	}
	
	return 0;
}
string getline(){
	string tmp;
	getline(cin, tmp);
	return tmp;
}
template <typename T>
inline T get(istream &is){
	T tmp;
	is >> tmp;
	return tmp;
}

