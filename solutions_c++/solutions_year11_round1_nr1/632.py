#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <queue>
#include <set>

using namespace std;

int main()
{
	freopen("C:\\Projects\\gcj\\input.txt", "r", stdin);
	freopen("C:\\Projects\\gcj\\output.txt", "w", stdout);
	int z;
	cin >> z;
	for (int q=0;q<z;q++) {
		long long n, pd, pg;
		cin >> n >> pd >> pg;

		cout << "Case #" << (q+1) << ": ";

		long long num = pd;
		long long den = 100;
		while (1) {
			int val = -1;
			for (int i=2;i<=den;i++) {
				if (num % i == 0 && den % i == 0) {
					val = i;
					break;
				}
			}

			if (val == -1) break;
			num/=val;
			den/=val;
		}

		if (den > n) {
			cout << "Broken" << endl;
			continue;
		}

		if (pg == 100) {
			if (pd == pg)
				cout << "Possible" << endl;
			else 
				cout << "Broken" << endl;
		}
		else if (pg == 0) {
			if (pd == pg)
				cout << "Possible" << endl;
			else 
				cout << "Broken" << endl;
		}
		else 
			cout << "Possible" << endl;
	}

	fclose(stdout);
	fclose(stdin);
	return 0;
}
