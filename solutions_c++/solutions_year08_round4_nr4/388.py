#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int kases;
	cin >> kases;
	for (int kase=1; kase<=kases; kase++)
	{
		int k;
		string s;
		cin >> k >> s;
		vector<int> perm(k);
		for (int i=0; i<k; i++)
			perm[i] = i;
		int sol = 1000000;
		do
		{
			string target = s;
			for (int i=0; i<(int)s.size(); i+=k)
				for (int j=0; j<k; j++)
					target[i+j] = s[i+perm[j]];
			char prev = '.';
			int val = 0;
			for (int i=0; i<(int)target.size(); i++)
			{
				if (target[i] != prev)
					val++;
				prev = target[i];
			}
			if (val < sol)
				sol = val;
		} while (next_permutation(perm.begin(), perm.end()));
		cout << "Case #" << kase << ": " << sol << endl;
	}
	return 0;
}
