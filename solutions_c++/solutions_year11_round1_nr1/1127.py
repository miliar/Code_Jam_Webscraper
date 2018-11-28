#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long ull;

ull N, Pd, Pg;

int main()
{
	int t;
	cin >> t;
	int c = 1;
	while(t--) {
		bool right = false;
		cin >> N >> Pd >> Pg;
		if (Pg == 0 && Pd != 0 || Pg == 100 && Pd != 100)
			right = false;
		else if (Pd == 0)
			right = true;
		else {
			for (int Wd = 1; Wd * 100 / Pd <= N; ++Wd) 
				if ((Wd * 100) % Pd == 0) {
					right = true;
					break;
			}
		}
		cout << "Case #" << c++ << ": ";
		if (right) 
			cout << "Possible" << endl;
		else
			cout << "Broken" << endl;
	}
	return 0;
}
