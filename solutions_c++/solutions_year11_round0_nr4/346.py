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
	if( freopen("D-large.in", "rt", stdin) ) {
		freopen("D-large.out", "wt", stdout);
	} else 	if( freopen("D-small-attempt.in", "rt", stdin) ) {
		freopen("D-small-attempt.out", "wt", stdout);
	} else ( freopen("test.txt", "rt", stdin) );

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		cerr << "Case " << i << endl;
		int N;
		cin >> N;
		int nums[1000] = {0};
		for (int j = 0; j < N; ++j) cin >> nums[j];
		vector<int> chains;

		for(int j = 0; j < N; ++j) if(nums[j] == j+1) nums[j] = 0;
		for(int j = 0; j < N; ++j) if(nums[j]) {
			int k = 0, v = j, t;
			while(t = nums[v]) ++k, nums[v] = 0, v = t-1;
			chains.push_back(k);
		}
		double t = 0;
		for(vector<int>::size_type j = 0; j < chains.size(); ++j) t += chains[j];
		cout << "Case #" << i << ": ";
		printf("%0.6lf\n", t);
	}

	return 0;
}