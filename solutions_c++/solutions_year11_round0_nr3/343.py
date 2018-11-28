#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <iterator>
using namespace std;

#define ALL(X) X.begin(), X.end()
int candy[1000];

int main()
{
	if( freopen("C-large.in", "rt", stdin) ) {
		freopen("C-large.out", "wt", stdout);
	} else 	if( freopen("C-small-attempt.in", "rt", stdin) ) {
		freopen("C-small-attempt.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		int N;
		cin >> N;
		int val = 0;
		for(int j = 0; j < N; ++j) {
			cin >> candy[j];
			val ^= candy[j];
		}
		if(val)	cout << "Case #" << i << ": " << "NO" << endl;
		else {
			val = 0;
			int min = 1000000;
			for(int j = 0; j < N; ++j) {
				if(candy[j] < min) min = candy[j];
				val += candy[j];
			}
			cout << "Case #" << i << ": " << val - min << endl;
		}
	}

	return 0;
}