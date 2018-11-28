#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large2.out", "w", stdout);
	
	int T, N, C, sum = 0, m = 0, i, j, mn = 2000000;
	
	cin >> T;
	
	for(i = 0; i < T; i++)
	{
		cin >> N;
		for(j = 0; j < N; j++)
		{
			cin >> C;
			sum += C, m ^= C;
			mn = min(C, mn);
		}
		if(m == 0)
			cout << "Case #" << i+1 << ": " << sum - mn << endl;
		else
			cout << "Case #" << i+1 << ": NO" << endl;
		mn = 2000000;
		m = sum = 0;
	}
	
    return 0;
}
