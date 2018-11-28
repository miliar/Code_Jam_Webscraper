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
#define MIN3(a, b, c)	(MIN((a),MIN((b),(c))))
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
#define N 520

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

	s32 t, m, n;
	char c[1000];
	u16 ** b = new u16*[N];
	FOR (i,0,N-1) b[i] = new u16[N];
	u16 ** d = new u16*[N];
	FOR (i,0,N-1) d[i] = new u16[N];
	u16 a[N];
	cin >> t;
	FOR (tt,1,t) {
		cin >> m >> n;
		FOR (mm,0,m-1) {
			cin >> c;
			FOR (i,0,n/4-1) {
				u32 k;
				if (c[i]>='A') k=c[i]-'A'+10;
				else k= c[i]-'0';
				FOR (j,1,4) {
					b[mm][4*(i+1)-j] = k%2;
					k/=2;
				}
			}
		}
		FOR (i,0,n-1) a[i] = 0;
		FOR (i,0,n-1) d[0][i] = 1;
		FOR (i,0,m-1) d[i][0] = 1;
		s32 l = n* m;
		while (l > 0) {
			u32 md=1, mi=0, mj=0;
			FOR (i,1,m-1) {
				FOR (j,1,n-1) {
					if ((b[i][j]==1 && b[i-1][j]==0 && b[i][j-1]==0 && b[i-1][j-1]==1) ||
						(b[i][j]==0 && b[i-1][j]==1 && b[i][j-1]==1 && b[i-1][j-1]==0)) {
						d[i][j] = MIN3(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1;
						if (md < d[i][j]) {
							md = d[i][j];
							mi = i;
							mj = j;
						}
					} else {
						d[i][j] = 1;
					}
				}
			}
			a[md] ++;
			FOR (i,mi-md+1,mi) FOR (j,mj-md+1,mj) {
				b[i][j] = 2;
			}
			l -= md*md;
		}

		u32 ki = 0;
		FOR (i,0,n-1) if (a[i] > 0) ki ++;

		cout << "Case #" << tt << ": ";
		cout << ki;
		cout << endl;
		for (s32 i=n-1; i>=0; i--) {
			if (a[i]>0) cout << i << " " << a[i] << endl;
		}
	}
	FOR (i,0,N-1) {
		delete [] b[i];
		delete [] d[i];
	}
	delete[] b;
    delete[] d;
	return 0;
}
