/* Rajat Goel [C++] */
#include<iostream>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;
const int    INF =     0x7FFFFFFF;
const double EPS =     1e-7;
typedef pair<int,int>  pii;
typedef long long      int64;
#define loop(i,n)      for(int i=0;i<n;i++)
#define foreach(i,a)   for(typeof((a).begin()) i=(a).begin();i!=(a).end();++i)
#define present(x,in)  (find((in).begin(),(in).end(),x) != (in).end())
#define all(a)         (a).begin(),(a).end()
#define cast(a,b)      { ostringstream myOut; myOut << a ; istringstream myIn ( myOut.str() ); myIn >> b; }
inline int fCMP(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}

map<pair<int, int>, bool> memo;

int next(int n, int b) {
	int ans = 0;
	while (n) {
		int tmp = n%b;
		ans += (tmp*tmp);
		n/=b;
	}
	return ans;
}

bool happy(int n, int b) {
	int tmp_n = n;
	if (memo.find(make_pair(n,b))!=memo.end()) return memo[make_pair(n,b)];
	vector<bool> visited(1000005, false);

	while (n!=1) {
		if (visited[n]) break;
		visited[n] = true;
		n = next(n,b);
	}
	return memo[make_pair(tmp_n, b)] = (n==1);
}

int main() {
	int T, tmp;
	cin >> T;
	for (int cas=1;cas<=T;cas++) {
		char arr[2048];
		scanf(" %[^\n]", arr);
		ostringstream out; out << arr;
		istringstream in (out.str());
		vector<int> base;
		while(in>>tmp) {
			base.push_back(tmp);
		}
		for (int i = 2; i < 1000000;i++) {
			bool poss = true;
			for (int j = 0;j<base.size();j++) {
				if (!happy(i, base[j])) {
					poss = false;
					break;
				}
			}
			if (poss) {
				cout << "Case #" << cas << ": " << i << endl;
				break;
			}
		}
	}
	return 0;
}
