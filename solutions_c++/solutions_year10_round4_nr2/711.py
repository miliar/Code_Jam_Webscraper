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

u32 a;
u32 M[10000];

void Next(u32 i, u32 j, s32 p) {
	bool d = false;
	FOR (k,i,j) {
		if (M[k]<=p) {
			d = true;
			break;
		}
	}
	if (d) {
		a ++;
		if (p>0) {
			Next(i, (i+j-1)/2, p-1);
			Next((i+j-1)/2+1, j, p-1);
		}
	}
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

	s32 T, P;
	cin >> T;
	FOR (tt,1,T) {
		cin >> P;
		u32 m=1<<P;
		FOR (i,0,m-1) cin >> M[i];
		for (s32 i=m/2; i>0; i/=2) {
			for (s32 j=0; j<i; j++) {
				u32 tmp;
				cin >> tmp;
			}
		}
		a=0;
		Next(0,m-1,P-1);

		cout << "Case #" << tt << ": ";
		cout << a;
		cout << endl;
	}



	return 0;
}
