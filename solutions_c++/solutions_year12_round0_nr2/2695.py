#include <fstream>
#include <cmath>

using namespace std;

int main()
{
	int T;
	short int n, s, p;
	short int* t;
	short int r;
	ifstream in("input.in");
	ofstream out("output.out");
	in >> T;
	for (int i = 0; i < T; i++)
	{
		r = 0;
		in >> n >> s >> p;
		t = new short int[n];
		for (int j = 0; j < n; j++)
		{
			in >> t[j];
			t[j] -= p;
			if (int(floor(t[j] / 2.0)) + 1 >= p)
				r++;
			else if (t[j] / 2 + 2 == p)
				if (s > 0)
				{
					s--;
					r++;
				}
		}
		out << "Case #" << i + 1 << ": " << r << endl;
		delete[] t;
	}
	in.close();
	out.close();
	return 0;
}