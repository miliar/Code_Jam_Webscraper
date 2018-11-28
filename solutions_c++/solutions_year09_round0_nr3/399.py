
#include <iostream>
#include <algorithm>
#include <vector>
#include <stdlib.h>
#include <iomanip>

using namespace std;

string a = "welcome to code jam";

const int md = 10000;

int solveCase() {
	string str;
	getline(cin,str);

	if (str.size()<1) {
		return 0;
	}

	int d[a.size()+1][str.size()+1];

	for (int i=0; i<=str.size(); i++) d[a.size()][i] = 1;

	for (int i=0; i<a.size(); i++) d[i][str.size()] = 0;

	for (int i=a.size()-1; i>=0; i--) {
		for (int j=str.size()-1; j>=0; j--) {
			if (a[i]!=str[j]) {
				d[i][j] = d[i][j+1];
			}
			else {
				d[i][j] = (d[i][j+1] + d[i+1][j+1])%md;
			}
		}
	}

	return d[0][0];
}


int main() {
	int ncases;
	cin>>ncases;
	cin.ignore();
	for (int i=0; i<ncases; i++) {
		cout<<"Case #"<<i+1<<": "<<setw(4)<<setfill('0')<<solveCase()<<"\n";
	}
	return 0;
}

