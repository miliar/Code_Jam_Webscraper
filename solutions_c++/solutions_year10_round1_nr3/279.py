#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
using namespace std;

bool ok(int a, int b)
{
	if (a < b) {
		int t = a;
		a = b;
		b = t;
	}

	vector<int> divs;
	while (b) {
		divs.push_back(a/b);
		int t = a;
		a = b;
		b = t%b;
	}

	int oneNum = 0;
	int i;
	for (i=0; i<divs.size(); ++i) {
		if (divs[i] != 1) break;
		oneNum++;
	}

	oneNum &= 1;

	return !oneNum;


	for (int i=0; i<divs.size(); ++i) {
		cout << divs[i] << ' ';
	}
	cout << endl;

	return true;
}

string calc()
{
	stringstream S;
	int i, j;

	int A1, A2, B1, B2;
	cin >> A1 >> A2 >> B1 >> B2;

	//ok(12, 51);

	long long ans = 0;
	for (i=A1; i<=A2; ++i) for (j=B1; j<=B2; ++j) {
		if (ok(i, j)) ans++;
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

