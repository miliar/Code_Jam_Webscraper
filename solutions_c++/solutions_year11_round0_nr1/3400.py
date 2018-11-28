#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<sstream>

using namespace std;

int main()
{
	int T;

	std::cin >> T;
	int case_num = 1;

	while (case_num <= T)
	{
		while(1)
		{
		int N,temp=0,total_seconds =0;
		char next_print;
		int OqPos = 0;
		int BqPos = 0;
		int next_O_print = -1;
		int next_B_print = -1;
		int cur_O_Pos = 1;
		int cur_B_Pos = 1;
		std::cin >> N;
		vector<char> Ri(N);
		vector<int> PO,PB;
		int posize=0,pbsize=0;
		while(temp<N)
		{
			std::cin >> Ri[temp];
			if(Ri[temp] == 'O')
			{
				int temp1;
				std::cin >> temp1;
				PO.push_back(temp1);
				posize++;
			}
			else
			{
				int temp1;
				std::cin >> temp1;
				PB.push_back(temp1);
				pbsize++;
			}
			temp++;
		}
		if(!PO.empty())
		{
			next_O_print = PO[OqPos];
		}
		if(!PB.empty())
		{
			next_B_print = PB[BqPos];
		}
		next_print = Ri[0];
		total_seconds = 0;
		int push_count = 0;
		while(push_count < N)
		{
			total_seconds++;
			if(next_print == 'O')
			{
				if(cur_O_Pos == next_O_print)
				{
					OqPos++; // pushing button O
					push_count++;
					if(push_count == N)
						break;
					next_print = Ri[push_count];
					if(OqPos < posize)
					{
					next_O_print = PO[OqPos];
					}
				}
				else if(cur_O_Pos > next_O_print)
				{
					cur_O_Pos--;
				}
				else if(cur_O_Pos < next_O_print)
				{
					cur_O_Pos++;
				}
				if(cur_B_Pos > next_B_print)
				{
					cur_B_Pos--;
				}
				else if(cur_B_Pos < next_B_print)
				{
					cur_B_Pos++;
				}
			}
			else
			{
				if(cur_B_Pos == next_B_print)
				{
					BqPos++; // pushing button O
					push_count++;
					if(push_count == N)
						break;
					next_print = Ri[push_count];
					if(BqPos < pbsize)
					{
					next_B_print = PB[BqPos];
					}
				}
				else if(cur_B_Pos > next_B_print)
				{
					cur_B_Pos--;
				}
				else if(cur_B_Pos < next_B_print)
				{
					cur_B_Pos++;
				}
				if(cur_O_Pos > next_O_print)
				{
					cur_O_Pos--;
				}
				else if(cur_O_Pos < next_O_print)
				{
					cur_O_Pos++;
				}
			}
		}
		std::cout << "Case #" << case_num << ": " << total_seconds << std::endl;
		break;
		}
		case_num++;
	}
	return 1;
}