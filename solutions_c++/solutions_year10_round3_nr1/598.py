#include <iostream>

#define MAXWIRES 2000

using std::cin;
using std::cout;
using std::endl;

typedef struct {
	int i, f;
} wire;

// Number of test cases
int t = 0, num = 1;
// Number of wires
int n = 0;
// Wires
wire wires[MAXWIRES];

int main()
{
	cin >> t;

	while (num <= t) {
		cin >> n;

		for (int i = 0; i < n; i++) {
			cin >> wires[i].i >> wires[i].f;
		}

		int res = 0;
		for (int i = 0; i < (n-1); i++) {
			for (int j = i+1; j < n; j++) {
				if ((wires[j].i < wires[i].i && wires[j].f > wires[i].f) || 
					(wires[j].i > wires[i].i && wires[j].f < wires[i].f))
					res++;
			}
		}

		cout << "Case #" << num << ": " << res << endl;

		num++;
	}

	return 0;
}
