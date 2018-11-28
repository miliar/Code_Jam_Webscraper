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

#define L 10
struct P {
	s32 i, j;
};

bool Exist(vector<s32> &v, s32 m) {
	FOR (i,0,v.size()) {
		if (v[i]==m) return true;
	}
	return false;
}
s64 Pow(s64 base, s64 exp)
{
	s64 ret = 1;
	for (s64 i = 0; i < exp; i ++) ret *= base;
	return ret;
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

	s32 t;
	cin >> t;
	FOR (tt,0,t) {
		s32 N, M;
		cin >> N >> M;
		P p[L];
		FOR (i,0,M) cin >> p[i].i;
		FOR (i,0,M) cin >> p[i].j;
		vector<vector<s32>> v, v1;
		vector<s32> u;
		FOR (i,1,N+1) u.push_back(i);
		v.push_back(u);
		FOR (i,0,M) {
			FOR (j,0,v.size()) {
				if (Exist(v[j], p[i].i) && Exist(v[j],p[i].j)) {
					bool md = true;
					vector<s32> u0, u1;
					FOR (k,0,v[j].size()) {
						if (md) u0.push_back(v[j][k]);
						else u1.push_back(v[j][k]);
						if (v[j][k]==p[i].i || v[j][k]==p[i].j) {
							if (md) {
								u1.push_back(v[j][k]);
							} else {
								u0.push_back(v[j][k]);
							}
							md = !md;
						}
					}
					v1.push_back(u0);
					v1.push_back(u1);
				} else {
					v1.push_back(v[j]);
				}
			}
			v = v1;
			v1.clear();
		}
		s64 a = N;
		s64 b[L];
		FOR (i,0,v.size()) a = min(a, v[i].size());
		s64 imax = Pow((s64)a, N);
		for (s64 i=0; i<imax; i++) {
			s64 m=i;
			FOR (j,1,N+1) {
				b[j] = (m%a) + 1;
				m/=a;
			}
			bool ok=true;
			FOR (j,0,v.size()) {
				set<s32> s;
				FOR (k,0,v[j].size()) s.insert(b[v[j][k]]);
				if (s.size()!=a) {
					ok=false;
					break;
				}
			}
			if (ok) {
				cout << "Case #" << tt+1 << ": " << a << endl;
				FOR (j,1,N+1) cout << b[j] << " ";
				cout << endl;
				break;
			}
		}
	}



	return 0;
}
