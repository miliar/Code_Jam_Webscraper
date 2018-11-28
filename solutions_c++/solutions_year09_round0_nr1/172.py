#include <iostream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <fstream>
#include <math.h>
#include <limits>
#include <set>
#include <map>
#include <sstream>
#include <stdio.h>
#include <time.h>
#include <memory.h>
using namespace std;

#define ALL(ar)       (ar).begin(),(ar).end()
#define SZ(a)         int((a).size())
#define MP(a,b)       make_pair(a,b)
#define INF           0x7f7f7f7f
typedef long long     LL;
typedef vector<int>   VI;
typedef pair<int,int> II;

/* @date    03.09.2009
 * @idea    Iterate dictionary every time and check word by word
 */

int L, D, N;
vector<string> dict;
bool patt[15][26];

void fillPattern (string& _s) {
	memset (patt, 0, sizeof (patt));
	for (int i = 0, token = 0; i < SZ(_s); i++, token++) {
		if (_s[i] == '(')
			while (_s[++i] != ')')
				patt[token][_s[i]-'a'] = true;
		else
			patt[token][_s[i]-'a'] = true;
	}
}

bool matchPattern (string& _s) {
	for (int i = 0; i < L; i++)
		if (!patt[i][_s[i]-'a']) return false;
	return true;
}

int main()
{
	freopen("in.in", "rt", stdin);
	freopen("out.out", "wt+", stdout);

	scanf ("%d %d %d\n", &L, &D, &N);
	string s;
	for (int i = 0; i < D; i++) {
		cin >> s;
		dict.push_back (s);
	}
	
	for (int tc = 0; tc < N; tc++)
	{
		int all = 0;
		cin >> s;
		fillPattern (s);
		for (int i = 0; i < D; i++)
			all += matchPattern (dict[i]);
		printf ("Case #%d: %d\n", tc+1, all);
	}

	return 0;
}