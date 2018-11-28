#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

std::ifstream in( "A-large.in" );
std::ofstream out( "A-large.out");

std::vector<int> num;

int main(void)
{
	int n = 0;
	in >> n;
	for (int i = 0; i != n; ++i)
	{
		int p,k,l;
		in >> p >> k >> l;
		num.resize(l);
		for(int j = 0; j != l; ++j)
			in >> num[j];

		std::sort( num.begin(), num.end() );
		int step = 1;
		int step_in = 1;
		__int64 sum = 0;
		bool result = true;
		for( int j = l-1; j >= 0; --j)
		{
			if( step_in > p || step > k )
			{
				result = false;
				break;
			}
			sum += step_in*num[j];
			step++;
			if( step > k )
			{	
				step = 1;
				step_in++;
			}
		}
		if( !result )
			out << "Case #" << i+1 << ": " << "Impossible" << std::endl;
		else
			out << "Case #" << i+1 << ": " << sum << std::endl;

	}


	return 0;
}