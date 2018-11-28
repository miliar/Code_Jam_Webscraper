#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <math.h>


using namespace std;


struct Robot {
	int x, t;

	
	Robot(): x(1), t(0) {};


	void push(int v, const Robot& r) {
		t += abs(x - v) + 1;
	    x = v;
	    if (t <= r.t) {
	    	t = r.t + 1;
	    }
	}
};


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int k;
	cin >> k;
	for (int counter = 1; counter <= k; counter++) {
		Robot o, b;
		string color;
		int v, n;
		cin >> n;
		for (int i = 0; i < n; i++) {
			cin >> color >> v;
			if (color == "O") {
				o.push(v, b);
			} else {
				b.push(v, o);
			}
		}
		cout << "Case #" << counter << ": " << max(o.t, b.t) << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}