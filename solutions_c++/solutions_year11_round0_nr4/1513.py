#include <iostream>

using namespace std;

int main()
{
	int i,j,k,T,N,C;
	cin >> T;
	for (i=0; i<T; i++)
	{
		cin >> N;
		k=0;
		for (j=0; j < N; j++)
		{
			cin >> C;
			if ( C != j+1) k++;
		}
		printf("Case #%d: %d.000000\n", i+1, k);
	}
	return 0;
}