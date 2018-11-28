
#include <string>
#include <vector>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <algorithm>

size_t total = 0;

std::vector<std::string> exist_path;
std::vector<std::string> need_path;

class str_cmp : public std::binary_function<std::string const &, std::string const &, bool>
{
public:
	bool operator()(std::string const &a, std::string const &b) const
	{
		int i = a.compare(b);
		return (i <= 0) ? true : false;
	}
};

void need(std::string & s)
{
	size_t prev_slash = s.rfind("/");

	std::string parent = s.substr(0, prev_slash);

	size_t x = 0;
	if (parent.length())
	{
		for (x = 0; x < exist_path.size(); ++x)
		{
			if (parent.compare(exist_path[x]) == 0) break;
		}
		
		// Not found, queue to create
		if (x == exist_path.size())
		{
			need(parent);
		}
	}
		
	++total;

	exist_path.push_back(s);
	std::sort(exist_path.begin(), exist_path.end(), str_cmp());
}

int main(int argc, char** argv) 
{
	std::ifstream fin("A-large.in");
	std::ofstream fout("A-large.out");

	size_t t;
	fin >> t;

	size_t n, m;
	std::string line;
	for (size_t i = 0; i < t; ++i)
	{
		total = 0;
		exist_path.clear();
		need_path.clear();

		fin >> n >> m;
		getline(fin, line);

		for (size_t j = 0; j < n; ++j)
		{
			getline(fin, line);
			exist_path.push_back(line);
		}

		for (size_t j = 0; j < m; ++j)
		{
			getline(fin, line);
			need_path.push_back(line);
		}

		size_t x;
		std::sort(exist_path.begin(), exist_path.end(), str_cmp());
		for (size_t j = 0; j < need_path.size(); ++j)
		{
			for (x = 0; x < exist_path.size(); ++x)
			{
				if (need_path[j].compare(exist_path[x]) == 0) break;
			}
			if (x != exist_path.size()) continue;
			need(need_path[j]);	
		}

		fout << "Case #" << i + 1 << ": " << total << std::endl;
	}

	fin.close();
	fout.close();

    return (EXIT_SUCCESS);
}

