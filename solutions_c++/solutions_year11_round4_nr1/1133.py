
#include <stdio.h>
#include <time.h>

#include <vector>
#include <list>
#include <set>
#include <string>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <iomanip>
#include <sstream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <stack>
#include <numeric>
#include <complex>

using namespace std;


typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<LL> VL;
#define FORE(it, c, T) for(T::iterator it = c.begin(); it != c.end(); it++)
#define FORI(i, n) for(int i = 0; i < (n); i++)
#define FORIS(i, s, n) for(int i = (s); i < (n); i++)
#define CLEAR(a, n) memset(a, n, sizeof(a))
#define PB(n) push_back(n)
#define SZ(c) int((c).size())
#define ALL(c) (c).begin(), (c).end()

#define NUM 101

int C, N;
double X, S, R, T;
typedef pair<double, double> PD;
PD w[10000];

int main(int argc, char* argv[])
{
#define TASK_NAME(file) "A"file
#define FOLDER(file) "c:\\Projects\\coding\\cj\\2011\\Round2\\"TASK_NAME("")"\\"file
//	ifstream in(FOLDER(TASK_NAME("-test.in")));
//	ofstream out(FOLDER(TASK_NAME("-test.out")));
//	ifstream in(FOLDER(TASK_NAME("-small-attempt0.in")));
//	ofstream out(FOLDER(TASK_NAME("-small-attempt0.out")));
	ifstream in(FOLDER(TASK_NAME("-large.in")));
	ofstream out(FOLDER(TASK_NAME("-large.out")));

	in >> C;
	FORI(ncase, C) {
		in >> X >> S >> R >> T >> N;
		double D = 0;
		FORI(i, N) {
			double B, E, W;
			in >> B >> E >> W;
			w[i] = PD(W, E-B);
			D += E-B;
		}
		w[N] = PD(0, X-D);
		sort(w, w+N+1);
		double res = 0;
		FORI(i, N+1) {
			if((w[i].first+R)*T >= w[i].second) {
				res += w[i].second / ((w[i].first+R));
				T -= w[i].second / ((w[i].first+R));
			} else {
				double rd = (w[i].first+R)*T;
				double sd = w[i].second - (w[i].first+R)*T;
				res += rd / (w[i].first+R) + sd / (w[i].first+S);
				T = 0;
			}
		}

		

		out << "Case #" << (ncase+1) << ": " << fixed << setprecision(9) << res << endl;
	}
	return 0;
}
