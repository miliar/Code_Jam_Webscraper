#include <vector>
#include <sstream>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

/*
 * if the input is 123456789011
 *
 * int a;
 * cin >> a;
 * a will we 2^31 - 1;
 *
 */

 int b[1000];
 int e[1000];
 int w[1000];

string calc()
{
	stringstream S;
	int i, j;

	int x, s, r, t, n;
	cin >> x >> s >> r >> t >> n;
	
	for (i=0; i<n; ++i) {
		cin >> b[i] >> e[i] >> w[i];
	}

	double ans = 0;
	double remain = t;

	for (i=0; i<=n; ++i) {
		int len;
		if (i == 0) {
			len = b[0];
		} else if (i == n) {
			len = x-e[n-1];
		} else {
			len = b[i]-e[i-1];
		}
		if (len == 0) continue;
		double t1 = len*1.0/s;
		double t2 = len*1.0/r;
		if (remain <= 0) {
			ans += t1;
		} else if (remain >= t2) {
			ans += t2;
			remain -= t2;
		} else {
			ans += remain + (len-remain*r)/s;
			remain = 0;
		}
	}

	vector<pair<int,int> > vp;
	for (i=0; i<n; ++i) {
		vp.push_back(make_pair(w[i], i));
	}

	sort(vp.begin(), vp.end());

	for (i=0; i<n; ++i) {
		int idx = vp[i].second;
		int len = e[idx]-b[idx];
		double t1 = len*1.0/(w[idx]+s);
		double t2 = len*1.0/(w[idx]+r);

		if (remain <= 0) {
			ans += t1;
		} else if (remain >= t2) {
			ans += t2;
			remain -= t2;
		} else {
			ans += remain + (len-remain*(w[idx]+r))/(w[idx]+s);
			remain = 0;
		}
	}

	char buf[128];
	sprintf(buf, "%.9f", ans);

	S << buf;


	//string line;
	//getline(cin, line);


	return S.str();
}

int main(void)
{
	int caseNum;
	cin >> caseNum;
	//string line;
	//getline(cin, line);
	for (int c=1; c<=caseNum; ++c) {
		cout << "Case #" << c << ": " << calc() << endl;
	}

	return 0;
}

