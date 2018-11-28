#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <utility>
#include <string>
#include <cstring>
using namespace std;

string calc()
{
	stringstream S;
	int i, j;

	//string line;
	//getline(cin, line);

	int N;
	cin >> N;

	int a;
	int m = 123456789;
	int sum = 0;
	int po = 0;
	for (i=0; i<N; ++i) {
		cin >> a;
		if (a < m) {
			m = a;
		}

		sum += a;

		po ^= a;
	}

	if (po != 0) {
		S << "NO";
	} else {
		S << sum-m;
	}

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

