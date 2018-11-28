#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <numeric>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;

#define eps 1e-10
#define inf 0x3f3f3f3f

#define console cout
#define dbg(x) console << #x << " == " << x << endl
#define print(x) console << x << endl

char c[101][101];
int N;
double wp[101], owp[101], oowp[101];
int read(){
	scanf("%d", &N);
	for(int i = 0; i < N; i++)scanf("%s", c[i]);
	return 1;
}
void process(){
	for(int i = 0; i < N; i++){
		wp[i] = 0.0;
		int num = 0;
		for(int j = 0; j < N; j++){
			if(c[i][j] != '.'){
				num++;
				wp[i] += c[i][j] == '1';
			}
		}
		wp[i] /= num;
	}
	for(int i = 0; i < N; i++){
		vector<double> perc;
		for(int j = 0; j < N; j++)if(c[i][j] != '.'){
			double dd = 0.0;
			int p = 0;
			for(int k = 0; k < N; k++)if(i-k && c[j][k] != '.'){
				p++;
				dd += c[j][k] == '1';
			}
			dd /= p;
			perc.push_back(dd);
		}
		owp[i] = 0;
		for(int j = 0; j < perc.size(); j++){
			owp[i] += perc[j];
		}
		owp[i] /= perc.size();
	}
	for(int i = 0; i < N; i++){
		oowp[i] = 0.0;
		int pp = 0;
		for(int j = 0; j < N; j++)if(c[i][j] != '.'){
			pp++;
			oowp[i] += owp[j];
		}
		oowp[i] /= pp;
	}
	for(int i = 0; i < N; i++){
		double answ = 0.0;
		answ = 0.25*wp[i] + 0.50*owp[i] + 0.25*oowp[i];
		printf("%.10lf\n", answ);
	}
}

// BEGIN CUT HERE
int main() {
//freopen("out.txt","w",stdout);
//freopen("out.txt","w",stderr);
	int casos;
	scanf("%d", &casos);
	for(int i = 1; i <= casos && read(); i++){
		printf("Case #%d:\n", i);
		process();
	}
	return 0;
}
// END CUT HERE 
