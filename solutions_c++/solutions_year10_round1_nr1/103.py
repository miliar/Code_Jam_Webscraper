/*
 * A.cpp
 *
 *  Created on: 2010-5-22
 *      Author: Allie
 */

#include <vector>
#include <stack> 
#include <queue>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <sstream> 
#include <iostream> 
#include <cmath>
#include <cassert>

using namespace std; 

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;

#define SZ(c) ((int) (c).size())

const int INF = 1000000000;

const int deltaR[] = { 0, 1, 1,  1 };
const int deltaC[] = { 1, 1, 0, -1 };

vs rotate(const vs &b)
{
	int n = SZ(b);
	vs res(n, string(n, '-'));
	for (int r = 0; r < n; ++r)
		for (int c = 0; c < n; ++c)
			res[c][n - 1 - r] = b[r][c];
	return res;
}

vs fall(vs b)
{
	int n = SZ(b);
	for (int c = 0; c < n; ++c) {
		int at = n - 1;
		for (int r = n - 1; r >= 0; --r)
			if (b[r][c] != '.')
				b[at--][c] = b[r][c];
		while (at >= 0)
			b[at--][c] = '.';
	}
	return b;
}

string winner(vs b, int K)
{
	b = fall(rotate(b));
	bool winR = false;
	bool winB = false;
	int n = SZ(b);
	for (int r = 0; r < n; ++r)
		for (int c = 0; c < n; ++c) if (b[r][c] != '.') {
			for (int i = 0; i < 4; ++i) {
				int cnt = 1;
				int dr = deltaR[i];
				int dc = deltaC[i];
				int rr = r;
				int cc = c;
				while (true) {
					rr += dr;
					cc += dc;
					if (rr < 0 || rr >= n || cc < 0 || cc >= n || b[rr][cc] != b[r][c])
						break;
					++cnt;
				}
				rr = r;
				cc = c;
				while (true) {
					rr -= dr;
					cc -= dc;
					if (rr < 0 || rr >= n || cc < 0 || cc >= n || b[rr][cc] != b[r][c])
						break;
					++cnt;
				}
				if (cnt >= K) {
					if (b[r][c] == 'R')  
						winR = true;
					else
						winB = true;
					break;
				} 
			}
		}
	
	if (winR) {
		if (winB)
			return "Both";
		else
			return "Red";
	} else {
		if (winB)
			return "Blue";
		else
			return "Neither";
	}
}

int main() 
{
	int T;
	cin >> T;
	for (int icase = 1; icase <= T; ++icase) {
		int N;
		int K;
		cin >> N >> K;
		vs b(N);
		for (int i = 0; i < N; ++i)
			cin >> b[i];
		printf("Case #%d: ", icase);
		cout << winner(b, K) << endl;
	}
	return 0;
}
