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

#define M 10001

void Smart()
{
	s64 inf = 1000000000000LL;
	s64 N, d[M], l[M], m[M], D;
	cin >> N;
	FOR (j,0,N) cin >> d[j] >> l[j];
	FOR (j,0,N) m[j] = inf;
	cin >> D;
	
	s64 x=d[0], k=d[0];
	d[N] = D;
	m[N] = 0;
	for (s32 i=N; i>=0; i--) {
		for (s32 j=i-1; j>=0; j--) {
			if (d[j]>d[i]-m[i]) continue;
			if (d[j]+l[j]>=d[i]) {
				m[j] = min(m[j], d[i]-d[j]);
			}
		}
	}
	if (m[0]!=inf && m[0]<=d[0]) cout << "YES";
	else cout << "NO";
}

void Naive()
{
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

	s32 num_of_trial;
	cin >> num_of_trial;
	FOR (tt,0,num_of_trial) {
		cout << "Case #" << tt+1 << ": ";
		Smart();
		cout << endl;
	}

	return 0;
}
