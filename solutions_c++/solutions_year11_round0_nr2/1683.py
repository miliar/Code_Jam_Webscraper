#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;

#define sz(a) int(a.size())
#define rep(i, b, e) for ((i) = (b); (i) < (e); ++(i))
#define dump(a) cerr << #a << " = " << (a) << endl

int main()
{
	int tests, test_num;
	cin >> tests;
	rep(test_num, 1, tests + 1)
	{
		int C, D, N, i, j;
		cin >> C;
		int comb[26][26], confl[26][26];
		rep(i, 0, 26)
			rep(j, 0, 26)
				comb[i][j] = confl[i][j] = -1;
		rep(i, 0, C) 
		{
			string s;
			cin >> s;
			comb[s[0] - 'A'][s[1] - 'A'] = s[2];
			comb[s[1] - 'A'][s[0] - 'A'] = s[2];
		}
		cin >> D;
		rep(i, 0, D)
		{
			string s;
			cin >> s;
			confl[s[0] - 'A'][s[1] - 'A'] = 1;
			confl[s[1] - 'A'][s[0] - 'A'] = 1;
		}
		cin >> N;
		string seq;
		cin >> seq;
		vector <char> l;
		l.push_back(seq[0]);
		rep(i, 1, sz(seq))
		{
			if (comb[seq[i] - 'A'][l[sz(l) - 1] - 'A'] >= 0)
				l[sz(l) - 1] = comb[seq[i] - 'A'][l[sz(l) - 1] - 'A'];
			else 
				l.push_back(seq[i]);
			rep(j, 0, sz(l))
				if (confl[l[j] - 'A'][l[sz(l) - 1] - 'A'] == 1) 
				{
					l.clear();
					break;
				}
		}
		cout << "Case #" << test_num << ": [";
		rep(i, 0, sz(l) - 1)
			cout << l[i] << ", ";
		if (sz(l) >= 1)
			cout << l[sz(l) - 1];
		cout << "]" << endl;
	}
	return 0;
}
