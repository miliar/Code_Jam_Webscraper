//	Rope Intranet
//

#include <iostream>
#include <iomanip>
#include <vector>

using namespace std;


struct Wire
{
	Wire()
	:	a (0)
	,	b (0)
	{};

	int a, b;	// termini
};


bool intersects(const Wire& wire0, const Wire& wire1)
{
	return
		((wire0.a < wire1.a) && (wire0.b > wire1.b))
	||	((wire0.a > wire1.a) && (wire0.b < wire1.b));
}


int main()
{
	int t;
	cin >> t;
	
	for (int nCase = 1; nCase != (t + 1); ++nCase) {
	
		int n;
		cin >> n;
		
		vector<Wire>  wires (n);

		// Input wires
		for (int i = 0; i != n; ++i) {
			cin >> wires[i].a >> wires[i].b;
		}
		//	Count intersections
		int intCount = 0;
		for (int i = 0; i != (n - 1); ++i) {
			for (int j = (i + 1); j != n; ++j) {
				if (intersects(wires[i], wires[j])) {
					++intCount;
				}
			}
		}

		// Output intersection count
		cout << "Case #" << nCase << ": " << intCount << endl;
	}

	return 0;
}


