#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;


int C, D;
vector<pair<int,int> > vendors;

bool ok(double t)
{
	double pre = -10000000;
	int i, j;
	for (i=0; i<vendors.size(); ++i) {
		int p = vendors[i].first;
		for (j=0; j<vendors[i].second; ++j) {
			if (p+t < pre+D) {
				return false;
			} else if (p-t > pre+D) {
				pre = p-t;
			} else {
				pre = pre+D;
			}
		}
	}

	return true;
}

string calc()
{
	stringstream S;
	int i, j;

	cin >> C >> D;

	vendors.resize(C);

	for (i=0; i<C; ++i) {
		cin >> vendors[i].first >> vendors[i].second;
	}

	double l = 0;
	double h = 1000000;

	for (i=0; i<100; ++i) {
		double m = (l+h)/2;
		if (ok(m)) {
			h = m;
		} else {
			l = m;
		}
	}

	S << (l+h)/2;
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

