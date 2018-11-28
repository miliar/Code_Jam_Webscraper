#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream in("dancing.in");
	ofstream out("dancing.out");
	int t;
	in >> t;
	for (int test = 1; test <= t; test++)
	{
		int n, s, p, ans = 0;
		in >> n >> s >> p;
		int dancers[150], scores[150];
		for (int i = 0; i < n; i++)
		{
			in >> dancers[i];
			scores[i] = dancers[i] / 3;
			if (dancers[i] % 3 != 0)
				scores[i]++;
			if (scores[i] == p - 1 && s > 0 && dancers[i] > 1)
			{
				ans++;
				s--;
			}
			else if (scores[i] >= p)
				ans++;
		}
		out << "Case #" << test << ": " << ans << "\n";
	}
	return 0;
}