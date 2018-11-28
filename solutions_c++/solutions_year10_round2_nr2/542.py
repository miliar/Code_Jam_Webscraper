#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <cstdlib>
using namespace std;

double pos[50];
double speed[50];
#define ZERO 1e-12
long long solve(int total, int min_suvival, double target, double max_time)
{
	long long result =0;
	double result_time[50];
	int max_possible =0;
	for(int i=0; i < total;++i)
	{
		result_time[i] = (target - pos[i]) / speed[i];
		if(result_time[i] <=max_time + ZERO)
		{
			max_possible+=1;
		}
	}
	if(max_possible < min_suvival)
	{
		return -1;
	}
	int swap_to = total -1;
	for(int i = total -1;min_suvival > 0 && i >=0;--i)
	{
		if(result_time[i] <= max_time + ZERO)
		{
			result += swap_to - i;
			swap_to -= 1;
			min_suvival--;
		}
	}
	return result;
}
int main(int argc, char* argv[])
{
	ifstream inf(argv[1]);
	int cases ;
	inf >> cases;
	for(int case_idx =0; case_idx< cases;++case_idx)
	{
		int a, b;
		double c,d;
		inf >> a>> b>> c>> d;
		for(int i =0; i< a;++i)
		{
			inf >> pos[i];
		}
		for(int i =0; i< a;++i)
		{
			inf >> speed[i];
		}
		long long result = solve(a, b, c,d);
		std::cout << "Case #" << case_idx+1 << ": " ;
		if(result <0)
		{
			std::cout << "IMPOSSIBLE";
		}
		else
		{
			std::cout << result;
		}
		std::cout << std::endl;
	}
	return 0;
}
