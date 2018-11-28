#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct WireType  {
	size_t left;
	size_t right;
};

int main ()
{
	freopen ("A.in", "r", stdin);
	freopen ("A.out", "w", stdout);

	size_t szT(0);
	cin >> szT;

	vector<WireType> vWires;
	vWires.reserve(1000);

	for (size_t szCaseId = 0; szCaseId < szT; ++szCaseId)  {

		size_t szN(0);
		cin >> szN;

		for (size_t i = 0; i < szN; ++i)  {

			WireType wire;

			cin >> wire.left;
			cin >> wire.right;

			vWires.push_back(wire);
		}

		size_t szY(0);

		for (size_t i = 0; i < szN - 1; ++i)  {

			for (size_t j = i + 1; j < szN; ++j)  {

				if ((vWires[i].left > vWires[j].left && vWires[i].right < vWires[j].right)  ||
					(vWires[i].left < vWires[j].left && vWires[i].right > vWires[j].right))  {

						szY++;
				}
			}
		}
		
		cout << "Case #" << szCaseId + 1 << ": " << szY << endl;

		vWires.clear();
	}

	return 0;
}