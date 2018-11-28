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
#include "../../common.h"
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
#define M 101

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
	char c[M][M];
	double WP[M], OWP[M], OOWP[M];
	s32 win[M], lose[M];

	FOR (tt,0,t) {
		s32 N;
		cin >> N;
		FOR (i,0,N) cin >> c[i];
		FOR (i,0,N) {
			win[i]=0; lose[i]=0;
			FOR (j,0,N) {
				if (c[i][j]=='1') {
					win[i] ++;
				}
				if (c[i][j]=='0') {
					lose[i] ++;
				}
			}
			WP[i] = (double)win[i] / (win[i]+lose[i]);
		}
		FOR (i,0,N) {
			OWP[i]=0;
			FOR (j,0,N) {
				if (c[i][j]=='.') continue;
				s32 win2=0, lose2=0;
				FOR (k,0,N) {
					if (i==k) continue;
					if (c[j][k]=='1') win2 ++;
					if (c[j][k]=='0') lose2 ++;
				}
				OWP[i] += (double)win2 / (win2+lose2);

			}
			OWP[i] /= (win[i]+lose[i]);
		}
		FOR (i,0,N) {
			OOWP[i]=0;
			FOR (j,0,N) {
				if (c[i][j]=='.') continue;
				OOWP[i] += OWP[j];
			}
			OOWP[i] /= (win[i]+lose[i]);
		}
		cout << "Case #" << tt+1 << ":" << endl;
		FOR (i,0,N) {
			cout << 0.25*WP[i] + 0.50*OWP[i] + 0.25*OOWP[i] << endl;
		}
	}



	return 0;
}
