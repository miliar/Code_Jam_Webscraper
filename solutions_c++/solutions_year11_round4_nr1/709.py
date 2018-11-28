#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <stack>
#include <deque>
#include <queue>
#include <map>
#include <set>
#include <stdlib.h>
#include <memory.h>
using namespace std;
int _T;
struct cell {
	double len,v;

	bool operator <(const cell& A) const {
		return v < A.v;
	}
};

int main() {
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	cin >> _T;
	for (int _t=1;_t<=_T;_t++) {
		printf("Case #%d: ", _t);
		cell T;
		vector<cell> a;
		a.clear();

		double x,v,dv,t; int n;
		cin >> x >> v >> dv >> t >> n;
		dv -= v;

		double prev = 0;
		for (int i=0;i<n;i++) {

			double B, E, w;
			cin >> B >> E >> w;
			if (B > prev) {
				T.len = B - prev; T.v = v;
				a.push_back(T);
			}
			T.len = E-B; T.v = w + v;
			a.push_back(T);
			prev = E;
		}
		if (prev < x) {
			T.len = x - prev; T.v = v;
			a.push_back(T);
		}

		double curans = 0;
		sort(a.begin(),a.end());
		for (int i=0;i<a.size();i++) curans += a[i].len / a[i].v;

		for (int i=0;i<a.size();i++)
			if (t > 0) {
				double c = min(t,a[i].len / (a[i].v + dv));
				double nlen = c * (a[i].v + dv);
				curans -= a[i].len / a[i].v;
				curans += c + (a[i].len - nlen) / a[i].v;
				t -= c;
			}
		
		printf("%.15lf\n",curans);
	}


	return 0;
}
