#include <iostream>
#include <math.h>
#include <vector>

using namespace std;
static const int p[8] = {1, 10, 100, 1000, 10000, 100000, 1000000, 2000001};

inline size_t GetPairsCount(const size_t num, pair<size_t, size_t> range, vector<bool>& used) {	
	if (used[num]) return 0;
	used[num] = true;
	size_t ans = 0;
	const size_t pow = (size_t)log10((double)num);
	for (size_t _pow = 1; _pow <= pow; ++_pow){
		const int l = num % p[_pow];
		size_t _num = num / p[_pow] + l * p[pow - _pow + 1];
		if (_num > num && _num >= range.first && _num <= range.second && !used[_num]) {
			used[_num] = true;			
			/*if (ans == 0) cout << num << " -> ";
			cout << _num << " ";*/
			++ans;
		}
	}
	/*if (ans > 0){
		cout << endl;
	}*/
	return ans += ans * (ans - 1) /2;
}

int main(int argc, char* argv[])
{		
	size_t t, a, b;
	cin >> t;
	for (size_t tcase = 1; tcase <= t; ++tcase) {
		cin >> a >> b;
		size_t ans = 0;
		vector<bool> v(p[(int)log10((double)max(a,b))+1], false);
		for (size_t i = a; i <= b; ++i) {
			ans += GetPairsCount(i, make_pair<size_t, size_t>(a, b), v);
		}
		cout << "Case #" << tcase << ": " << ans;  if (tcase != t)	cout << endl;
	}
	return 0;
}