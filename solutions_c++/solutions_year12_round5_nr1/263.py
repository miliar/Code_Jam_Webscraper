#define _CRT_SECURE_NO_WARNINGS
#pragma comment (linker, "/STACK:268435456")
#include <cstdio>
#include <cstring>
#include <math.h>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <cctype>
#include <bitset>
#include <sstream>
#include <set>
#include <map>

using namespace std;
template <class T> T sqr(T a) { return a * a; }

struct ss
{
	int a, b, id;

	double getp() const
	{
		if (b == 0)
			return 0;
		return 1.0 / (1 - b / 100.0) * a;
	}

	bool operator< (const ss &s) const
	{
		if (fabs(getp() - s.getp()) > 1e-6)
			return getp() > s.getp();
		return id < s.id;
	}
};

ss s[1010];

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int testNum;
	cin >> testNum;
	int n;
	for (int testCount = 0; testCount < testNum; testCount++)
	{
		cin >> n;
		for (int i = 0; i < n; i++)
			cin >> s[i].a;
		for (int i = 0; i < n; i++)
			cin >> s[i].b, s[i].id = i;
		sort(s, s + n);
		cout << "Case #" << testCount + 1 << ": ";
		for (int i = 0; i < n; i++)
			cout << s[i].id << " ";
		cout << endl;
	}
	return 0;
}