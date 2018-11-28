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
#define MAX(a, b)		((a)>(b)?(a):(b))
#define MAX3(a, b, c)	(MAX((a),MAX((b),(c))))
#define FOR(a,b,c)		for (s32(a)=(b);(a)<=(s32)(c);(a)++)
#define BL				{char bl[10];cin.getline(bl, 10);}
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
#define N 1100

struct P {
	u32 next;
	u32 ride;
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

	u64 t, r, k, n, x;
	cin >> t;
	FOR (tt,1,t) {
		cin >> r >> k >> n;
		vector<u64> v;
		FOR (i,0,n-1) {
			cin >> x;
			v.push_back(x);
		}
		bool b[N];
		P p[N];
		memset(b, 0, N);

		u64 a = 0;
		u32 j = 0;
		FOR (i,0,n-1) {
			while (true) {
				if (a + v[j] > k) break;
				a += v[j];
				if (++j == n) j = 0;
				if (j == i) break;
			}
			p[i].ride = a;
			p[i].next = j;
			a -= v[i];
		}
		
		j = 0;
		u64 c = 0;
		a = 0;
		while (true) {
			if (b[j]) {
				break;
			} else {
				b[j] = true;
				a ++;
				c += p[j].ride;
				j = p[j].next;
			}
		}
		u64 j0 = j;
		j = 0;
		u64 c0 = 0, a0 = 0;
		while (true) {
			if (j == j0) {
				break;
			} else {
				a0 ++;
				c0 += p[j].ride;
				j = p[j].next;
			}
		}
		c -= c0;
		a -= a0;

		u64 ans = c0 + ((r-a0)/a)*c;
		u64 i0 = (r-a0)%a;
		for (u64 i = 0; i < i0; i ++) {
			ans += p[j].ride;
			j = p[j].next;
		}


		cout << "Case #" << tt << ": ";
		cout << ans;
		cout << endl;
	}

	return 0;
}
