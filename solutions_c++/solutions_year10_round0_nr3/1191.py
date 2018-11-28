#include<iostream>
#include<vector>

using namespace std;

int main()
{
	unsigned T;
	cin >> T;

	vector<unsigned> g;

	for(unsigned x = 1; x <= T; ++x)
	{
		unsigned R, k, N;
		cin >> R >> k >> N;

		g.resize(N);
		for(unsigned i = 0; i < N; ++i)
			cin >> g[i];

		unsigned y = 0;

		for(unsigned i=0, p=0; i<R; ++i)
		{
			unsigned c = 0;

			for(unsigned j = 0; j < N and (c + g[p] <= k); ++j)
			{
				c += g[p];
				p = (p + 1) % N;
			}

			y += c;
		}

		cout << "Case #" << x << ": " << y << "\n";
	}

	return 0;
}