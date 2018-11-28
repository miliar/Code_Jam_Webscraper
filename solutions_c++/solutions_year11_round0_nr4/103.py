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

#define N 1001

double Bi(s32 n, s32 m)
{
	if (m<0 || m>n) return 0;
	if (n/2 < m) m = n-m;
	double r = 1.0;
	FOR (i,0,m) {
		r *= n-i;
		r /= i+1;
	}
	return r;
}

double p[N][N];
double q[N], q_new[N];

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

	s32 t;
	cin >> t;

	memset(p,0,sizeof(double)*N*N);
	p[0][0] = 1.0;
	FOR (i,1,N) {
		FOR (j,0,i) {
			p[i][j] = Bi(i, j);
			FOR (k,0,i-j) {
				p[i][j] /= i-k;
			}
			p[i][j] *= p[j][j];
		}
		p[i][i] = 1.0;
		FOR (j,0,i) p[i][i] -= p[i][j];
	}

	FOR (tt,0,t) {
		s32 n, r;
		cin >> n;
		s32 a = n;
		FOR (i,0,n) {
			cin >> r;
			if (r == i+1) a --;
		}
		memset(q,0,sizeof(double)*N);
		q[a] = 1.0;
		double e = 0.0;
		for (s32 k=1; k<1000; k++) {
			memset(q_new,0,sizeof(double)*N);
			FOR (i,1,n+1) {
				FOR (j,0,i+1) {
					q_new[j] += q[i] * p[i][j];
				}
			}
			memcpy(q, q_new, sizeof(double)*N);
			e += k * q[0];
			q[0] = 0.0;
		}				

		cout << "Case #" << tt+1 << ": " << e << endl;
	}



	return 0;
}
