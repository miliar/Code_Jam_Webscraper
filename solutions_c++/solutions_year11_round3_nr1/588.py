#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <ctime>

using namespace std;

	int m, n;
	char ch[50][50];

bool test(int i, int j) {
	if (i==m-1) return false;
	if (j==n-1) return false;
	if (ch[i+1][j]!='#') return false;
	if (ch[i][j+1]!='#') return false;
	if (ch[i+1][j+1]!='#') return false;
	return true;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("5l.out", "w", stdout);

	int t; cin>>t;
	bool finished;
	for (int k=1; k<=t; k++) {
		cout<<"Case #"<<k<<":\n";

		finished = false;
		cin>>m>>n;
		for (int i=0; i<m; i++) {
			for (int j=0; j<n; j++) {
				cin>>ch[i][j];
			}
		}
		for (int i=0; i<m && !finished; i++) {
			for (int j=0; j<n; j++) {
				if (ch[i][j]=='#') {
					if (test(i,j)) {
						ch[i][j] = ch[i+1][j+1] = '/';
						ch[i+1][j] = ch[i][j+1] = '\\';
					}
					else {
						cout<<"Impossible\n";
						finished = true;
						break;
					}
				}
			}
		}

		if (!finished) {
			for (int i=0; i<m; i++) {
				for (int j=0; j<n; j++) {
					cout<<ch[i][j];
				}
				cout<<endl;
			}
		}
	}

	return 0;
}
