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
#define MIN(a, b)		((a)<(b)?(a):(b))
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

struct R {
	u64 a, b;
};

s32 C;

u32 Next(u64 a, u64 b) {
	if (a*C >=b) return 0;
	u64 m = (u64)sqrt((double)b * a);
	if (b-a==2) {
		if (C==2) return 1;
		else return 0;
	}
	u32 l1 = Next(a, m);
	u32 l2 = Next(m, b);
	u32 r1 = Next(a, m+1);
	u32 r2 = Next(m+1, b);
	return MIN( MAX(l1, l2), MAX(r1, r2) ) + 1;
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

	u64 t, L, P;
	cin >> t;
	FOR (tt,1,t) {
		cin >> L >> P >> C;
		u32  ans = Next(L, P);

		cout << "Case #" << tt << ": ";
		cout << ans;
		cout << endl;

	}
	return 0;
}
