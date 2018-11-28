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
template<class T> void minimize(T& a, T b) { a = min(a, b); }
template<class T> void maximize(T& a, T b) { a = max(a, b); }
#define ALL(a) (a).begin(), (a).end()
#define RALL(a) (a).rbegin(), (a).rend()

double sq(double x) {
	return x*x;
}

double dist(int x1, int y1, int x2, int y2) {
	return sqrt(sq(x1-x2)+sq(y1-y2));
}

double solve() {
	int n;
	cin>>n;
	vector<int> X(n),Y(n),R(n);
	for (int i=0; i<n; ++i) {
		cin>>X[i]>>Y[i]>>R[i];
	}
	if (n==1) {
		return R[0];
	}
	if (n==2) {
		return max(R[0],R[1]);
	}
	if (n==3) {
		return
		min(
			max(1.0*R[2],0.5*(R[0]+R[1]+dist(X[0],Y[0],X[1],Y[1]))),
		min(max(1.0*R[0],0.5*(R[1]+R[2]+dist(X[1],Y[1],X[2],Y[2]))),
			max(1.0*R[1],0.5*(R[0]+R[2]+dist(X[0],Y[0],X[2],Y[2]))))
		);
	}
	return -1;
}

int main() {
	freopen("gcj.in","r",stdin);
	freopen("gcj.out","w",stdout);
	cout.setf(ios::fixed,ios::floatfield);
	cout.precision(5);

	int N;
	cin>>N;
	for (int i=1; i<=N; ++i) {
		cout<<"Case #"<<i<<": "<<solve()<<endl;
	}
	return 0;
}
