#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef long long LL;
#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; e<= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n, t) t *v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c, t) for(VAR(i, (c).begin() , t); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second

unsigned int words[5000][15], curr[15];
bool set;

int main()
{
	int L, D, N;
	string temp;

	cin >> L >> D >> N;

	REP(i, D) {
		cin >> temp;
		REP(j, L) {
			words[i][j] = 1 << (temp[j] - 'a');
		}
	}

	int ind;
	REP(cases, N) {
		cin >> temp;
		REP(i, 15) curr[i] = 0;
		ind = 0;
		set = false;
		REP(lett, temp.length()) {
			if (temp[lett] == '(') set = true;
			else
				if (temp[lett] == ')') { set = false; ind++; }
				else {
					curr[ind] |= 1 << (temp[lett] - 'a');
					if (!set) ind++;
				}
		}
		
		int count = D;
		REP(word, D)
			REP(lett, L)
				if ((words[word][lett] & curr[lett]) == 0) {count--; break;};

		cout << "Case #" << (cases+1) << ": " << count << endl;

	}

	return 0;
};