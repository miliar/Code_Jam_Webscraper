#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>

#define INF_MAX 2147483647
#define INF_MIN -2147483648
#define INF (1 << 30)
#define pi acos(-1.0)
#define SIZE 1000000
#define LL long long
#define vi vector<int>
#define vs vector<string>
#define vc vector<char>
#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define ms(x, a) memset((x), (a), sizeof(x))
#define For(i, a, b) for(int i=(a); i<(b); i++)
#define Fors(i, sz) for(size_t i=0; i<sz.size(); i++)

using namespace std;


int main()
{
	#ifndef ONLINE_JUDGE
		freopen("A-small-attempt2.in", "r", stdin);
		freopen("a.out", "w", stdout);
	#endif

	int i, j, k, n, tc;
	string str;

	char ch[30] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	map<char, char> m;
	for(char c='a', i=0; c<='z'; c++,i++) m[c] = ch[i];

	cin >> tc;
	getline(cin, str);
	For(cn, 1, tc+1)
	{
		getline(cin, str);

		cout << "Case #" << cn << ": ";
		Fors(i, str)
		{
			if(isspace(str[i])) cout << ' ';
			else cout << m[str[i]];
		}
		cout << endl;
	}

	return 0;
}
