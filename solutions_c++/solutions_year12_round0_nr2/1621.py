#include <iostream>
#include <vector>
using namespace std;


int main(int ac, char* av[])
{
	int N; cin >> N;
	for (int x=1;x<=N;x++) {
		int r=0;
		int n, s, p; cin >> n >> s >> p;
		vector<int> v(n);
		for (int i=0; i<n; i++) {
			int t; cin >> t;
			if (((t/3) >= p) || ((t%3) && ((t/3 + 1) >= p))) {
				r++;
			} else {
				// eligible for surprise
				v.push_back(t);
			}
		}
		for (vector<int>::iterator i = v.begin(); i != v.end() && s; ++i) {
			int t =*i;
			// reminder 2 and we can add it to one of the digits
			if ((t%3 == 2) && (t/3+2 >= p)) {
				r++; s--;
			// reminder 0 so we can reduce one number and increase another
			} if ((t%3 == 0) && (t/3 >= 1) && (t/3+1 >= p)) {
				r++; s--;
			}
		}
		cout << "Case #" << x << ": " << r << endl;
	}
	return 0;
}