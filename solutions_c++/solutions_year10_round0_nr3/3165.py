#include <iostream>

#define	NGROUPS	10

using namespace std;

int main()
{
	unsigned t, r, n, k;
	cin >> t;
	int gr[NGROUPS];
	for (int i=0; i<t; i++) {
		cin >> r >> k >> n;
		for (int j=0; j<n; j++)
			cin >> gr[j];
		
		int pos = 0, sum = 0;
		for (int j=0; j<r; j++) {
			int s = 0, p = pos;
			while (s + gr[p] <= k) {
				s += gr[p];
				p++;
				if (p == n)	p = 0;
				if (p == pos)	break;
			}
			sum += s;
			pos = p;
		}
		
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
	return 0;
}
