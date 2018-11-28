#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int T, N, Pd, Pg;

bool OK() {
    double num, pd;
    pd = Pd * 0.01;
    bool is_lose = false;
    int n = N;
    while (n) {
	num = n * pd;
	if (fabs((int)num - num) < 0.00001) {
	    if ((int)num < n) {
		is_lose = true;
	    }
	    break;
	}
	n--;
    }
    if (is_lose && Pg == 100) return false;
    if ((int)num != 0 && Pg == 0) return false;
    if (n == 0) return false;
    return true;
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    cin >> T;
    for (int i=0; i<T; ++i) {
	cin >> N >> Pd >> Pg;
	cout << "Case #" << i+1 << ": ";
	if (OK())
	    cout << "Possible";
	else cout << "Broken";
	cout << endl;
    }

    return 0;
}
