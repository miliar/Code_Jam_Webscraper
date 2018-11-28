#include <iostream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

int M, V;

vector<int> tree;
vector<int> change;
vector<int> cache;

const int MNUM = 1000000;

int main(void)
{
	int i, j;
	int N;
	cin >> N;
	for (i=1; i<=N; ++i) {
		cin >> M >> V;

		tree.clear();
		change.clear();
		cache.clear();

		tree.resize(M+1);
		change.resize(M+1);
		cache.resize(M+1, MNUM);

		int g, c;
		for (j=1; j<=(M-1)/2; ++j) {
			cin >> g >> c;
			change[j] = (g<<8) | c;
		}
		for (j=(M-1)/2+1; j<=M; ++j) {
			cin >> tree[j];
		}

		for (j=M/2; j>0; --j) {
			tree[j] = (change[j]>>8) ? tree[2*j]&&tree[2*j+1] : tree[2*j]||tree[2*j+1]; 
		}

		for (j=M/2; j>0; --j) {
			bool isch = change[j]&0xff;
			bool isand = change[j]>>8;

			if (isch) {
				if (isand) {
					if (tree[j]) {
						cache[j] = min(cache[2*j], cache[2*j+1]);
					} else {
						if (tree[2*j] || tree[2*j+1]) cache[j] = 1;
						else cache[j] = 1 + min(cache[2*j], cache[2*j+1]);
					}
				} else {
					if (tree[j]) {
						if (!tree[2*j] || !tree[2*j+1]) cache[j] = 1;
						else cache[j] = 1 +  min(cache[2*j], cache[2*j+1]);
					} else {
						cache[j] = min(cache[2*j], cache[2*j+1]);
					}
				}
			} else {
				if (isand) {
					if (tree[j]) {
						cache[j] =  min(cache[2*j], cache[2*j+1]);
					} else {
						if (!tree[2*j]) {
							if (!tree[2*j+1]) cache[j] = cache[2*j] + cache[2*j+1];
							else cache[j] = cache[2*j];
						} else {
							cache[j] = cache[2*j+1];
						}
					}
				} else {
					if (tree[j]) {
						if (tree[2*j]) {
							if (tree[2*j+1]) cache[j] = cache[2*j] + cache[2*j+1];
							else cache[j] = cache[2*j];
						} else {
							cache[j] = cache[2*j+1];
						}
					} else {
						cache[j] =  min(cache[2*j], cache[2*j+1]);
					}
				}
			}

			if (cache[j] > MNUM) cache[j] = MNUM;
		}

		/*
		cout << V << endl;
		for (j=1; j<=M; ++j) cout << cache[j] << ' ';
		cout << endl;
		*/

		cout << "Case #" << i << ": ";
		if (V == tree[1]) {
			cout << 0 << endl;
		} else if (cache[1] == MNUM) {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << cache[1] << endl;
		}
	}

	return 0;
}
