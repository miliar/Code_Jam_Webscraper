#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> num;

int solve(int pos = 0) 
{
	static int first, second;
	static int sum1, sum2;
	static int sum;
	if (!pos) {
		first = second = sum1 = sum2 = sum = 0;
	}
	else if (pos == num.size()) {
		return first == second && sum1 && sum2 ? sum1 : 0 ;
	}
	
	int old = first;
	first ^= num[pos];
	sum1 += num[pos];
	int ans1 = solve(pos+1);
	sum1 -= num[pos];
	first = old;
	
	old = second;
	second ^= num[pos];
	sum2 += num[pos];
	int ans2 = solve(pos+1);
	sum2 -= num[pos];
	second = old;
	
	return max(ans1, ans2);
}

int main(int argc, char **argv) 
{
	int T;
	cin >> T;
	for (int t=1; t<=T; ++t) {
		int N;
		cin >> N;
		num.resize(N);
		for (int i=0; i<N; ++i) {
			cin >> num[i];
		}
		sort(num.begin(), num.end());
		int ans = solve();
		if (ans) {
			cout << "Case #" << t << ": " << ans << endl;
		}
		else {
			cout << "Case #" << t << ": NO" << endl;
		}
	}
    return 0;
}
