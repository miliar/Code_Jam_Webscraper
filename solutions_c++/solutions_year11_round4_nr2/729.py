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
#define M 12

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
	s32 m[M][M];
	char c[M];
	FOR (tt,0,num_of_trial) {
		s32 R, C, D;
		cin >> R >> C >> D;
		FOR (i,0,R) {
			cin >> c;
			FOR (j,0,C) m[i][j] = c[j]-'0'+D;
		}
		bool ok=false;
		cout << "Case #" << tt+1 << ": ";
		for (s32 k=min(C,R); k>=3; k--) {
			for (s32 x=0; x<=R-k; x++) {
				for (s32 y=0; y<=C-k; y++) {
					double gx = 0, gy = 0;
					double cx = x + 0.5*k, cy = y+0.5*k;
					for (s32 i=0; i<k; i++) {
						for (s32 j=0; j<k; j++) {
							if (i==0)
								if (j==0 || j==k-1) continue;
							if (i==k-1)
								if (j==0 || j==k-1) continue;
							gx += (x+i+0.5-cx) * m[x+i][y+j];
							gy += (y+j+0.5-cy) * m[x+i][y+j];
						}
					}
					if (fabs(gx)<1.0e-6 && fabs(gy)<1.0e-6) {
						cout << k << endl;
						ok = true;
						goto fin;
					}
				}
			}
		}
fin:
		if (!ok) cout << "IMPOSSIBLE" << endl;
	}



	return 0;
}
