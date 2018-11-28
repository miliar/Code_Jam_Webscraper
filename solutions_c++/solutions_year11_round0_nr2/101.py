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

#define N 110
struct P {
	char a, b, c;
};

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
		s32 c, d, n;
		char s[N];
		vector<P> v, u;
		string w;
		cin >> c;
		FOR (i,0,c) {
			cin >> s;
			P p = { s[0], s[1], s[2] };
			v.push_back(p);
		}
		cin >> d;
		FOR (i,0,d) {
			cin >> s;
			P p = { s[0], s[1], '0' };
			u.push_back(p);
		}
		cin >> n;
		cin >> s;
		FOR (i,0,n) {
			if (w.empty()) {
				w += s[i];
				continue;
			}
			// Check combine
			bool combine = false;
			FOR (j,0,v.size()) {
				if ((s[i]==v[j].a && w[w.size()-1]==v[j].b) || 
					(s[i]==v[j].b && w[w.size()-1]==v[j].a)) {
					w.erase(w.size()-1);
					w += v[j].c;
					combine = true;
					break;
				}
			}
			if (combine) continue;
			// Check oppose
			bool oppose = false;
			FOR (j,0,u.size()) {
				if ((s[i]==u[j].a && w.find(u[j].b)!=string::npos) ||
					(s[i]==u[j].b && w.find(u[j].a)!=string::npos)) {
					oppose = true;
					w.clear();
					break;
				}
			}
			if (!oppose) w += s[i];
		}
		cout << "Case #" << tt+1 << ": [";
		FOR (i,0,w.size()) {
			cout << w[i];
			if (i!=w.size()-1) cout << ", ";
		}
		cout << "]" << endl;
	}

	return 0;
}
