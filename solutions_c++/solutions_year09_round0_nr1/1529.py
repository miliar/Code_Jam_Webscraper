#include <iostream>
#include <iterator>
#include <algorithm>
#include <string>
#include <vector>
#include <map>

#include <cmath>

typedef unsigned long long ULL;
typedef long long LL;

using namespace std;

void update_table(map<string, ULL> &table, string &s)
{
	for(unsigned int i = 0; i < s.length(); ++i) {
		++table[s.substr(0, i + 1)];
	}
}

void make_input(vector<char> *input, string &s)
{
	int idx = -1;
	bool inside_paren = false;
	for(string::iterator si = s.begin(); si != s.end(); ++si) {
		if(*si == '(') {
			inside_paren = true;
			++idx;
		} else if(*si == ')') {
			inside_paren = false;
		} else if(inside_paren) {
			input[idx].push_back(*si);
		} else {
			++idx;
			input[idx].push_back(*si);
		}
	}
}

ULL calc_imp(int max, int index, map<string, ULL> &table, vector<char> *input, string s)
{
	if(max == index) {
		return table[s];
	} else if(index != 0 && table.count(s) == 0) {
		return 0;
	} else {
		vector<char> &v = input[index];
		ULL result = 0;
		for(unsigned int i = 0; i < v.size(); ++i) {
			string ts(s);
			ts.push_back(v[i]);
			result += calc_imp(max, index + 1, table, input, ts);
		}
		return result;
	}
}

ULL calc(int max, map<string, ULL> &table, vector<char> *input)
{
	return calc_imp(max, 0, table, input, string(""));
}

int main(void)
{
	int L, D, N;
	cin >> L >> D >> N;
	cin.ignore();

	ULL result = 0;
	string s;
	map<string, ULL> table;

	for(int d = 0; d < D; ++d) {
		getline(cin, s);
		update_table(table, s);
	}

	for(int nn = 0; nn < N; ++nn) {

		vector<char> input[20];
		getline(cin, s);
		make_input(input, s);

		result = calc(L, table, input);

		cout << "Case #" << nn+1 << ": " << result << endl;
	}
	
	return 0;
}
