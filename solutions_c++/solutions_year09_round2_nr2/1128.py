#include<iostream>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

int next(vector<int> & N, int const len)
{
	if(len == 1)
	{
		N.push_back(0);
		return len + 1;
	}

	int i = len - 2;
	do
	{
		int j = i + 1,
			nd = 10,
			np;

		do
		{
			if(nd > N[j] and N[j] > N[i])
			{
				nd = N[j];
				np = j;
			}

			++j;
		}
		while(j < len);

		if(nd < 10)
		{
			N[np] = N[i];
			N[i] = nd;
			
			vector<int>::iterator ii = N.begin();
			advance(ii, i + 1);

			sort(ii, N.end());

			return len;
		}

		--i;
	}
	while(i >= 0);

	N.push_back(0);

	sort(N.begin(), N.end());

	for(i = 1; N[i] == 0; ++i);

	N[0] = N[i];
	N[i] = 0;

	return len + 1;
}

int main()
{
	int T;
	cin >> T;

	string line;
	vector<int> N;

	for(int X = 1; X <= T; ++X)
	{
		cin >> line;

		int s = line.length();

		N.resize(s);

		for(int i = 0; i < s; ++i)
			N[i] = line[i] - '0';

		s = next(N, s);

		cout << "Case #" << X << ": ";

		for(int i = 0; i < s; ++i)
			cout << N[i];

		cout << '\n';
	}
}