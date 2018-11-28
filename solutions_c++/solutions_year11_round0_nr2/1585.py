#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l;
int opposed[26][26], combine[26][26];

int main() {

//	freopen("x.in", "r", stdin);

//	freopen("X-small-attempt0.in", "r", stdin);
//	freopen("X-small-attempt0.out", "w", stdout);

//	freopen("X-large.in", "r", stdin);
//	freopen("X-large.out", "w", stdout);

	int tt, tn; cin >> tn;

	F1(tt,tn) {
		printf("Case #%d: ", tt);

	F0(i,26) F0(j,26) combine[i][j] = opposed[i][j] = -1;

cin >> n;
while (n--) {
string s;
cin >> s;
i=s[0]-'A';
j=s[1]-'A';
k=s[2]-'A';
combine[i][j] = combine[j][i] = k;
}

cin >> n;
while (n--) {
string s;
cin >> s;
i=s[0]-'A';
j=s[1]-'A';
opposed[i][j] = opposed[j][i] = 1;
}

cin >> n;
string s;
vector<int> ans;
cin >> s;
F0(k,n) {
ans.push_back(s[k]-'A');

while (1) {
i = SZ(ans);
if (i >= 2 && combine[ans[i-2]][ans[i-1]] != -1) {
j = combine[ans[i-2]][ans[i-1]];
ans.pop_back();
ans.pop_back();
ans.push_back(j);
} else break;
}

i = SZ(ans);
F0(j,i)
if (opposed[ans[j]][ans[i-1]] == 1) {
ans.clear();
break;
}

}



	cout << "[";
F0(i,SZ(ans)) {
if (i) cout << ", ";
cout << (char)(ans[i]+'A');
}
cout << "]";

		cout << endl;
	}
	
	return 0;
}