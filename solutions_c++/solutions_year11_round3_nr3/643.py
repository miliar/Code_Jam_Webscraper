#include <iostream>
#include <string>
#include <vector>
#include <list>

using namespace std;

int main(int argc, char** args)
{
	int T;
	cin >> T;
	
	for (int t = 0; t < T; t++)
	{
		long long N, L, H;
		cin >> N >> L >> H;
		
		vector<long long>	freq;
		freq.reserve(N);
		
		for (long long n = 0; n < N; n++) cin >> freq[n];
		
		long long	f;
		bool		possible = false;
		if (H >= L)
		{
			for (int i = L; i <= H; i++)
			{
				possible = true;
				
				for (long long n = 0; n < N; n++)
					if ((freq[n] % i != 0) && (i % freq[n] != 0))
					{
						possible = false;
						break;
					}

				f = i;
				if (possible) break;
			}
		}

		cout << "Case #" << (t+1) << ": ";		
		if (possible)
			cout << f << endl;
		else
			cout << "NO" << endl;
	}
}

