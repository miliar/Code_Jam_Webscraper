#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int T, k;
string S;

int main()
{
	ifstream input;
	ofstream output;
	input.open("D-small.in");
	output.open("D-small.out");

	input >> T;
	for (int c = 0; c < T; c++)
	{
		input >> k;
		input >> S;

		vector<int> perm(k);
		for (int i = 0; i < k; i++)
			perm[i] = i;

		int ans = S.length();
		int n = S.length() / k;
		do
		{
			int c = S.length();
			for (int i = 0; i < n; i++)
				for (int j = 0; j < k - 1; j++)
					if (S[k*i+perm[j]] == S[k*i+perm[j+1]])
						c--;
			for (int i = 0; i < n-1; i++)
				if (S[k*i+perm[k-1]] == S[k*(i+1)+perm[0]])
					c--;
			if (c < ans) ans = c;
		} while (next_permutation(perm.begin(), perm.end()));

		output << "Case #" << c + 1 << ": " << ans << endl;
	}

	input.close();
	output.close();
}
