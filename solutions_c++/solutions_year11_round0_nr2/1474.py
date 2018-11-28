#include <iostream>
#include <set>
#include <map>
#include <vector>
void solve(int q_no)
{
	std::vector<char> result;
	std::set<int> clear;
	std::map<int, char> combine;

	int nm_comb, nm_clear;
	std::cin >> nm_comb;
	for(int i =0; i< nm_comb;++i)
	{
		std::string tmp;
		std::cin >> tmp;
		combine[tmp[0] * 256 + tmp[1]] = tmp[2];
		combine[tmp[1] * 256 + tmp[0]] = tmp[2];
	}
	std::cin >> nm_clear;
	for(int i =0; i < nm_clear;++i)
	{
		std::string tmp;
		std::cin >> tmp;
		clear.insert(tmp[0] * 256 + tmp[1]);
		clear.insert(tmp[1] * 256 + tmp[0]);
	}
	int input_len ;
	std::string input;
	std::cin >> input_len >> input;
	if(input_len != input.size())
	{
		std::cout << "invalid input\n";
	}

	for(int i =0; i < input.size();++i)
	{
		char c = input[i];
		if(result.size() ==0)
		{
			result.push_back(c);
			continue;
		}
		else
		{
			while(1)
			{
				std::map<int, char>::iterator iter = combine.find(result[result.size() -1] * 256 + c);
				if(iter!= combine.end())
				{
					result.pop_back();
					c = iter->second;
				}
				else
				{
					break;
				}
			}
		}
		if(result.size() ==0)
		{
			result.push_back(c);
			continue;
		}
		else
		{
			for(int i =0; i < result.size();++i)
			{
				std::set<int>::iterator iter = clear.find(result[i] * 256 + c);
				if(iter!= clear.end())
				{
					result.clear();
					c =0;
					break;
				}
			}
			if(c!=0)
			{
				result.push_back(c);
			}
		}
	}
	std::cout << "Case #" << q_no << ": [";
	for(int i =0 ; i < result.size();++i)
	{
		std::cout << result[i];
		if(i != result.size() -1)
		{
			std::cout << ", ";
		}
	}
	std::cout  << "]\n"; 
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
