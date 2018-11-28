#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <queue>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

template <class A, class B> void convert(A& x, B& y) {stringstream s; s<<x; s>>y;}


struct state {
	vector<string> v;
	int d;
};

bool validate(vector<string> v) {
	int i, j, k;
	for (i=0; i<v.size(); i++) {
		for (j=i+1; j<v.size(); j++) {
			if (v[i][j] == '1') return false;
		}
	}
	return true;
}

int main() {
	//ifstream cin("in.txt");
	ifstream cin("A-small.in");
	//ifstream cin("A-large.in");
	ofstream cout("out");
	int N, T, Case;
	int i, j, k,dd;
	string s;
	vector<string> vv;
	int res = 0;
	for (cin>>T, Case=1; T; T--,Case++) {
		map<vector<string>,int> m;
		vv.resize(0);
		cin>>N;
		for (i=0; i<N; i++) {
			cin>>s;
			vv.push_back(s);
		}
		struct state st;
		st.v = vv;
		st.d = 0;
		queue<struct state> q;
		m[st.v] = 1;
		q.push(st);
		while (!q.empty()) {
			st = q.front();
			q.pop();
			vv = st.v;
			dd = st.d;
			if (validate(vv)) {
				res = st.d;
				break;
			}
			for (i=0; i<vv.size(); i++) {
				if (i>0) {
					swap(vv[i-1], vv[i]);
					if (m[vv] == 0) {
						m[vv] = 1;
						st.d = dd + 1;
						st.v = vv;
						q.push(st);
					}
					swap(vv[i-1], vv[i]);
				}
				if (i<vv.size()-1) {
					swap(vv[i+1], vv[i]);
					if (m[vv] == 0) {
						m[vv] = 1;
						st.d = dd + 1;
						st.v = vv;
						q.push(st);
					}
					swap(vv[i+1], vv[i]);
				}
			}
		}
		cout<<"Case #"<<Case<<": "<<res<<endl;
	}

}