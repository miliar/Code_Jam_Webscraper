#include <iostream>
#include <fstream>
#include <algorithm>


long long solve(int start, int end) {
	int m = 1;
	while((start / m )>=10) {
		m = m * 10;
	}
	long long result =0;
	for(int i = start; i < end; ++i) {
		int b = i;
		while(true) {
			int trans_val = b / 10 + (b%10) * m;
			if(trans_val == i) {
				break;
			}
			if(trans_val > i && trans_val <= end) {
				result++;
			}
			b = trans_val;
		}
	}
	return result;
}
int main(int argc , char** argv)
{
	std::ifstream in(argv[1]);
	int count;
	in >> count;
	for(int i = 1; i <=count;++i) 
	{
		int start, end;
		in >> start >> end;

		std::cout << "Case #" << i << ": " << solve(start, end) << std::endl;
	}
	return 0;
}

