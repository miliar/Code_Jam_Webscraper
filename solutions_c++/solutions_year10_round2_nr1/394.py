#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using std::string;
using std::vector;

vector<string> parents(const string& path)
{
	vector<string> ans;
	for (size_t i = 1; i < path.size(); i++)
		if (path[i] == '/')
			ans.push_back(path.substr(0, i));
			
	return ans;
}

int main()
{
	int ntests;
	std::cin >> ntests;
	for (int testcase = 1; testcase <= ntests; testcase++)
	{
		int n, m;
		std::cin >> n >> m;
		vector<string> dirs(n);
		for (int i = 0; i < n; i++) std::cin >> dirs[i];
		
		std::sort(dirs.begin(), dirs.end());
		
		int c = 0;
		for (int i = 0; i < m; i++)
		{
			string curr;
			std::cin >> curr;
			if (std::binary_search(dirs.begin(), dirs.end(), curr)) continue;
			
			vector<string> pars = parents(curr);
			
			for (size_t i = 0; i < pars.size(); i++)
				if (!std::binary_search(dirs.begin(), dirs.end(), pars[i]))
					{c++; dirs.insert(std::lower_bound(dirs.begin(), dirs.end(), pars[i]), pars[i]);}
					
			c++; dirs.insert(std::lower_bound(dirs.begin(), dirs.end(), curr), curr);
		}
		
		std::cout << "Case #" << testcase << ": " << c << '\n';
	}

	return 0;
}
