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

struct Node {
	double w;
	string f;
	Node* children[2];
	Node() {
		char c;
		cin>>c;
		cin>>w;
		cin>>c;
		f="";
		if (c!=')') {
			cin.putback(c);
			cin>>f;
			children[0]=new Node();
			children[1]=new Node();
			cin>>c;
		}
	}
	void prob(const set<string>& features, double& p) {
		p*=w;
		if (features.count(f)) {
			children[0]->prob(features,p);
		}
		else if (f!="") {
			children[1]->prob(features,p);
		}
	}
};

void solve() {
	int n;
	cin>>n;
	Node tree;
	cin>>n;
	for (int i=0; i<n; ++i) {
		string s;
		int m;
		cin>>s>>m;
		set<string> f;
		for (int j=0; j<m; ++j) {
			cin>>s;
			f.insert(s);
		}
		double p=1;
		tree.prob(f,p);
		cout<<p<<endl;
	}
}

int main() {
	freopen("gcj.in","r",stdin);
	freopen("gcj.out","w",stdout);
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(7);

	int N;
	cin>>N;
	for (int i=1; i<=N; ++i) {
		cout<<"Case #"<<i<<":"<<endl;
		solve();
	}
	return 0;
}
