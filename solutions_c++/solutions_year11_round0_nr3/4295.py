#include <iostream>
#include <list>
#include <algorithm>

using namespace std;

int main() {
    long N;
    cin >> N;

    for (long c = 0; c < N; c++) {
	long C;
	cin >> C;

	long sum = 0, min = 0, min_found = 0;
	long x = 0l;

	for (long i = 0; i < C; i++) {
	    long tmp;
	    cin >> tmp;

	    if ((min > tmp) || (!min_found)) {
		min = tmp;
		min_found = 1;
	    }

	    x ^= tmp;
	    sum += tmp;
	}

        if (x)
            cout << "Case #" << c+1 << ": " << "NO" << endl;
        else
            cout << "Case #" << c+1 << ": " << sum - min << endl;
    }

    return 0;
}
