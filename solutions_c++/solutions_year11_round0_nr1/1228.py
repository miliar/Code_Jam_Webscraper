#include <cstdlib>
#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N, P, i, j, O, B, K = 0, prevO, prevB, X;
	char R;
	cin >> T;
	
	for(i = 0; i < T; i++)
	{
		O = B = K = 0;
		prevO = prevB = 1;
		cin >> N;
		for(j = 0; j < N; j++)
		{
			cin >> R >> P;
			if(R == 'O')
			{
				X = abs(P - prevO) + 1;
				X = (O < X) ? X - O : 1;
				K += X;
				B += X;
				prevO = P;
				O = 0;
			}
			else
			{
				X = abs(P - prevB) + 1;
				X = (B < X) ? X - B : 1;
				K += X;
				O += X;
				prevB = P;
				B = 0;
			}			
			
		}
		cout << "Case #" << i+1 << ": " << K << endl;
	}
    return 0;
}
