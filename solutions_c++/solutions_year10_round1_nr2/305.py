#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <cstring>
using namespace std;

int D, I, M, N;
vector<int> a;

int cache[128][300];

int calc(int pos, int preVal)
{
	if (pos == N) {
		return 0;
	}

	if (cache[pos][preVal] != -1) return cache[pos][preVal];

	preVal--;

	int ans = 100*D;

	//Delete
	int t = calc(pos+1, preVal+1) + D;
	if (t < ans) ans = t;

	if (preVal != -1) {
		//Insert
		int v = abs(a[pos]-preVal);
		if (v <= M) {
			t = calc(pos+1, a[pos]+1);
			if (t < ans) ans = t;
		} else if (M != 0) {
			t = calc(pos+1, a[pos]+1) + ((v+M-1)/M-1)*I;
			if (t < ans) ans = t;
		}

		for (int i=0; i<=255; ++i) if (abs(i-preVal) <= M) {
			t = calc(pos+1, i+1) + abs(a[pos]-i);
			if (t < ans) ans = t;
		}
	} else {
		for (int i=0; i<=255; ++i) {
			t = calc(pos+1, i+1) + abs(a[pos]-i);
			if (t < ans) ans = t;
		}
	}

	//cout << pos << ' ' << preVal << " : " << ans << endl;
	return cache[pos][preVal+1] = ans;
}

string calc()
{
	stringstream S;
	int i, j;

	cin >> D >> I >> M >> N;

	a.resize(N);

	for (i=0; i<N; ++i) {
		cin >> a[i];
	}

	memset(cache, -1, sizeof(cache));

	S << calc(0, 0);

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

