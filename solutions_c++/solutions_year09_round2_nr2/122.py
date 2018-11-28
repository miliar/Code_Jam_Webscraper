#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cassert>
#include <climits>
#include <cfloat>
#include <ctime>
#include <vector>
#include <deque>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <utility>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <sstream>
#include <iostream>
#include <iomanip>
using namespace std;

typedef long long LL;

string solve() {
	string n;
	cin>>n;
	n='0'+n;
	next_permutation(n.begin(), n.end());
	if (n[0]=='0') {
		n=n.substr(1);
	}
	return n;
}

int main() {
	freopen("gcj.in","r",stdin);
	freopen("gcj.out","w",stdout);
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(7);

	int N;
	cin>>N;
	for (int i=1; i<=N; ++i) {
		cout<<"Case #"<<i<<": "<<solve()<<endl;
	}
	return 0;
}
