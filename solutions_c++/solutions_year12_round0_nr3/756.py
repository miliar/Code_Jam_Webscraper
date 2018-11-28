
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
typedef set<int> SI;
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

int T, A, B;
int fl[2000005];

int main(int argc, char* argv[])
{
#define TASK_NAME(file) "C"file
#define FOLDER(file) "c:\\Projects\\coding\\cj\\2012\\QualificationRound\\"TASK_NAME("")"\\"file
//	ifstream in(FOLDER(TASK_NAME("-test.in")));
//	ofstream out(FOLDER(TASK_NAME("-test.out")));
//	ifstream in(FOLDER(TASK_NAME("-small-attempt0.in")));
//	ofstream out(FOLDER(TASK_NAME("-small-attempt0.out")));
	ifstream in(FOLDER(TASK_NAME("-large.in")));
	ofstream out(FOLDER(TASK_NAME("-large.out")));

	in >> T;
	FORI(ncase, T) {
		in >> A >> B;
		int k = 0, nn = 1, x = A;
		while(x) {
			k ++;
			nn *= 10;
			x /= 10;
		}
		nn /= 10;
		int res = 0;
		CLEAR(fl, 0);
		FORIS(n, A, B) {
			int s = n;
			int kk = 1;
			if(fl[s]) continue;
			fl[s] = 1;
			FORI(i, k-1) {
				s = s/10 + (s%10)*nn;
				if(s >= A && s <= B && s > n) {
					if(!fl[s]) {
						fl[s] = 1;
						kk++;
					}
				}
			}
			res += kk * (kk-1)/2;
		}
		out << "Case #" << (ncase+1) << ": " << res << endl;
	}
	return 0;
}
