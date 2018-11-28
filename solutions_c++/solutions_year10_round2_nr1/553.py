#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
using namespace std;
set<string> existing;

int insert_dir(string& str)
{
	int ops= 0;
	while(str.size())
	{
		if(existing.find(str) != existing.end())
		{
			break;
		}
		existing.insert(str);
		ops +=1;
		str = str.substr(0, str.rfind('/'));
	}
	return ops;
}
long long solve(vector<string>& data)
{
	long long result =0;
	while(data.size())
	{
		result += insert_dir(data.back());
		data.pop_back();
	}
	return result;
}
int main(int argc, char* argv[])
{
	std::ifstream inf(argv[1]);
	int cases ;
	inf >> cases;
	for(int c =0; c< cases;++c)
	{
		std::vector<string> new_dirs;
		existing.clear();
		int a, b;
		inf >> a>> b;
		for(int i =0; i < a; ++i)
		{
			string tmp;
			inf >> tmp;
			insert_dir(tmp);
		}
		for(int i =0; i < b;++i)
		{
			string tmp;
			inf >> tmp;
			new_dirs.push_back(tmp);
		}
		std::cout << "Case #" << c+1 << ": " << solve(new_dirs) << std::endl;
		
	}
	return 0;
}
