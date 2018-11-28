/* Rob Keim
    Google Code Jam
	 Online Round 1 */

#include <algorithm>
#include <cassert>
#include <cmath>
#include <deque>
#include <fstream>
#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i, a, b) for (int i = a; i < b; i++)
#define REP(i, n) FOR(i, 0, n)
#define ALL(v) (v).begin(), (v).end()
#define int long int

int main(int argc, char* argv[])
{
	if (argc != 3)
	{
		cout << "\tUSAGE: Program In Out\n";
		exit(1);
	}
	ifstream fin (argv[1]);
	ofstream fout (argv[2]);
	assert(fin != NULL);

	vector<int> v1;
	vector<int> v2;

	int T;
	fin >> T;
	REP(i, T)
	{
		cout << "Case #" << (i + 1) << ": ";
		fout << "Case #" << (i + 1) << ": ";
		v1.clear();
		v2.clear();
		int N;
		fin >> N;
		REP(j, N)
		{
			int tmp;
			fin >> tmp;
			v1.push_back(tmp);
		}
		REP(j, N)
		{
			int tmp;
			fin >> tmp;
			v2.push_back(tmp);
		}
		sort(ALL(v1));
		sort(ALL(v2));
		int sum = 0;
		int one = 0, two = N - 1;
		REP(j, N)
		{
			sum += (v1.at(one)*v2.at(two));
			one++;
			two--;
		}
		cout << sum << endl;

		fout << sum << endl;
	}

	return 0;
}
