#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main(int argc, char* argv[])
{
	int N;
	cin >> N;
	for (int i = 0; i < N; i++)
	{
		int P, K, L;
		cin >> P >> K >> L;
		vector<int> f(L);
		for (int l = 0; l < L; l++)
		{
			cin >> f[l]; 
		}
		sort(f.begin(), f.end());
		long long c = 0;
		int l = 1, u = 0, j = 0;
		for (j = L-1; j >= 0; j--)
		{
			c += f[j] * l;
			u++;
			if (u >= K)
			{
				u = 0;
				l++;
				if (l > P && j > 0)
					break;
			}
		}
		if (j > 0)
		{
			cout << "Case #" << (i+1) << ": Impossible" << endl;
		}
		else
		{
			cout << "Case #" << (i+1) << ": " << c << endl;
		}
	}
	return 0;
}
