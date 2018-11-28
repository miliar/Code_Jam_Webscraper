#include <iostream>
using std::cin;
using std::cout;


int main()
{
	int t,T;
	
	cin >> T;
	
	for ( t = 0; t < T; t++ )
	{
		int n,N;
		
		cin >> N;

		int bitwise_sum = 0;
		int	sum = 0;
		int min_element = 1000001;
		int c;

		for ( n = 0; n < N; n++ )
		{
			cin >> c;
			bitwise_sum ^= c;
			sum += c;
			min_element = (min_element<c)?min_element:c;
		}
		
		cout << "Case #" << t + 1 << ": ";
		if ( bitwise_sum == 0 )
			cout << (sum - min_element) << "\n";
		else
			cout << "NO\n";
	}
	
	return 0;
}
