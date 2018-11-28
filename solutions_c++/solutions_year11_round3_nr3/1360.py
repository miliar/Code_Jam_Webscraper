#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
 	freopen("C-small-attempt0.in", "r", stdin);
 	freopen("C-small-attempt0.out", "w", stdout);
    
    int T, N, L, H, a[10001], res = -1, i, j, k;
    
    cin >> T;
    
    for(i = 0; i < T; i++)
    {
		res = -1;
		cin >> N >> L >> H;
		for(j = 0; j < N; j++)
			cin >> a[j];
		
		for(j = L; j <= H; j++)
		{
			for(k = 0; k < N; k++)
			{
				if(j > a[k]) if(j % a[k] != 0) break;
							else ;
				else if(a[k] % j != 0) break;
			}
			if(k == N)
			{
				res = j;
				break;
			}
		}
		cout << "Case #" << i+1 << ": ";
		if(res == -1)
			cout << "NO" << endl;
		else
			cout << res << endl;
		
		
		
	}
    return 0;
}
