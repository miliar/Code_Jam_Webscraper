#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <utility>
#include <queue>
#include <map>
using namespace std;

typedef long long LL;
typedef unsigned int UINT32;

int M, N;


map<vector<string>, int> cache;

bool valid(string& s, int m)
{
	int pre = -2;
	for (int i=0; i<N; ++i) if (m&(1<<i)) {
		if (s[i] == 'x') return false;
		if (pre+1 == i) return false;
		pre = i;
	}
	return true;
}

int calc(vector<string>& curmap)
{
	if (curmap.size() == 0) return 0;

	if (cache.find(curmap) != cache.end()) return cache[curmap];

	int & ans = cache[curmap];
	ans = 0;

	int r = curmap.size()-1;
	for (int i=0; i<1<<N; ++i) if (valid(curmap[r], i)) {
		int num = 0;
		vector<string> newmap = curmap;
		newmap.erase(newmap.begin()+r);
		int nr = r-1;
		for (int j=0; j<N; ++j) if (i&(1<<j)) {
			num++;
			if (nr >= 0) {
				if (j-1>=0) newmap[nr][j-1] = 'x';
				if (j+1<N) newmap[nr][j+1] = 'x';
			}
		}
		num += calc(newmap);

		if (num > ans) ans = num;
	}

	return ans;
}

int main(void)
{
	int C;
	cin >> C;
	vector<string> map;
	for (int i=1; i<=C; ++i) {
		cin >> M >> N;
		map.clear();

		string s;
		for (int j=0; j<M; ++j) {
			cin >> s;
			map.push_back(s);
		}

		cout << "Case #" << i << ": " << calc(map) << endl;
	}

	return 0;
}

