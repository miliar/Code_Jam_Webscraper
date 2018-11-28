#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

int a[100][100];
int conns[100];
int p[100][25];
int isClique[1<<16];
int isMaxClique[1<<16];
int dp[1<<16];
vector<int> MaxCliques;
vector<int> bCache[16];

int cb(int x) {
	int res = 0;
	while(x) {
		x &= (x-1);
		res++;
	}
	return res;
}

int noConflict(int x, int y, int k) {
	for (int i=0;i<k;i++)
		if (p[x][i] == p[y][i])
			return 0;
	
	for (int i=0;i<k-1;i++) {
		if (p[x][i] < p[y][i] && p[x][i+1] >= p[y][i+1])
			return 0;
		if (p[x][i] > p[y][i] && p[x][i+1] <= p[y][i+1])
			return 0;
	}
	return 1;
}

void dump(int x) {
	int c = 0;
	cerr << '(';
	while(x) {
		if (x & (1<<c)) {
			cerr << c << ' ';
			x ^= (1<<c);
		}
		++c;
	}
	cerr << ')' << endl;
}

int solve(int mask) {
	int& res = dp[mask];
	if (res >= 0)
		return res;
	if (isClique[mask])
		return res = 1;
	res = 987654321;
    int bit = mask ^ (mask & (mask-1));
    for (int i=0;i<MaxCliques.size();i++)
		if (MaxCliques[i] & bit)
			res = min(res, 1+solve(mask & ~MaxCliques[i]));
	return res;
}

int solve(int n, int k) {
	for(int i=0;i<n;i++) {
		a[i][i] = 0;
		for (int j=i+1;j<n;j++)
			a[i][j] = a[j][i] = noConflict(i,j,k);
	}
	for (int i=0;i<n;i++)   {
		for(int j=0;j<n;j++)
			cerr << a[i][j] << ' ';
		cerr << endl;
	} 
    for (int i=0;i<n;i++) {
		conns[i] = 0;
		for (int j=0;j<n;j++)
			if (a[i][j])
				conns[i] |= (1 << j);
	}
    memset(dp, -1, sizeof(dp));
	dp[0] = 1;
	memset(isClique,0,sizeof(isClique));
	isClique[0] = 1;
	for(int i=0;i<n;i++)
		isClique[1<<i] = dp[1<<i] = 1;
    for (int i=1;i<n;i++) {
		for (int j=0;j<bCache[i].size();j++) {
			int cur=bCache[i][j];
			if (cur >= (1<<n))
				break;
			if (!isClique[cur])
				continue;
            for (int k=0;k<n;k++) {
				int kMask = 1<<k;
				if (kMask & cur)
					continue;
				if ((conns[k] & cur) == cur) { 
					isClique[kMask | cur] = 1;
				}
			}
		}
	}
	MaxCliques.clear();
	for (int i=0;i<(1<<n);i++) {
		if (!isClique[i])
			isMaxClique[i] = 0;
		else {
			isMaxClique[i] = 1;
			for (int j=0;j<n;j++)
				if (!(i & (1<<j)))
					if (isClique[i|(1<<j)]) {
						isMaxClique[i] = 0;
						break;
					}
			if (isMaxClique[i] ) {
				MaxCliques.push_back(i);
				dump(i);
			}
		}
	}
	cerr << endl;
    return solve((1<<n)-1);
}

void initCache() {
	for (int i=0;i<(1<<16);i++) {
		bCache[cb(i)].push_back(i);
	}
}

int main() {
	initCache();
	int nCases;
	cin >> nCases;
	for (int i=1;i<=nCases;i++) {
		int m,n;
		cin >> m >> n;
		for(int j=0;j<m;j++) 
			for (int k=0;k<n;k++)
				cin >> p[j][k];
		cout << "Case #" << i << ": " << solve(m,n) << endl;
	}
	return 0;
}
