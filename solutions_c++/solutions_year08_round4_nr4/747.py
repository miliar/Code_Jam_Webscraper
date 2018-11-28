#include <iostream>
#include <cstdio>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;

int p[5];

int calc(string s)
{
	int ret = 1;
	for (int i = 1; i < (int)s.length(); i++)
	{
		if (s[i] != s[i-1])
		{
			ret++;
		}
	}
	return ret;
}

int main()
{
	int N, k;
	string S;

	ifstream fin("D.in");
	ofstream fout("D.out");

	fin >> N;
	for (int ni = 1; ni <= N; ni++)
	{
		fin >> k >> S;
		for (int i = 0; i < k; i++) p[i] = i;
		int n = (int)S.length()/k;
		int best = 987654321;
		do
		{
			string S2 = S;
			for (int i = 0; i < n; i++)
			{
				for (int j = 0; j < k; j++)
				{
					S2[i*k+j] = S[i*k+p[j]];
				}
			}

			int t = calc(S2);
			if (t < best) best = t;

			//for (int i = 0; i < k; i++)
			//{
			//	cout << p[i] << " ";
			//}
			//cout << endl;
			//cout << S2 << " " << t << endl;
		} while(next_permutation(p, p+k));
		fout << "Case #" << ni << ": " << best << endl;
	}

	return 0;
};