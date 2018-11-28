#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <algorithm>
#include <numeric>

using namespace std;

int toInt(char ch) {
	return ch - 'A';
}

char toChar(int i) {
	return i + 'A';
}

vector<char> solve( map<int, int>* combine, set<int>* opposite, vector<char>& invoke) 
{
	vector<char> ret;
	int distinctCnt[26];
	memset(distinctCnt, 0, 26 * 4);
	for (int i = 0; i < invoke.size(); ++i) {
		ret.push_back(invoke[i]);
		++distinctCnt[toInt(ret.back())];
		if (ret.size() < 2) {
			continue;
		}
		int last = toInt(ret.back());
		int last_1 = toInt(ret[ret.size() - 2]);
		map<int, int>::iterator combIt = combine[last].find(last_1);
		if (combIt != combine[last].end() && combIt->first == last_1) {
			ret.pop_back();
			--distinctCnt[last];
			ret.pop_back();
			--distinctCnt[last_1];
			ret.push_back(toChar(combIt->second));
		} // if (combIt != combine[last].end() && combIt->second == last_1)
		else { // may be opposite
			for (set<int>::iterator oppositeIt = opposite[last].begin(); oppositeIt != opposite[last].end(); ++oppositeIt) {
				if (distinctCnt[*oppositeIt]) {
					memset(distinctCnt, 0, 26 * 4);
					ret.clear();
					break;
				}
			} // for (set<int>
		} // else
	} // for (int i = 0; i < invoke.size(); ++i)
	return ret;
}

int main(int argc, char* argv[]) {
	int numOfCases;
	int curCase = 1;
	cin >> numOfCases;
	for (;curCase <= numOfCases; ++curCase) {
		int numOfCombine;
		cin >> numOfCombine;
		map<int, int> combine[26];
		for (int i = 0; i < numOfCombine; ++i) {
			string tmp;
			cin >> tmp;
			combine[toInt(tmp[0])].insert(make_pair(toInt(tmp[1]), toInt(tmp[2])));
			combine[toInt(tmp[1])].insert(make_pair(toInt(tmp[0]), toInt(tmp[2])));
		} // for (int i = 0; i < numOfCombine; ++i)
		set<int> opposite[26];
		int numOfOpposite;
		cin >> numOfOpposite;
		for (int i = 0; i < numOfOpposite; ++i) {
			string tmp;
			cin >> tmp;
			opposite[toInt(tmp[0])].insert(toInt(tmp[1]));
			opposite[toInt(tmp[1])].insert(toInt(tmp[0]));
		} // for (int i = 0; i < numOfOpposite; ++i)

		int numOfInvoke;
		cin >> numOfInvoke;
		vector<char> invoke;
		for (int i = 0; i < numOfInvoke; ++i) {
			char ch;
			cin >>ch;
			invoke.push_back(ch);
		}
		const vector<char>& result = solve(combine, opposite, invoke);
		cout << "Case #" <<curCase << ": [";
		for (int i = 0; i < result.size(); ++i) {
			cout << result[i];
			if (i != result.size() - 1) {
				cout <<", ";
			}
		}
		cout <<']' << endl;
	}
}