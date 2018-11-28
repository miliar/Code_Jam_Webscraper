#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;

int n,N;

#define SMALL
//#define LARGE
int main() {
//	freopen("A.in", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif

	int c,tt;
//	string in[3],out[3];
	char mp[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q' };

	cin >> N;
	cin.ignore();
//	for (int i = 0; i < 3; ++i) {
//		getline(cin, in[i]);
//
//	}
//	for (int i = 0; i < 3; ++i) {
//			getline(cin, out[i]);
//			out[i] = out[i].substr(9);
//		}
//
//	for (int i = 'a'; i <= 'z'; ++i) {
//		mp[i] = '0';
//	}
//	for (int i = 0; i < 3; ++i) {
//		for (int j = 0; j < in[i].size(); ++j) {
//			mp[in[i][j]] = out[i][j];
//		}
//	}
//	cout << "{";
//	for (int i = 'a'; i <= 'z'; ++i) {
//		cout <<"'" <<(char)mp[i]<<"', ";
//	}
//	cout << "};\n";
	string line;
	for(int nn = 1 ; nn <= N ; nn++ ) {
		getline(cin, line);
		for (int i = 0; i < line.size(); ++i) {
			if(line[i] >= 'a' && line[i] <= 'z')
				line[i] = mp[(int)(line[i]-'a')];
		}
		printf("Case #%d: %s\n", nn, line.c_str());
	}
	return 0;
}
