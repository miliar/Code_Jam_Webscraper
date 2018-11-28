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

struct P {
	u32 x, y;
};

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

	s32 t, n;
	cin >> t;
	FOR (tt,1,t) {
		vector<P> v;
		cin >> n;
		FOR (nn,1,n) {
			P p;
			cin >> p.x >> p.y;
			v.push_back(p);
		}
		u32 a = 0;
		FOR (i,0,n-1) FOR (j,i+1,n-1) {
			if ( (v[i].x>v[j].x && v[i].y<v[j].y) || (v[i].x<v[j].x && v[i].y>v[j].y)) {
				a ++;
			}
		}
		cout << "Case #" << tt << ": ";
		cout << a;
		cout << endl;
	}



	return 0;
}
