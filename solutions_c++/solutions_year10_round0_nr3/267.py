#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

typedef unsigned long long LL;

string calc()
{
	stringstream S;
	int i, j;

	int r, k, n;
	cin >> r >> k >> n;

	vector<LL> groups(n);
	for (i=0; i<n; ++i) {
		cin >> groups[i];
	}

	//cout << 1 << endl;

	vector<pair<int,LL> > loads(n+1);
	int start = 0;
	for (i=0; i<n+1; ++i) {
		LL num = 0;
		for (j=0; j<n; ++j) {
			LL a = groups[(start+j)%n];
			if (num+a > k) break;
			num += a;
		}

		loads[i] = make_pair(start, num);

		//cout << i << " : " << start << ' ' << num << endl;

		start = (start+j)%n;
	}

	//cout << 2 << endl;

	if (r <= n+1) {
		LL ans = 0;
		for (i=0; i<r; ++i) {
			ans += loads[i].second;
		}

		S << ans;
		return S.str();
	}

	//cout << 3 << endl;

	for (i=0; i<n+1; ++i) {
		for (j=i+1; j<n+1; ++j) {
			if (loads[i].first == loads[j].first) goto FOUND;
		}
	}
FOUND:

	//cout << 4 << endl;

	int first = i;
	int second = j;
	
	LL a = 0;
	for (i=0; i<first; ++i) {
		a += loads[i].second;
	}

	LL b = 0;
	for (i=first; i<second; ++i) {
		b += loads[i].second;
	}

	LL ans = a;
	r -= first;
	ans += r/(second-first)*b;

	for (i=0; i<r%(second-first); ++i) {
		ans += loads[(i+first)%n].second;
	}

	S << ans;
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

