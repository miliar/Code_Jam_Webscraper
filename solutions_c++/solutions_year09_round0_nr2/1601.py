#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;

int main(void)
{
	int n;
	cin >> n;
	for(int nn = 0; nn < n; ++nn) {
		int height[102][102];
		int label[102][102];
		map<int,int> alias;

		int h, w;
		cin >> h >> w;
		for(int i=0;i<h;++i)
			for(int j=0;j<w;++j)
			{
				cin >> height[i+1][j+1];
				label[i+1][j+1] = 0;
			}

		for(int i=0;i<h;++i) height[i+1][0] = height[i+1][w+1] = 10000;
		for(int j=0;j<w;++j) height[0][j+1] = height[h+1][j+1] = 10000;

		int idx = 0;
		for(int i=1;i<=h;++i) {
			for(int j=1;j<=w;++j) {
				if(label[i][j] == 0) {
					int ii = i, jj =j;
					++idx;
					while(1) {
						if(label[ii][jj] == 0) {
							label[ii][jj] = idx;
							int c = height[ii][jj], n = height[ii-1][jj], w = height[ii][jj-1], s = height[ii+1][jj], e = height[ii][jj+1];
							if(c <= n && c <= w && c <= s && c <= e) { // sink
								break;
							} else if(n <= w && n <= s && n <= e) {
								ii = ii - 1;
							} else if(w < n && w <= s && w <= e) {
								jj = jj - 1;
							} else if(e < n && e < w && e <= s) {
								jj = jj + 1;
							} else if(s < n && s < w && s < e) {
								ii = ii + 1;
							}
						} else {
							alias[idx] = label[ii][jj];
							break;
						}
					}
				}
			}
		}

		for(map<int, int>::iterator mi = alias.begin(); mi != alias.end(); ++mi) {
			if(alias.count(mi->second)) {
				alias[mi->first] = alias[mi->second];
			}
		}

		map<int, char> table;
		char c = 'a';
		cout << "Case #" << nn+1 << ":" << endl;
		for(int i=1;i<=h;++i) {
			for(int j=1;j<=w;++j) {
				int idx = label[i][j];
				if(alias.count(idx)) idx = alias[idx];
				if(table.count(idx) == 0) {
					table[idx] = c;
					++c;
				}
				if(j!=1) cout << ' ';
				cout << table[idx];
			}
			cout << endl;
		}
	}
	
	return 0;
}
