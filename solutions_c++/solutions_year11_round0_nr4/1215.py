#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	
	int T, i, j, N, A, k;
	cin >> T;
	for(i = 1; i <= T; i++)
	{
		k = 0;
		cin >> N;
		for(j = 1; j <= N; j++)
		{
			cin >> A;
			if(A != j) k++;
		}
		cout << "Case #" << i << ": " << k << ".000000" << endl;
	}
		
    return 0;
}
