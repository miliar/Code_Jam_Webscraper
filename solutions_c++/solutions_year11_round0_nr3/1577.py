#include <iostream>
#include <vector>
void solve(int q_no)
{
	int result = 0;
	int total_num;
	int xor_result =0;
	int smallest =1000000;
	std::cin >> total_num;
	for(int i =0; i < total_num;++i)
	{
		int tmp ;
		std::cin >> tmp;
		if(smallest > tmp)
		{
			smallest = tmp;
		}
		result = result + tmp;
		xor_result = xor_result ^ tmp;
	}
	if(xor_result == 0)
	{
		result = result - smallest;
		std::cout << "Case #" << q_no << ": " << result << "\n";
	}
	else
	{
		std::cout << "Case #" << q_no << ": NO\n";
	}
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
