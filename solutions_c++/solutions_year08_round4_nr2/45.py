#include <iostream>

using namespace std;

int main()
{
    int c;
    cin >> c;
    for (int k = 1; k <= c; ++k) {
	int n, m, a;
	cin >> n >> m >> a;
	if (a > n*m)
	    cout << "Case #" << k << ": IMPOSSIBLE" << endl;
	else if (a == n*m)
	    cout << "Case #" << k << ": " << n << " 0 0 0 0 " << m << endl;
	else
	    cout << "Case #" << k << ": " << a%n << " 0 0 " << a/n
		 << " " << n << " " << a/n + 1 << endl;
    }
}
