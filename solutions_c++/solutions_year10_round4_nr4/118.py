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
#define MAX(a, b)		((a)>(b)?(a):(b))
#define MAX3(a, b, c)	(MAX((a),MAX((b),(c))))
#define FOR(a,b,c)		for (s32(a)=(b);(a)<=(s32)(c);(a)++)
#define BL				{char bl[10];cin.getline(bl, 10);}
#define GL(c)			cin.getline(c, sizeof(c))
#define THREAD_LOW BOOL thread_low = SetThreadPriority(GetCurrentThread(), THREAD_PRIORITY_LOWEST)
typedef char					s8;
typedef unsigned char			u8;
typedef short					s16;
typedef unsigned short			u16;
typedef int						s32;
typedef unsigned int			u32;
typedef long long int			s64;
typedef unsigned long long int	u64;
using namespace std;

THREAD_LOW;
ifstream test_input;
#define cin test_input
#define PI 3.1415926535897932384626433832795

struct P {
	double x, y;
};

double Len(P &p1, P &p2) {
	return sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y));
}

int main(int argc, char* argv[])
{
	if (argc!=2) {
		cout << "Need input file name." << endl;
		return 0;
	}
	test_input.open(argv[1]);
	if (test_input.fail()) {
		cout << "Cannot open input file " << argv[1] << "." << endl;
		return 0;
	}

	s32 T, N, M;
	cin >> T;
	FOR (tt,1,T) {
		vector<P> v, u;
		P p;
		cin >> N >> M;
		FOR (i,1,N) {
			cin >> p.x >> p.y;
			v.push_back(p);
		}
		FOR (i,1,M) {
			cin >> p.x >> p.y;
			u.push_back(p);
		}
		printf("Case #%d:", tt);
		FOR (i,0,M-1) {
			double d = 0.0;
			FOR (j,0,1) {
				u32 k=j==0?1:0;
				double a0 = Len(v[j], u[i]);
				double a1 = Len(v[k], u[i]);
				double a01 = Len(v[j], v[k]);
				double c = (a0*a0+a01*a01-a1*a1) / (2.0*a0*a01);
				double th = 2.0*acos(c);
				double b0 = a0*a0*th/(2.0) - 0.5*a0*a0*sin(th);
				d += b0;
			}
			printf(" %.7lf", d);
		}
		printf("\n");
	}



	return 0;
}
