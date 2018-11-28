#include <iostream>

using namespace std;

int main()
{
	int T;

	cin >> T;

	for(int t = 0; t < T; t++)
	{
		int N;
		int L;
		int H;

		cin >> N >> L >> H;
		int* p = new int[N];


		for(int n  = 0; n < N; n++)
		{
			cin >> p[n];
		}

			bool success  = false;
			int ans = 0;
			for(int f = L; f <= H; f++)
			{
				for(int n = 0; n < N; n++)
				{
					if(f % p[n] != 0 & p[n] % f != 0)
						break;

					if(n == N-1)
					{
						success = true;
						ans = f;
					}
				}
				if(success)
					break;
			}

			if(!success)
				cout << "Case #" << t+1 << ": NO" << endl;
			else
				cout << "Case #" << t+1 << ": " << ans << endl;


		delete[] p;
	}

	return 0;
}