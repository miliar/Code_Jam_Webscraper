#include <iostream>
#include <map>

#define MAX_N 101
#define MAX_M 101

using namespace std;

pair<unsigned long long int, unsigned long long int> boxes[MAX_N + 1], toys[MAX_M + 1];

unsigned long long int lcs(int n, int m, int maxn, int maxm) {
	if(n > maxn || m > maxm) return 0;
	else if(n == 0 || m == 0) return 0;
	
	unsigned long long int ret;
	if (boxes[n].second == toys[m].second) {
		unsigned long long int mc = min(boxes[n].first, toys[m].first);
		
		boxes[n].first -= mc;
		toys[m].first -= mc;
		
		if (boxes[n].first) {
			ret = mc + lcs(n, m - 1, maxn, maxm);
		} else if (toys[m].first) {
			ret = mc + lcs(n - 1, m, maxn, maxm);
		} else {	
			ret = mc + lcs(n - 1, m - 1, maxn, maxm);
		}
		
		boxes[n].first += mc;
		toys[m].first += mc;
		
		return ret;
	} else {
		ret = max(lcs(n, m - 1, maxn, maxm), lcs(n - 1, m, maxn, maxm));
	}
	
	return ret;
}

int main(void) {
	int t, n, m;
	
	cin >> t;
	for(int numCase = 1; numCase <= t; numCase++) {
		cin >> n >> m;
		for(int i = 1; i <= n; i++) cin >> boxes[i].first >> boxes[i].second;
		for(int i = 1; i <= m; i++) cin >> toys[i].first >> toys[i].second;
		
		cout << "Case #" << numCase << ": ";
		cout << lcs(n, m, n, m) << endl;
	}
}
