#include <iostream>
#include <fstream>
using namespace std;

int main (int argc, char * const argv[]) {
	
	int tests,test;
	
	int n, k, b, t,i;
	int x[50];
	int v[50];
	string s;
	ifstream in("B.in");
	ofstream out("B-out.txt");
	int intime;
	int changes;
	int hastopass;
	in >> tests;
	for (test = 0; test < tests; test++) {
		in >> n >> k >> b >> t;
		intime = 0;
		changes = 0;
		hastopass = k;
		for (i=0; i<n; i++) {
			in >> x[i];
		}
		for (i=0; i<n; i++) {
			in >> v[i];
		}
		
		for (i=n-1; i>=0; i--) {
			if(v[i] * t < b - x[i]){//Is this chick will be in time
				//This chick does not get in time, so all other chiks has to pass her
				changes += hastopass;
			}else {
				intime++;
				if(intime == k){
					break;
				}
				hastopass--;
				if(hastopass < 0){
					hastopass = 0;
				}
			}
		}
		if(intime  == k){
			out << "Case #" << test + 1 << ": " << changes << endl;
			cout << "Case #" << test + 1 << ": " << changes << endl;
		}else {
			out << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << endl;
			cout << "Case #" << test + 1 << ": " << "IMPOSSIBLE" << endl;
		}

		
	}
	
	cin >> n;
	
	return 0;
}
