#include <iostream>
#include <fstream>
long long solve(int rd, int k, int qc, int *q)
{
	int r_count[1000000];
	int r_max=0;
	int start=0;
	while(r_max < rd)
	{
		int end =start;
		int total =0;
		do 
		{
			if((total  + q[end]) <= k)
			{
				total = total + q[end];
				end++;
				if(end ==qc)
				{
					end =0;
				}
			}
			else
			{
				 break;
			}
		} while (end != start);
		r_count[r_max] = total;
		r_max ++;
		if(end == start)
		{
			break;
		}
		start = end;
	}
	int loops = rd / r_max;
	int extras = rd % r_max;
	long long result =0;
	for(int i =0; i < r_max;++i)
	{
		result += r_count[i];
	}
	result = result * loops;
	for(int i =0; i < extras;++i)
	{
		result += r_count[i];
	}
	return result;
}
int main(int argc, char* argv[])
{
        std::ifstream inf(argv[1]);
        int cases ;
        inf >> cases;
	
	for(int i =0 ; i < cases;++i)
	{
		int queue[1000];
		int rd , k;
		int qc;
		inf >> rd >> k >> qc;
		for(int j=0; j < qc;++j)
		{
			inf >> queue[j];
		}
		std::cout << "Case #" << i+ 1 << ": " <<  solve(rd, k, qc, queue) << "\n";
	}
	return 0;
}
