#include <iostream>
#include <algorithm>

using namespace std;

int perm[32];

int main()
{
	int kases, kase = 0;
	for (cin >> kases; kases; kases--)
	{
		int k;
		string s;
		cin >> k >> s;

		int res = s.size();
		for (int i = 0; i < k; i++)
			perm[i] = i;
		do {
			int blocks = 0;
			char cur = '?';
			for (int b = 0; b < s.size(); b += k)
				for (int i = 0; i < k; i++)
				{
					char act = s[b + perm[i]];
					if (act != cur)
					{
						blocks++;
						cur = act;
					}
				}
			res = min(res, blocks);
		} while (next_permutation(perm, perm+k));
		cout << "Case #" << ++kase << ": " << res << endl;
	}
	return 0;
}
