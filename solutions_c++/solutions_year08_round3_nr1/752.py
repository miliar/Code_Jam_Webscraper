#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

#define MAX_L 1000

using namespace std;

typedef unsigned long long int ull;
typedef long long int ll;

int main()
{
	long num_cases;

	cin >> num_cases;

	for (long icase = 1; icase <= num_cases; icase++)
	{
		int P, K, L;

		cin >> P >> K >> L;

		vector<int> freq;

		for (int i = 0; i < L; i++)
		{
			int l;
			cin >> l;

			if (freq.size() == 0)
				freq.push_back(l);
			else
			{

				vector<int>::iterator it;
				for (it = freq.begin(); it != freq.end(); it++)
				{
					if (*it > l)
					{
						freq.insert(it, l);
						break;
					}
				}

				if (it == freq.end())
					freq.push_back(l);
			}
		}

		int RESULT = 0;

		int mult = 1;
		int i = 1;
		vector<int>::reverse_iterator it;
		for (it = freq.rbegin(); it != freq.rend() && mult <= P; it++)
		{
			RESULT += mult * (*it);
			if (i%K == 0)
				mult++;
			i++;
		}

		if (it != freq.rend())
			cout << "Case #" << icase << ": Imposible" << endl;
		else
			cout << "Case #" << icase << ": " << RESULT << endl;
	}

	return 0;
}
