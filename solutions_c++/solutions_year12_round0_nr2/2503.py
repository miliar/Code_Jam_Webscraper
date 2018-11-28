#include <iostream>
#include <map>
#include <fstream>
//#include "all.h"
using namespace std;

int main(){
	string file = "in.in";
	freopen(file.c_str(), "r", stdin);
	int t;
	cin >> t;
	ofstream of;
	of.open("out.txt");

	int n, s, p, ti;
	int normal, surprise;
	int n_n, n_s;
	int normal1[11];
	int surprise1[11];
	for (int i=0; i<11; i++) {
		if (i>=2){
			normal1[i] = 3*i-2;
			surprise1[i] = 3*i - 4;
		} else {
			normal1[i] = i;
			surprise1[i] = i;
		}
	}

	for(int i=0; i<t; i++) {
		cin >> n >> s >> p;
		if (p>10) {
			of << "Case #"<< i + 1 << ": " << 0 << endl;
			continue;
		}

		normal = normal1[p];
		surprise = surprise1[p];

		n_n = 0; n_s = 0;
		for (int j=0; j<n; j++) {
			cin >> ti;
			//cout << ti << " ";
			if (ti>=normal) n_n++;
			else if (ti>=surprise) n_s++;
		}

		if (n_s > s) n_s = s;
		of << "Case #"<< i + 1 << ": " << n_n + n_s << endl;
	}
	of.close();
	return 0;
}
