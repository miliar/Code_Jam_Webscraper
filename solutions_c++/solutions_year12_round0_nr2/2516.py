#include <iostream>
#include <fstream>
#include <algorithm>


int solve(int* d, int size, int s, int p) {
	int result =0;
	std::sort(d, d + size, std::greater<int>());
	for(int i =0; i < size;++i) {
		if(((d[i] + 2 ) /3) >=p) {
			result++;
		}
		else if(d[i] >=2 && s >0 && ((d[i] +4)/ 3 ) >=p)
		{
			s--;
			result++;
		}
		else
		{
			break;
		}
	}
	return result;
}
int main(int argc , char** argv)
{
	std::ifstream in(argv[1]);
	int count;
	in >> count;
	int data[100];
	for(int i = 1; i <=count;++i) 
	{
		int size, s, p;
		in >> size >> s >> p;
		for(int j = 0; j < size; ++j) {
			in >> data[j];
		}
		std::cout << "Case #" << i << ": " << solve(data, size, s, p) << std::endl;
	}
	return 0;
}

