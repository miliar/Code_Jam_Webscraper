#include <iostream>
#include <vector>
#include <stdio.h>
void solve(int q_no)
{
	double result =0;
	long long pos[1000000];
	int total =0;
	int line_c=0;
	int min_dis = 0;
	std::cin >> line_c >> min_dis;
	for(int i =0; i < line_c;++i)
	{
		int val;
		int c;
		std::cin >> val >> c;
		for(int j =0; j< c;++j)
		{
			pos[total] = val;
			total +=1;
		}
	}

	long long max_dist_move = 0;
	
	for(int i = 0; i < total -1;++i)
	{
		if(pos[i+1] - pos[i] < min_dis)
		{
			long long disp = pos[i] + min_dis - pos[i+1];

			pos[i+1] = pos[i] + min_dis;
			if(disp > max_dist_move)
			{
				max_dist_move = disp;
			}
		}
	}
	result = double(max_dist_move) / 2;
	printf("Case #%d: %.8f\n", q_no, result);
}

int main(void)
{
	int count;
	std::cin >> count;
	for(int i =0; i < count;++i)
	{
		solve(i+1);
	}
	return 0;
}
