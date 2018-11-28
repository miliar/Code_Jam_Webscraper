#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;

int matrix[50];

int main()
{
	//freopen("a-small.in", "r", stdin);
	freopen("a-small.out", "w", stdout);
	ofstream fout("a-small.out");
	ifstream fin("a-small.in");
	int testcases;
	char line;
	scanf("%d", &testcases);
	for (int tt=1; tt<=testcases; ++tt) {
		int N, i, t;
		memset(matrix, 0, sizeof matrix);
		scanf("%d", &N);
		for (i=0; i<N; ++i) {
			for (t=0; t<N; ++t) {
				cin >> line;
				if (line == '1') matrix[i] = t;
			}
		}
		int ans = 0;
		for (i=0; i<N; ++i) {
			for (t=i; t<N; ++t) {
				if (matrix[t] <= i && t == i) break;
				if (matrix[t] <= i && t > i) {
					int tmp = matrix[t]; 
					for (int k=t-1; k>=i; --k) {
						matrix[k+1] = matrix[k];
						++ans;
					}
					matrix[i] = tmp;
					break;
				}
			}
		}
		printf("Case #%d: %d\n", tt, ans);
	}

	return 0;
}