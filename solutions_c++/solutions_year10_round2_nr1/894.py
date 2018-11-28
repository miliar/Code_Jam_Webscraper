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

struct D {
	string s;
	vector<D> v;
};

string s;
D root;

D * Find(D &d, string s) {
	for (vector<D>::size_type i=0; i<d.v.size(); i++) {
		if (d.v[i].s == s) return &(d.v[i]);
	}
	return NULL;
}

u32 Insert() {
	string::size_type i=1, j;
	u32 ret = 0;
	D * d = &root;
	while (true) {
		 j = s.find_first_of('/', i);
		 string r = s.substr(i, j-i);
		 D * p = Find(*d, r);
		 if (p == NULL) {
			 D d_new;
			 d_new.s = r;
			 d->v.push_back(d_new);
			 d = &(d->v.back());
			ret ++;
		 } else {
			 d = p;
		 }
		 if (j == string::npos) break;		
		 i = j+1;
	}
	return ret;
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

	s32 t, N, M;
	char c[1000];
	cin >> t;
	FOR (tt,1,t) {
		cin >> N >> M;
		u32 a = 0;
		FOR (nn,1,N) {
			cin >> c;
			s = c;
			Insert();
		}
		FOR (mm,1,M) {
			cin >> c;
			s = c;
			a += Insert();
		}
		cout << "Case #" << tt << ": ";
		cout << a;
		cout << endl;

		root.s.clear();
		root.v.clear();

	}
	return 0;
}
