#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <queue>
#include <fstream>

using namespace std;

typedef vector <string> vs;
typedef vector <int> vi;
#define REP(a,b) for(long long a=0;a<(b);++a)
#define FOR(a,c,b) for(long long  a=c;a<(b);++a)

const string msg = "welcome to code jam";

int m[501][20];

int main()
{
	//ifstream fin("C-small.in");
	//ofstream fout("C-small.out");
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");

	int t;

	string s;

	fin >> t;

	getline(fin, s);

	for (int tc = 1; tc <= t; ++tc)
	{
		fout <<"Case #"<<tc<<": ";	

		getline(fin, s);

		memset(m, 0, sizeof(m));

		int tot = 0;

		REP(i,s.size()) REP(j,msg.size()) if (s[i] == msg[j]) {
			if (j == 0) m[i][j] = 1;
			else {
				REP(k,i) m[i][j] += m[k][j-1];
				m[i][j] %= 10000;
			}

			if (j == msg.size()-1) tot += m[i][j];
		}

		tot %= 10000;
		
		fout.width(4);
		fout.fill('0');
		fout.setf(ios::right);
		fout << tot << endl;
	}

	fin.close();
	fout.close();

	return 0;
}

