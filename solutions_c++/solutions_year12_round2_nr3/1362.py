#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int rInt() {int N; cin >> N; return N;}

void solve(vector <int>& v) {
	int N = (v).size();
	map <int, vector <int> > marked;
	for (int i = 0; i < (1 << N); ++i) {
		int mask = i;
		vector <int> subset;
		int s = 0;
		for (int j = 0; j < N; ++j)
			if (i & (1 << j)) {
				subset.push_back(v[j]);
				s += v[j];
			}
		if (marked.find(s) != marked.end()) {
			vector <int> temp = marked[s];
			for (int j = 0; j < temp.size(); ++j)
				printf("%d ", temp[j]);
			printf("\n");
			for (int j = 0; j < subset.size(); ++j)
				printf("%d ", subset[j]);
			printf("\n");
			return;
		}
		else
			marked[s] = subset;
	}
	printf("Impossible\n");
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int nTest = rInt();
	for (int test = 1; test <= nTest; ++test) {
		int N = rInt();
		vector <int> v(N, 0);
		for (int i = 0; i < N; ++i)
			v[i] = rInt();
		printf("Case #%d:\n", test);
		solve(v);
	}
	return 0;
}
