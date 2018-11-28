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
using namespace std;
static const double EPS = 1e-5;
typedef long long ll;

class GCJ {
public:
	string solve(int n, int k) {
		string result;
		
		if(k%(1<<n)==(1<<n)-1) result.assign("ON");
		else result.assign("OFF");

		return result;
	}
};

int main() {
	string prb[12];
	ofstream ofs("output.txt");
	string filename;
	char key;
	int n;
	int N, K;
	GCJ gcj;

	for(int i=0; i<12; i++) {
		prb[i].push_back('A'+i/2);
		prb[i].push_back('-');
		if(i%2) prb[i]+="large";
		else prb[i]+="small";
		prb[i]+=".in.txt";
		cout << (char)('a'+i) << ". " << prb[i] << endl;
	}
	do {
		cout << "Choose the input file." << endl;
		cin >> key;
	} while(key-'a'<0 || key-'a'>=12);
	filename=prb[key-'a'];
	cout << "Filename is " << filename << endl;
	ifstream ifs(filename.c_str());

	ifs >> n; ifs.ignore();
	for(int i=1; i<=n; i++) {
		ifs >> N >> K;
		ofs << "Case #" << i << ": " << gcj.solve(N, K) << endl;
	}
}
