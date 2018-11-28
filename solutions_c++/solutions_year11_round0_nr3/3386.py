#include<iostream>
using namespace std;
#include<algorithm>
#include<queue>
#include<stack>
#include<functional>
#include<string>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<math.h>
#include<vector>
#include<deque>
#include<list>
#include<set>
#include<map>


int numbers[1010];

int main() {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int T, cases = 0, N;
	cin >> T;
	++T;
	while( -- T ) {
		cin >> N;
		int sum = 0;
		for(int i = 0 ; i < N ; ++i) {
			cin >> numbers[i];
			sum += numbers[i];
		}
		int number = numbers[0];
		for(int i = 1 ; i < N ; ++i) {
			number ^= numbers[i];
		}
		cout << "Case #" << ++cases << ": ";
		if( number != 0 ) {
			cout << "NO\n";
		} else {
			cout << sum - *min_element(numbers, numbers+N) << endl;
		}

	}
	return 0;
}