#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iterator>
using namespace std;

#define ALL(X) X.begin(), X.end()

int main()
{
	if( freopen("A-large.in", "rt", stdin) ) {
		freopen("A-large.out", "wt", stdout);
	} else 	if( freopen("A-small-attempt.in", "rt", stdin) ) {
		freopen("A-small-attempt.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		cerr << "Case " << i << endl;
		int N;
		cin >> N;
		int rp = 1, op = 1;
		int rb = 0, ob = 0;
		int total_time = 0;
		for(int i = 0; i < N; ++i)	{
			char R; int B;
			cin >> R >> B;
			if(R == 'B') {
				int tm = abs(rp - B) + 1;
				rp = B;
				tm = std::max(1, tm - rb);
				ob += tm;
				total_time += tm;
				rb = 0;
			} else {
				int tm = abs(op - B) + 1;
				op = B;
				tm = std::max(1, tm - ob);
				rb += tm;
				total_time += tm;
				ob = 0;
			}
		}
		cout << "Case #" << i << ": " << total_time << endl;
	}

	return 0;
}