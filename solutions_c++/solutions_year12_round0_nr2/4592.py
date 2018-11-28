#include <iostream>
using namespace std;

int main() {
	int N; cin >> N;
	for (int I=0; I<N; ++I) {
		cout << "Case #" << I+1 << ": ";
		int n, s, p; cin >> n >> s >> p;
		int ok=0;
		for (int i=0; i<n; ++i) {
			int num; cin >> num;
			if (p==1) {
				if (num>=1)
					ok++;
			} else if (p==0 or num>=3*p-2) {
				ok++;
			} else if (num>=3*p-4 and s>0) {
				ok++;
				s--;
			}
		}
		cout << ok << endl;
	}
}
