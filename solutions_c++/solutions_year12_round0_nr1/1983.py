#include <iostream>
#include <fstream>
#include <sstream>
#include <iomanip>
#include <algorithm>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cassert>
#include <cmath>

using namespace std;
const int inf = INT_MAX / 4;
int n_case;
int trans[256];
int mark[26];
char googlerese[101];

void solve(void)
{
	int i, j, k;

	const char *en[3];
	const char *un[3];
	en[0] = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	en[1] = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	en[2] = "de kr kd eoya kw aej tysr re ujdr lkgc jv";

	un[0] = "our language is impossible to understand";
	un[1] = "there are twenty six factorial possibilities";
	un[2] = "so it is okay if you want to just give up";


	for (i = 0; i < 3; i++) {
		const char *pe = en[i];
		const char *pu = un[i];
		while (*pe && *pu)
			trans[*pe++] = *pu++;
	}

	trans['z'] = 'q';

	for (i = 'a'; i <= 'z'; i++)
		mark[trans[i] - 'a'] = 1;

	for (i = 0; i < 26; i++) {
		if (!mark[i]) {
			trans['q'] = 'a' + i;
			break;
		}
	}
		
	// for (i = 'a'; i <= 'z'; i++)
	// 	cout << char(i) << " " << char(trans[i]) << endl;

	cin >> n_case;
	cin.ignore();
	for (i = 0; i < n_case; i++) {
		cin.getline(googlerese, 101);
		
		char *p = googlerese;
		j = 0;
		while (*p)
			googlerese[j++] = char(trans[*p++]);
		googlerese[j] = '\0';
		cout << "Case #" << i + 1 << ": " << googlerese << endl;
	}
}

int main()
{
	solve();
	return 0;
}
