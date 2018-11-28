#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <sstream>
using namespace std;

int getSquare(vector<int> & num)
{
	int ret = 0;
	for (int i = 0; i < num.size(); ++i)
		ret += num[i] * num[i];
	return ret;
}

vector<int> toBase(int num, int base)
{
	vector<int> ret;
	while (num > 0) {
		ret.push_back(num % base);
		num /= base;
	}
	return ret;
}

set<int> appear;
bool judge(int num, int base)
{
	appear.clear();
	while (true) {
		vector<int> digits = toBase(num, base);
		int square = getSquare(digits);
		if (square == 1) return true;
		if (appear.find(square) != appear.end()) return false;
		appear.insert(square);
		num = square;
	}
}

int main()
{
	string line;
	int T;
	cin >> T;
	getline(cin, line);

	for (int i = 1; i <= T; ++i) {
		getline(cin, line);
		istringstream sin(line);
		vector<int> bases;
		int base;
		while (sin>>base)
			bases.push_back(base);
		
		int answer = 1;
		while (true) {
			answer ++;
			bool ok = true;
			for (int j = 0; j < bases.size(); ++j) {
				if (judge(answer, bases[j]) == false) {
					ok = false;
					break;
				}
			}
			if (ok) {
				printf("Case #%d: %d\n", i, answer);
				break;
			}
		}
	}

	return 0;
}

