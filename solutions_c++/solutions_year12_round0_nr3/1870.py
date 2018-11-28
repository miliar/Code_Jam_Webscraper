#include <cmath>
#include <utility>
#include <set>
#include <iostream>
#include <sstream>

using namespace std;

int main() {
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++) {
		int a, b;
		cin >> a >> b;

		ostringstream oss;
		oss << a;
		int n_digits = oss.str().size();

		set<pair<int,int> > pairs;

		for(int n = a; n <= b; n++) {
			for(int move = 1; move < n_digits; move++) {
				int power = pow((double)10, move);
				int front = n / power;
				int back = n % power;
				
				if(back / (power/10) == 0)
					continue;

				int pow2 = pow((double)10, n_digits-move);
				int recycled = back * pow2 + front;

				if(n == recycled)
					continue;

				if(a <= recycled && recycled <= b) {
					int smaller = (n < recycled ? n : recycled);
					int bigger = (n < recycled ? recycled : n);
					pairs.insert(pair<int,int>(smaller, bigger));
				}
			}
		}
		
		cout << "Case #" << i+1 << ": " << pairs.size() << endl;
	}
	
	return 0;
}
