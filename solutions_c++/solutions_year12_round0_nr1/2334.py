#pragma comment(linker, "/STACK:25600000")
#define _CRT_NO_WARNINGS
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
#include <cstring>
#include <map>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
#define REP(i, n) for(int i=0; i<n; i++)
#define FOR(i, x, y) for(int i=x; i<=y; i++)
#define RFOR(i, x, y) for(int i=x; i>=y; i--)
#define ALL(a) (a).begin(),(a).end()
#define pb push_back
#define PII pair<int, int>
const double pi=acos(-1.0);

int main()
{
	freopen("a-input.txt", "r", stdin);
	freopen("a-output.txt", "w", stdout);

	map<char, char> mp;
    string words = "y n f i c w l b k u o m x s e v z p d r j g a t h a q";
	string translation = "a b c d e f g h i j k l m n o p q r s t u v y w x y z";

	REP(i, words.size())
			mp[words[i]] = translation[i];

	int tests;
	cin >> tests;
	string s;
	getline(cin, s);
	FOR(TEST, 1, tests)
	{
		string s;
		getline(cin, s);
		printf("Case #%d: ", TEST);
		REP(i, s.size())
			cout << mp[s[i]];
		cout << endl;
	}

}