#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

typedef vector<char> VC;
typedef vector<VC> VVC;

string line;
VVC table;
int has_empty;

void readin()
{
	int i;
	size_t found;
	line.clear();
	table.clear();
	has_empty = 0;
	for (i = 0; i < 4; ++i) {
		getline(cin, line, '\n');
		found = line.find('.');
		if (found != string::npos)
			has_empty = 1;
		VC tmp(line.begin(), line.end());
		table.push_back(tmp);
	}
	// for empty line
	getline(cin, line, '\n');
}

int check(VC buf) {
	int ret = 0;
	int i;
	for (i = 0; i < 4; ++i) {
		if (buf[i] == '.')
			return 0;
		if (buf[i] == 'T')
			continue;
		if (ret == 0)
			ret = buf[i];
		else if (ret != buf[i])
			return 0;
	}
	return ret;
}

void solve()
{
	char ret = 0;
	int i, j;
	// check rows
	for (i = 0; i < 4; ++i) {
		ret = check(table[i]);
		if (ret) {
			cout << ret << " won" << endl;
			return;
		}
	}
	// check columns
	for (i = 0; i < 4; ++i) {
		VC column;
		for (j = 0; j < 4; ++j)
			column.push_back(table[j][i]);
		ret = check(column);
		if (ret) {
			cout << ret << " won" << endl;
			return;
		}
	}
	// check diagonal
	VC diagonal1, diagonal2;
	for (i = 0; i < 4; ++i) {
		diagonal1.push_back(table[i][i]);
		diagonal2.push_back(table[i][3-i]);
	}
	ret = check(diagonal1);
	if (ret) {
		cout << ret << " won" << endl;
		return;
	}
	ret = check(diagonal2);
	if (ret) {
		cout << ret << " won" << endl;
		return;
	}
	if (has_empty)
		cout << "Game has not completed" << endl;
	else
		cout << "Draw" << endl;
}

int main(int argc, char *argv[])
{
	int case_num = 0;

	scanf("%d\n", &case_num);

	for (int case_id = 1; case_id <= case_num; ++case_id) {
		readin();
		cout << "Case #" << case_id << ": ";
		solve();
		cout.flush();
	}

	return 0;
}

