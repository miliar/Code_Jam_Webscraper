#include <iostream>
#include <cstdio>
#include <cmath>

int main()
{
	int Num_of_Cases;
	scanf_s("%d", &Num_of_Cases);

	for( int i = 0; i < Num_of_Cases; ++i )
	{
		int n,k;

		scanf_s( "%d %d", &n, &k );

		if( ((k + 1) % int(pow(2.0, n))) == 0 )
			std::cout << "Case #" << i+1 << ": ON" << std::endl;
		else
			std::cout << "Case #" << i+1 << ": OFF" << std::endl;
	}

}