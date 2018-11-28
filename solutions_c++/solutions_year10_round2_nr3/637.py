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
    freopen("C-small.in", "r", stdin);
    ofstream fp("C-small.out");

	int fib[501];
	int memo[501][501] = {};

	int c[501][501] = {};
	c[0][0] = 1;
	for(int i = 1; i < 501;i++) {
		c[i][0] = 1;
		for(int j = 1; j <= i; j++) {
			c[i][j] = (c[i-1][j-1] + c[i-1][j]) % 100003;
		}
	}

	for(int num = 2; num <= 500; num++) {
		memo[num][1] = 1;
		for(int rank = 2; rank <= num - 1; rank++) {
			int res = 0;
			for(int rr = rank - 1; rr >= max(1, 2*rank-num); rr-- ) {
				res += (memo[rank][rr] * c[num-rank-1][rank-rr-1]) % 100003;
			}
			memo[num][rank] = res;
		}
	}
	for(int i = 2; i <= 500; i++ ) {
		int res = 0;
		for(int j = 1; j <= i-1; j++) {
			res += memo[i][j];
		}
		res %= 100003;
		fib[i] = res;
	}

	int T;
	scanf("%d", &T);

	for(int i = 0; i < T; i++)
	{
		int n;
		scanf("%d", &n);
		fp << "Case #" << i+1 << ": " << fib[n] << endl;
	}

    fp.close();
    return 0;
}