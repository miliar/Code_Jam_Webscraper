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

#define N 200
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

	s32 C, R, x1,y1,x2,y2;
	cin >> C;
	FOR (tt,1,C) {
		cin >> R;
		bool g[N][N], gn[N][N];
		memset(g,0,N*N);
		FOR (rr,1,R) {
			cin >> x1>>y1>>x2>>y2;
			FOR (x,x1,x2) FOR (y,y1,y2) g[x][y]=true;
		}
		u32 a = 0;
		while (true) {
			bool dead = true;
			FOR (x,1,N-1) FOR (y,1,N-1) {
				if (g[x][y]) {
					dead=false;
					break;
				}
			}
			if (dead) break;
			memset(gn,0,N*N);
			FOR (x,1,N-1) FOR (y,1,N-1) {
				if (g[x][y]) {
					if (!g[x-1][y] && !g[x][y-1]) gn[x][y]=false;
					else gn[x][y]=true;
				}
				if (!g[x][y]) {
					if (g[x-1][y] && g[x][y-1]) gn[x][y]=true;
					else gn[x][y]=false;
				}
			}
			memcpy(g, gn, N*N);
			a ++;
		}

		



		cout << "Case #" << tt << ": ";
		cout << a;
		cout << endl;
	}



	return 0;
}
