#include <memory.h>
#include <iostream>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <bitset>
#include <deque>
#include <map>
#include <stack>
#include <sstream>

using namespace std;

typedef vector<int> vi;
typedef long long ll;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef vector<vi> vvi;

#define mp make_pair
#define pb push_back
#define all(x) (x).begin(), (x).end()
#define sz(x) ((x).size())
#define sqr(x) ((x)*(x))
#define slen(x) ((x).length())

template<class T> T abs(T x) { return x > 0 ? x : -x;}

int n, m;

int main()
{
	int i, j, t;
	char s[100];
	int dig[256];
	int p;
	int toSign[38];
	
//	freopen("input", "r", stdin);
//	freopen("output", "w", stdout);
	cin >> t;
	gets(s);
	string tmp;
	toSign[0] = 1;
	toSign[1] = 0;
	for (i = 2; i < 38; i++)
		toSign[i] = i;
	int diff = 0;
	for (i = 0; i < t; i++)
	{
		gets(s);
		tmp = s;
		if (tmp.length() == 1)
		{
			cout << "Case #" << i + 1 << ": 1" << endl;
			continue;
		}
		memset(dig, 0, sizeof(dig));
		diff = 0;
		for (j = 0; j < tmp.length(); j++)
			if (dig[tmp[j]] == 0)
			{
				diff++;
				dig[tmp[j]] = 1;
			}
		if (diff == 1)
			diff++;
		memset(dig, 255, sizeof(dig));

		p = 0;
		ll result = 0;
		for (j = 0; j < tmp.length(); j++)
		{
			if (dig[tmp[j]] == -1)
				dig[tmp[j]] = toSign[p++];				
//			cout << dig[tmp[j]];
			result = result * diff + dig[tmp[j]];
		}
		cout << "Case #" << i + 1 << ": " << result << endl;
	}
	return 0;
}
