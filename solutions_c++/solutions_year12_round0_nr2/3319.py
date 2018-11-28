#include <cstdlib>
#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	
	int T; 
	cin >> T;
	for(int i = 0; i <  T; i++)
	{
		int N, S, p, t, C = 0;
		cin >> N >> S >> p;
		for(int j = 0; j < N; j++)
		{
			cin >> t;
			int m = t % 3;
			int d = t / 3 + (m > 0);
			if(d >= p) C++;
			else if(m != 1 && d != 0 && S > 0)
				 if(d + 1 >= p) C++, S--;
		}
		cout << "Case #" << i+1 << ": " << C << endl;
	}
    return EXIT_SUCCESS;
}
