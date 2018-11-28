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

	s32 t, b, o, n, p, pb, po;
	char c;
	cin >> t;
	FOR (tt,0,t) {
		s64 a = 0;
		cin >> n;
		b = o = 1;
		pb = po = 0;
		FOR (i,0,n) {
			cin >> c;
			cin >> p;
			if (c == 'O') {
				a += max(1, abs(p-o)+1-a+po);
				o = p;
				po = a;
			} else {
				a += max(1, abs(p-b)+1-a+pb);
				b = p;
				pb = a;
			}
		}
		cout << "Case #" << tt+1 << ": " << a << endl;
	}



	return 0;
}
