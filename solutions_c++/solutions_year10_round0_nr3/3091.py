#include <iostream>
#include <deque>

using namespace std;

struct Queue {
	int a[1000000], l, r;
	void clear () {
		l = r = 0;
	}
	void push (int x) {
		a[r++] = x;
	}
	int sum (int k) { 
		int s = 0;
		int x = r;
		while (s + a[l] <= k && l < x) a[r++] = a[l++], s += a[l-1];
		return s;
	}
} a;

int main ()
{
	freopen ("c.in", "r", stdin);
	freopen ("c.out", "w", stdout);

        int t, r, k, n, x;
        long long s = 0;

        cin >> t;

        for (int i = 0; i < t; i++) {
        	cin >> r >> k >> n;
        	a.clear();
        	for (int j = 0; j < n; j++) cin >> x, a.push (x);
        	for (int j = 0; j < r; j++) 
        		s += a.sum (k);
		cout << "Case #" << i+1 << ": " << s << endl;
		s = 0; 
        }

	return 0;
}