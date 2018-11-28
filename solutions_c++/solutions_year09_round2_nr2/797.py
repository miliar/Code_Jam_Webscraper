#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <string>
#include <utility>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cassert>

#define INF INT_MAX / 2
#define X first
#define Y second
#define ft first
#define sc second
#define all(a) (a).begin(), (a).end()
#define pb push_back
#define mp(a, b) make_pair((a), (b))
#define forn(i, n) for(int i = 0; i < int(n); i++)
#define forl(i, n) for(int i = 1; i <= int(n); i++)
#define sqr(a) ((a) * (a))
#define PI 3.1415926535897932384626433832795
#define NMAX 1000

using namespace std;

typedef pair<int, int> pt;
typedef unsigned char byte;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

	int t;
	cin >> t;

	forn(i, t)
	{
		string n;
		cin >> n;

		string tmp(n);
		if(!next_permutation(all(tmp)))
			n = "0" + n;

		next_permutation(all(n));
		printf("Case #%d: ", i + 1);
		cout << n << endl;
	}

    return 0;
}