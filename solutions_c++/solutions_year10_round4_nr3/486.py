#define _USE_MATH_DEFINES
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <list>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <numeric>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <complex>
#include <stack>
#include <queue>
#include <NTL/ZZ.h>
using namespace std;
using namespace NTL;
static const double EPS = 1e-5;
typedef long long ll;
typedef complex <double> pt;

class GCJ {
public:
	ll solve(int R, vector <int> X1, vector <int> X2, vector <int> Y1, vector <int> Y2) {
		ll res=0, cnt=0;
		vector <vector <int> > grid(102, vector <int>(102, 0)), grid2;

		for(int i=0; i<R; i++) {
			for(int p=X1[i]; p<=X2[i]; p++) {
				for(int q=Y1[i]; q<=Y2[i]; q++) {
					if(grid[q][p]==0) {
						grid[q][p]=1;
						cnt++;
					}
				}
			}
		}

		while(cnt>0) {
			grid2=grid;
			for(int i=1; i<=100; i++) {
				for(int j=1; j<=100; j++) {
					if(grid[i][j]==1) {
						if(grid[i-1][j]==0 && grid[i][j-1]==0) {
							grid2[i][j]=0;
							cnt--;
						}
					} else {
						if(grid[i-1][j]==1 && grid[i][j-1]==1) {
							grid2[i][j]=1;
							cnt++;
						}
					}
				}
			}
			res++;
			grid=grid2;
		}

		return res;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string s, filename;
	char key;
	int testcase, R;
	vector <int> X1, X2, Y1, Y2;
	GCJ gcj;

	for(int i=0; i<12; i++) {
		prb[i].push_back('A'+i/2);
		if(i%2) prb[i]+="-large";
		else prb[i]+="-small-attempt";
		prb[i]+=".in.txt";
		cout << (char)('a'+i) << ". " << prb[i] << endl;
	}
	do {
		cout << "Choose the input file." << endl;
		cin >> key;
	} while(key-'a'<0 || key-'a'>=12);
	filename=prb[key-'a'];
	if((key-'a'+1)&1) {
		do {
			cout << "Choose number of attempt times." << endl;
			cin >> key;
		} while(key-'0'<0 || key-'9'>0);
		filename.insert(15, 1, key);
	}
	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ifs >> testcase; ifs.ignore();
	for(int i=1; i<=testcase; i++) {
		ifs >> R;
		X1.resize(R); X2.resize(R); Y1.resize(R); Y2.resize(R);
		for(int j=0; j<R; j++) {
			ifs >> X1[j] >> Y1[j] >> X2[j] >> Y2[j];
		}
		ofs << "Case #" << i << ": " << gcj.solve(R, X1, X2, Y1, Y2) << endl;
	}
}

//Powered by NTL-5.5.2 (http://www.shoup.net/ntl/)