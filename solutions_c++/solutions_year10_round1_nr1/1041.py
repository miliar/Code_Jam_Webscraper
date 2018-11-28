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

#define M 100
char b[M+1][M+1], d[M+1][M+1];
s32 t, N, K;

void Print() {
	FOR (i,0,N-1) {
		cout << d[i] << endl;
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

	cin >> t;
	FOR (tt,1,t) {
		cin >> N >> K;
		char c[M];
		FOR (i,0,N-1) {
			cin >> c;
			FOR (j,0,N-1) {
				b[i][j] = c[j];
				d[i][j] = '.';
			}
			b[i][N] = d[i][N] = '\0';
		}
		for (s32 i=N-1; i>=0; i--) {
			u32 k = N-1;
			for (s32 j=N-1; j>=0; j--) {
				if(b[i][j]!='.') {
					d[i][k] = b[i][j];
					k --;
				}
			}
		}
		//Print();
		bool blue = false, red = false;
		FOR (i,0,N-1) {
			FOR (j,0,N-1) {
				if (d[i][j]!='.') {
					u32 h = 1, v = 1, g = 1, w = 1, f = 1;
					FOR (k,j+1,N-1) {
						if (d[i][k] == d[i][j]) h ++;
						else break;
					}
					FOR (k,i+1,N-1) {
						if (d[k][j] == d[i][j]) v ++;
						else break;
					}
					FOR (k,1,N-1) {
						if (i+k >= N || j+k >= N) break;
						if (d[i+k][j+k] == d[i][j]) g ++;
						else break;
					}
					FOR (k,1,N-1) {
						if (i+k >= N || j-k >= N) break;
						if (d[i+k][j-k] == d[i][j]) w ++;
						else break;
					}
					FOR (k,1,N-1) {
						if (i-k >= N || j+k >= N) break;
						if (d[i-k][j+k] == d[i][j]) f ++;
						else break;
					}
					if (h>=K || v>=K || g>=K || w>=K || f>=K) {
						if (d[i][j] == 'R') red = true;
						else blue = true;
					}
				}
			}
		}
		cout << "Case #" << tt << ": ";
		if (red) {
			if (blue) cout << "Both";
			else cout << "Red";
		} else {
			if (blue) cout << "Blue";
			else cout << "Neither";
		}
		cout << endl;
	}
	return 0;
}
