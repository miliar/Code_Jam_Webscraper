#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

double task() {
	//read
	int x, s, r, t, n;
	
	scanf("%d %d %d %d %d", &x, &s, &r, &t, &n);
	
	priority_queue<pair<pair<int, int>, int >, vector<pair<pair<int, int>, int > >, greater<pair<pair<int, int>, int > > > vrsta1;
	priority_queue<pair<int, int >, vector<pair<int, int > >, greater<pair<int, int > > > vrsta2;
	
	for (int i = 0; i < n; i++) {
		int b, e, w;
		scanf("%d %d %d", &b, &e, &w);
		vrsta1.push(make_pair(make_pair(b, e), w));
		vrsta2.push(make_pair(w, e - b));
	}
	
	int pos = 0;
	while (!vrsta1.empty()) {
		int raz = vrsta1.top().first.first - pos;
		
		//cout << vrsta1.top().first.first << endl;
		
		if (raz > 0)
			vrsta2.push(make_pair(0, raz));
		
		pos = vrsta1.top().first.second;
		
		vrsta1.pop();
	}
	
	if (pos < x)
		vrsta2.push(make_pair(0, x - pos));
	
	double td = t;
	double res = 0;
	
	while (!vrsta2.empty()) {
		int hitrost = vrsta2.top().first;
		int razdalja = vrsta2.top().second;
		vrsta2.pop();
		
		double cas = (double)razdalja / (hitrost + r);
		
		//cout << hitrost << " "  << razdalja << endl;
		
		if (cas > td) {
			res += td;
			
			res += (razdalja - (hitrost + r) * td) / (hitrost + s);
			
			//cout << " + " << t << " " << (razdalja - (hitrost + r) * t) / (hitrost + s) << endl;
			
			td = 0;
		} else {
			td -= cas;
			res += cas;
			
			//cout << " + " << cas << endl;
		}
		
	}

	return res;
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		printf("%lf\n", task());
		//task();
	}
}

