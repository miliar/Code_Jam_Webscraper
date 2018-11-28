#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
using namespace std;

static bool same(char &old, char z) {
	if (old=='?') {
		old = z;
		return true;
	}
	return old == z || z=='?';
}

static bool symmetric(const vector<string> &v) {
	int n = (int)v.size()-1;
	for (int y=0; 2*y<=n; y++) {
		for (int x=0; 2*x<=n; x++) {
			char value = v[y][x];
			if (!same(value, v[n-y][x]))
				return false;
			if (!same(value, v[y][n-x]))
				return false;
			if (!same(value, v[n-y][n-x]))
				return false;
		}
	}
	return true;
}

int runTest() {
	int k;
	cin >> k;
	vector<string> v(2*k-1);
	string line;

	for (int i=0; i<2*k-1;) {
		getline(cin, line);
		if (line.empty())
			continue;
		for (unsigned int j=0; j<line.size() && line[j]==' '; j++)
			line[j] = '?';
		unsigned int oldSize = (unsigned int)line.size();
		line.resize(2*k-1);
		for (unsigned int j=oldSize; j<line.size(); j++)
			line[j] = '?';
		v[i++] = line;
	}

	for (int n=0; ; n+=2) {
		vector<string> v2(v.size() + n);
		for (unsigned int y=0; y<v2.size(); y++)
			v2[y].resize(v.size()+n);
		for (int left=0; left<=n; left++) {
			for (int top=0; top<=n; top++)
			if (top+left==n/2
				|| top + (n-left) == n/2
				|| (n-top) + left == n/2
				|| (n-top) + (n-left) == n/2
				)
			{
				for (int y=0; y<v2.size(); y++) {
					for (int x=0; x<v2.size(); x++) {
						unsigned int y2 = y-top;
						unsigned int x2 = x-left;
						if (y2>=v.size() || x2>=v.size())
							v2[y][x] = '?';
						else
							v2[y][x] = v[y2][x2];
					}
				}
				if (symmetric(v2))
					return (k+n/2)*(k+n/2) - (k*k);
			}
		}
	}
}

int main() {
	int T;
	cin >> T;
	for (int i=0; i<T; i++) {
		printf("Case #%d: %d\n", i+1, runTest());
		cerr << (i+1) << endl;
	}
	return 0;
}
