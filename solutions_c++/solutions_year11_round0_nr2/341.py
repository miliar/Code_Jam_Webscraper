#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iterator>
#include <map>
using namespace std;

#define ALL(X) X.begin(), X.end()

int main()
{
	if( freopen("B-large.in", "rt", stdin) ) {
		freopen("B-large.out", "wt", stdout);
	} else 	if( freopen("B-small-attempt.in", "rt", stdin) ) {
		freopen("B-small-attempt.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		cerr << "Case " << i << endl;
		int C;
		cin >> C;
		map<std::pair<char, char>, char> comb;
		set<pair<char, char> > del;
		set<char> can;
		for(int j = 0; j < C; ++j) {
			char c1, c2, c3;
			cin >> c1 >> c2 >> c3;
			comb[std::make_pair(c1, c2)] = c3;
			comb[std::make_pair(c2, c1)] = c3;
		}

		int D;
		cin >> D;
		for(int j = 0; j < D; ++j) {
			char d1, d2;
			cin >> d1 >> d2;
			can.insert(d1);
			can.insert(d2);
			del.insert(make_pair(d1, d2) );
			del.insert(make_pair(d2, d1) );
		}

		int N;
		cin >> N;
		int j = -1;
		char result[101] = {0};
		for(int k = 0; k < N; ++k) {
			cin >> result[++j];
			result[j+1] = '\0';
			if( j == 0) continue;
			map<std::pair<char, char>, char>::iterator f= comb.find(make_pair(result[j], result[j-1]) );
			while(f != comb.end() ) {
				result[j-1] = f->second;
				result[j] = '\0';
				if(0 == --j) break;
				f= comb.find(make_pair(result[j], result[j-1]) );
			}
			if( j == 0) continue;

			while(j > 0 && can.find(result[j]) != can.end() ) {
				bool brk = true;
				for(int p = j - 1; p >= 0; --p)
				if(del.end() != del.find(make_pair(result[j], result[p]) ) ) {
					p = 0;
					j = p-1;
					result[p] = '\0';
					brk = false;
				}
				if(brk) break;
			}
		}

		cout << "Case #" << i << ": [";
		if(j >= 0) {
			for(int k = 0; k < j; ++k) cout << result[k] << ", ";
			cout << result[j];
		}
		cout << ']' << endl;
	}

	return 0;
}