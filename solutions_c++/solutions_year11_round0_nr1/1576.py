#include <iostream>
#include <vector>
void solve(int q_no)
{
	int result =0;
	int total_step ;
	int pos_1= 1;
	int pos_2 =1;
	int idx_1 =0;
	int idx_2 =0;
	std::vector<int> act_pos_1 ;
	std::vector<int> act_pos_2;
	std::vector<int> step_1;
	std::vector<int> step_2;

	std::cin >> total_step;
	for(int i =0; i < total_step;++i)
	{
		std::string actor;
		int pos;
		std::cin >> actor;
		std::cin >> pos;
		if(actor[0] == 'O')
		{
			act_pos_1.push_back(pos);
			step_1.push_back(i);
		}
		else
		{
			act_pos_2.push_back(pos);
			step_2.push_back(i);
		}
	}
	int cur_step = 0;
	while(cur_step < total_step)
	{
		result++;
		bool step_inc= false;
		if(idx_1 < step_1.size())
		{
			if(step_1[idx_1] == cur_step && pos_1 == act_pos_1[idx_1])
			{
				step_inc = true;
				idx_1++;
			}
			else
			{
				if(pos_1 > act_pos_1[idx_1])
				{
					pos_1--;
				}
				else if(pos_1 < act_pos_1[idx_1])
				{
					pos_1++;
				}
			}
		}
		if(idx_2 < step_2.size())
		{
			if(step_2[idx_2] == cur_step && pos_2 == act_pos_2[idx_2])
			{
				step_inc = true;
				idx_2++;
			}
			else
			{
				if(pos_2 > act_pos_2[idx_2])
				{
					pos_2--;
				}
				else if(pos_2 < act_pos_2[idx_2])
				{
					pos_2++;
				}
			}
		}
		if(step_inc)
		{
			cur_step++;
		}
	}
	
	std::cout << "Case #" << q_no << ": " << result << "\n"; 
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
