
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream in("A-large.in");
	ofstream out("A_large.txt");
	
	int T;
	in >> T;

	for (int i=0; i<T; ++i)
	{
		int N;
		in >> N;

		vector<pair <char, int> > pairs;

		for (int j=0; j<N; ++j)
		{
			char r;
			int b;
			in >> r; in >> b;
			pairs.push_back(pair<char, int>(r,b));
		}

		int oPos = 1; int bPos = 1;
		int t = 0;
		int nextO = -1; int nextB = -1;
		int nextOPos = -1; int nextBPos = -1;

		for (int j=0; j<N;)
		{
			if (nextO < j)
			{
				for (int k=j; k<N; ++k)
				{
					if (pairs[k].first == 'O')
					{
						nextO = k;
						nextOPos = pairs[k].second;
						break;
					}
				}
			}

			if (nextB < j)
			{
				for (int k=j; k<N; ++k)
				{
					if (pairs[k].first == 'B')
					{
						nextB = k;
						nextBPos = pairs[k].second;
						break;
					}
				}
			}

			if ((nextO == j && nextOPos == oPos) || (nextB == j && nextBPos == bPos))
			{
				++j;
			}

			if (nextO >= j)
			{
				if (oPos > nextOPos) --oPos;
				if (oPos < nextOPos) ++oPos;
			}

			if (nextB >= j)
			{
				if (bPos > nextBPos) --bPos;
				if (bPos < nextBPos) ++bPos;
			}

			++t;
		}

		cout << "Case #" << i+1 << ": " << t << endl;
		out << "Case #" << i+1 << ": " << t << endl;
	}

	return 0;
}
