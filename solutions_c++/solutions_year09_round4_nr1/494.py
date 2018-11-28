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

int n;
/*
bool test(const vector<int>& m) {
	for (int i=0; i<m.size(); ++i) {
		string& row=rows[m[i]];
		for (int j=i+1; j<m.size(); ++j) {
			if (row[j]=='1') {
				return false;
			}
		}
	}
	return true;
}
*/

int minRow(string row) {
	int ans=n-1;
	for (int i=n-1; i>0; --i) {
		if (row[i]=='0') {
			--ans;
		}
		else {
			break;
		}
	}
	return ans;
}

int solve() {
	cin>>n;
	vector<pair<int, string> > rows(n);
	for (int i=0; i<n; ++i) {
		cin>>rows[i].second;
		rows[i].first=minRow(rows[i].second);
	}
	vector<int> vis(n);
	for (int i=0; i<n; ++i) {
		for (int j=0; j<n; ++j) {
			if (!vis[j]) {
				if (rows[j].first<=i) {
					rows[j].first=i;
					vis[j]=1;
					break;
				}
			}
		}
	}
	int ans=0;
	for (int j=0; j<n; ++j) {
		for (int i=0; i+1<n; ++i) {
			if (rows[i].first>rows[i+1].first) {
				swap(rows[i],rows[i+1]);
				++ans;
			}
		}
	}
	return ans;
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
