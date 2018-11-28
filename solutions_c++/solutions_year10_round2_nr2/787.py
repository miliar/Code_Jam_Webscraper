#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <fstream>

using namespace std;

int main() 
{
    freopen("B-small.in", "r", stdin);
    ofstream fp("B-small.out");

	int X[50];
	int V[50];
	bool mark[50];

	int C;
	scanf("%d", &C);

	for(int i = 0; i < C; i++)
	{
		int N, K, B, T;
		scanf("%d%d%d%d", &N, &K, &B, &T);
		for(int j = 0; j < N; j++) {
			scanf("%d", &(X[j]));
		}
		for(int j = 0; j < N; j++) {
			scanf("%d", &(V[j]));
		}

		memset(mark, 0, sizeof(mark));
		for(int j = 0; j < N; j++) {
			if(B - X[j] <= V[j] * T) {
				mark[j] = 1;
			}
		}

		int res = 0;
		int nCannot = 0;
		int nCan = 0;
		for(int j = N - 1; j >= 0; --j) {
			if(nCan >= K) break;
			if(mark[j]) {
				nCan++;
				res += nCannot;
			}
			else {
				nCannot++;
			}
		}
		if(nCan >= K) {
			fp << "Case #" << i+1 << ": " << res << endl;
		}
		else {
			fp << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}
	}

    fp.close();
    return 0;
}