#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <set>
#include <queue>
#include <stack>
#include <string>
#include <map>
#include <deque>

#define PII pair< int, int >
#define VI vector< int >
#define VV vector< vector< int > >
#define VB vector< bool >
#define VS vector< string >
#define VD vector< double >
#define INT64 long long
#define LD long double
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define ULL unsigned long long

using namespace std;

const string tname = "snapper";

int sqr(int a)
{
	return a * a;
}

int main()
{
	freopen((tname+".in").c_str(), "rt", stdin);
	freopen((tname+".out").c_str(), "wt", stdout);

	int T;
	cin >> T;
	int n, k;

	int r;

	for (int i = 0; i < T; i++)
	{
		cin >> n >> k;
		int r = (1 << n) - 1;
		if ((k % (r+1)) == r) cout << "Case #" << i+1 << ": ON" << endl;
		else cout << "Case #" << i+1 << ": OFF" << endl;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
