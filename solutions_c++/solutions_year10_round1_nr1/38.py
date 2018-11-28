#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

string b[1000];
string r[1000];
string e[1000];

void show(string* a, int n) {
	for (int i=0;i<n;++i)
		cout << a[i] << endl;
	cout << endl;
}

bool check(string* a, int n, char g, int k) {
	static const int dx[]={0,1,1,1};
	static const int dy[]={1,0,1,-1};
	for (int i=0;i<n;++i) {
		for (int j=0;j<n;++j) {
			for (int z=0;z<4;++z) {
				bool ok = 1;
				for (int am=0;am<k;++am) {
					int nx = i + am*dx[z];
					int ny = j + am*dy[z];
					if (0 <= nx && nx < n && 0 <= ny && ny < n && a[nx][ny] == g);
					else {
						ok = 0;
						break;
					}
				}
				if (ok) return 1;
			}
		}
	}
	return 0;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int z=1;z<=ncases;++z) {
		int n,k;
		cin >> n >> k;
		for (int i=0;i<n;++i) {
			cin >> b[i];
			r[i] = e[i] = string(n,'.');
		}

		for (int i=0;i<n;++i)
			for (int j=0;j<n;++j)
				r[j][n-1-i] = b[i][j];

		for (int j=0;j<n;++j) {
			int place = n-1;
			for (int i=n-1;i>=0;--i) {
				if (r[i][j] != '.') {
					e[place][j] = r[i][j];
					--place;
				}
			}
		}

		bool blue = check(e,n,'B',k);
		bool red = check(e,n,'R',k);

		printf("Case #%d: ", z);
		if (blue && red) printf("Both");
		else if (blue) printf("Blue");
		else if (red) printf("Red");
		else printf("Neither");
		printf("\n");
	}
}
