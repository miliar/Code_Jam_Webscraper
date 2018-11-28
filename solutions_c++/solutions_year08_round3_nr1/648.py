#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;


int main(int argc, char *argv[]) {
    int num_cases;

    cin >> num_cases;

    for (int cse = 0 ; cse < num_cases ; ++cse) {
	int P, K, L;
	// TODO insert solution here
	
	cin >> P >> K >> L;

	if (P * K < L) {
	    cout << "Case #" << (cse + 1) << ": Impossible" << endl;
	    continue;
	}


	vector<int> freqs;
	for (int i = 0 ; i < L ; ++i) {
	    int f;
	    cin >> f;

	    freqs.push_back(f);
	}

	sort(freqs.begin(), freqs.end(), greater<int>());

	vector<int> keys(K, 0);

	int min_presses(0);

	for (size_t i = 0 ; i < freqs.size() ; ++i) {
	    ++keys[0];

	    min_presses += freqs[i] * keys[0];

	    sort(keys.begin(), keys.end());
	}

	cout << "Case #" << (cse + 1) << ": " << min_presses << endl;
    }

    return 0;
}
