#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>

using namespace std;

template<class T>
class add_xor : public binary_function<T, T, T> {
public:
	result_type operator()(first_argument_type a, second_argument_type b)
		{ return a ^ b; }
};

class CandySplitting {
public:
	unsigned int solve(vector<unsigned int>& data) {
		unsigned int ans = accumulate(data.begin(), data.end(), 0, add_xor<unsigned int>());
		if (ans != 0) return 0;
		sort(data.begin(), data.end());
		ans = accumulate(data.begin() + 1, data.end(), 0);
		return ans;
	}
};

int main()
{
	//fstream fs("test.in");
	//fstream fs("C-small-attempt0.in");
	fstream fs("C-large.in");

	int T, N;
	unsigned int num;
	vector<unsigned int> data;

	CandySplitting test;

	fs >> T;
	for (int i = 0; i < T; i++) {
		fs >> N;
		data.clear();
		for (int j = 0; j < N; j++) {
			fs >> num;
			data.push_back(num);
		}

		unsigned int ans = test.solve(data);

		if (ans == 0) cout << "Case #" << i + 1 << ": NO" << endl;
		else cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}
