#include <iostream>

using namespace std;

void Problem_2 () {
	int cases;
	cin >> cases;

	for (int k = 1; k <= cases; ++k) {
		int n, s, p, num;
		cin >> n >> s >> p;

		int L1 = p + 2 * (p-1 > 0 ? p-1 : 0),
			L2 = p + 2 * (p-2 > 0 ? p-2 : 0);
		int result = 0;

//		cout << "(" << n << "," << s << "," << p << ")[" << L1 << "," << L2 << "]";
		for (int i = 0; i < n; ++i) {
			cin >> num;
			if (num >= L1) 
				++result;
			else if (num >= L2) {
				if (s > 0) {
					--s;
					++result;
				}
			}
//			cout << num << ",";
		}
		cout << "Case #" << k << ": " << result << endl;
		
	}
}

int main () {
	Problem_2 ();
	return 0;
}