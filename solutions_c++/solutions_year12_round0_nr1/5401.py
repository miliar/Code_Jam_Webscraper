#include <iostream>
#include <string>
#include <string.h>
#include <algorithm>
#include <vector>
#include <queue>
#include <ctime>
#include <cmath>
#include <stdio.h>
#include <set>
#include <map>
#include <stack>
#include <fstream>
#include <list>

#define SZ(a) (int(a.size()))
#define MEM(a, val) memset(a, val, sizeof(a))

typedef unsigned long long ULL;
typedef long long LL;
typedef long double dbl;

using namespace std;

string sg[3];
string so[3];
char F[256];

const char G[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};

int main()
{
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
	/*MEM(F, '?');
	for (int i = 0; i < 3; ++i)
	{
		getline(cin, sg[i]);
	}
	for (int i = 0; i < 3; ++i)
	{
		getline(cin, so[i]);
	}
	F['z'] = 'q';
	F['q'] = 'z';
	for (int i = 0; i < 3; ++i) {
		for (int j = 0; j < SZ(sg[i]); ++j) {
			if (!(F[sg[i][j]] == '?' || F[sg[i][j]] == so[i][j]))
				cout << "false" << endl;
			F[sg[i][j]] = so[i][j];
		}
	}
	
	for (char ch = 'a'; ch <= 'z' ; ++ch) {
		cout << ", '" << F[ch] << "'";
	}*/

	string s;
	int T;
	cin >> T;
	getline(cin, s);
	for (int I = 1; I <= T; ++I) {
		getline(cin, s);
		for (int i = 0; i < SZ(s); ++i) {
			if (s[i] != ' ')
				s[i] = G[s[i] - 'a'];
		}
		cout << "Case #" << I << ": " ; 
		cout << s << endl;
	}
	return 0;
}