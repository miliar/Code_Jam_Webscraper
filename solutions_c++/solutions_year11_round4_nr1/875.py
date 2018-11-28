#include <stdio.h>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <map>
#include <algorithm>
#include "windows.h"
//#include "../../gmp_int.h"
//#include "../../common.h"
#define MAX(a, b)		((a)>(b)?(a):(b))
#define MAX3(a, b, c)	(MAX((a),MAX((b),(c))))
#define FOR(a,b,c)		for (s32(a)=(b);(a)<(s32)(c);(a)++)
#define BL				{char bl[10];cin.getline(bl, 10);}
#define GL(c)			cin.getline(c, sizeof(c))
typedef char					s8;
typedef unsigned char			u8;
typedef short					s16;
typedef unsigned short			u16;
typedef int						s32;
typedef unsigned int			u32;
typedef long long int			s64;
typedef unsigned long long int	u64;
using namespace std;

ifstream test_input;
#define cin test_input

struct P {
	s32 w, l;
};

bool operator < (const P &p1, const P &p2) {
	return p1.w < p2.w;
}

int main(int argc, char* argv[])
{
	cout.precision(15);
	if (argc!=2) {
		cout << "Need input file name." << endl;
		return 0;
	}
	test_input.open(argv[1]);
	if (test_input.fail()) {
		cout << "Cannot open input file " << argv[1] << "." << endl;
		return 0;
	}

	s32 num_of_trial;
	cin >> num_of_trial;
	FOR (tt,0,num_of_trial) {
		s32 X, S, R, N;
		double t;
		s32 B, E;
		cin >> X >> S >> R >> t >> N;
		vector<P> u;
		P p;
		s32 x = X;
		FOR (i,0,N) {
			cin >> B >> E >> p.w;
			p.l = E-B;
			u.push_back(p);
			x -= p.l;
		}
		if (x > 0) {
			p.l = x;
			p.w = 0;
			u.push_back(p);
		}
		sort(u.begin(), u.end());
		double a=0;
		FOR (i,0,u.size()) {
			double a0 = min((double)u[i].l/(u[i].w+R), t);
			a += a0 + (u[i].l-(double)(u[i].w+R)*a0) / (u[i].w+S);
			t -= a0;
		}
		cout << "Case #" << tt+1 << ": " << a << endl;
	}

	return 0;
}
