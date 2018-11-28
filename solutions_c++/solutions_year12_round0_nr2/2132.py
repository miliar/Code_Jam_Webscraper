#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>

#define MaxN 100

int T;
int N;
int S;
int p;
std::vector<int> ti;

int main()
{
	std::fstream input;
	std::fstream output;
	input.open( "input.txt", std::istream::in );
	output.open("output.txt", std::ostream::out);

	input >> T;
	for(int t = 0; t < T; t++)
	{
		
		input >> N >> S >> p;
		ti.clear();
		ti.resize(N);
		for(int n = 0; n < N; n++)
		{
			input >> ti[n];
		}
		int out = 0;
		std::sort(ti.begin(),ti.end());
		for(int n = 0; n < N; n++)
		{
			int k = ti[n] / 3;
			int mod = ti[n] % 3;
			if(k >= p)
				out++;
			else
			{
				if(mod != 0 && k + 1 >= p)
					out ++;
				else
				{
					if(S <= 0)
						continue;
					if( (mod != 2 && k !=0 && k + 1 >= p) ||
						(mod == 2 && k + 2 >= p) )
					{
						S--;
						out++;
					}
				}
			}
		}
		
		std::cout << "Case #" << t+1 << ": " << out << std::endl;
		output << "Case #" << t+1 << ": " << out << std::endl;
	}
	getchar();
	return 1;
}