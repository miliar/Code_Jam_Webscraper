#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>

using namespace std;

template<class AnswerType>
void PrintAnswerToTestCase(size_t caseNumber, AnswerType ans)
{
	cout << "Case #" << caseNumber << ": " << ans << endl;
}


int GetCode(char a, char b) {
	if (a < b)
		return (int)a + 256 * (int)b;
	return (int)b + 256 * (int)a;
}

template <class AnswerType>
AnswerType SolveTestCase() {
	int numCombs;
	cin >> numCombs;
	map<int, char> combs;
	for (int i = 0; i < numCombs; i++) {
		string str;
		cin >> str;
		combs[GetCode(str[0], str[1])] = str[2];
	
	}
	int numOppositions;
	cin >> numOppositions;
	set<int> oppositions;
	for (int i = 0; i < numOppositions; i++) {
		string str;
		cin >> str;
		oppositions.insert(GetCode(str[0], str[1]));
	}

	int len;
	cin >> len;

	string seq;
	cin >> seq;

	string res;
	for (int i = 0; i < len; i++) {
		if (res.empty()) {
			res.push_back(seq[i]);
		} else {
			if (combs.find(GetCode(res[res.length() - 1], seq[i])) != combs.end()) {
				res[res.length() - 1] = combs[GetCode(res[res.length() - 1], seq[i])];
			} else {
				bool clear = false;
				for (int j = 0; j < res.length(); j++)
					if (oppositions.find(GetCode(res[j], seq[i])) != oppositions.end())
						clear = true;
				if (clear) {
					res.clear();
				} else {
					res.push_back(seq[i]);
				}

			}
		}
	}

	string resToPrint(3 * res.length() + 2 * (res.length() == 0), ' ');
	resToPrint[0] = '[';
	resToPrint[resToPrint.length() - 1] = ']';
	for (int i = 0; i < res.length(); i++)
		resToPrint[3 * i + 1] = res[i];
	for (int i = 0; i < (int)res.length() - 1; i++)
		resToPrint[3 * i + 2] = ',';
	return resToPrint;
}

int main()
{
	//freopen("input.txt", "r", stdin);
	//freopen("small.in", "r", stdin);
	freopen("large.in", "r", stdin);

	freopen("output.txt", "w", stdout);

	int numCases;
	cin >> numCases;

	for (int caseNumber = 1; caseNumber <= numCases; caseNumber++)
		PrintAnswerToTestCase(caseNumber, SolveTestCase<string>() );

	return 0;
}