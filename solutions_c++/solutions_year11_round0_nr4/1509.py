#include <iostream>

using namespace std;

int main() {
	int n;

	cin >> n;

	for (int cs = 1; cs <= n; cs++) {
		int nn, p = 0;

		cin >> nn;

		for (int i = 1; i <= nn; i++) {
			int tmp;
			cin >> tmp;
			if (tmp == i) p++;
		}

		cout << "Case #" << cs << ": " << ((nn<=1)?0:(nn-p)) << ".000000" << endl;
	}	


	return 0;
}
