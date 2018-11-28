
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <list>
#include <algorithm>

using namespace std;


int main()
{
	ifstream in("B-small-attempt0.in");
	//ifstream in("A-small.in");
	ofstream out("B_small.out");

	int T;
	in >> T;

	for (int i=0; i<T; ++i)
	{
		vector<double> pos;
		pos.reserve(1000000);
		double t=0;
		int C; double D;
		in >> C;
		in >> D;
		
		for (int j=0; j<C; ++j)
		{
			int P; int V;
			in >> P; in >> V;
			for (int k=0; k<V; ++k)
			{
				pos.push_back(P);
			}
		}

		while(true)
		{
			bool done = true;
			sort(pos.begin(), pos.end());
			for (size_t j=1; j<pos.size(); ++j)
			{
				if (pos[j] - pos[j-1] < D)
				{
					done = false;
				}
			}

			if (done)
			{
				break;
			}

			if (!done)
			{
				pos[0] -= 0.5;
				pos[pos.size()-1] += 0.5;
				for (size_t j=1; j<pos.size()-1; ++j)
				{
					double d1, d2;
					d1 = pos[j] - pos[j-1];
					d2 = pos[j+1] - pos[j];

					if (d1 == 0 || d2 == 0)
					{
						pos[j] -= 0.5;
					}
					else if (d2 > d1)
					{
						pos[j] += 0.5;
					}
					else
					{
						pos[j] -= 0.5;
					}
				}

				t += 0.5;
			}
		}

		cout << "Case #" << i+1 << ": " << t << endl;
		out << "Case #" << i+1 << ": " << t << endl;
	}

	return 0;
}
