#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

int main(){
	int t, c, d, n;
	std::string tmp, ans, str;
	std::map<char, std::string> combine, opposite;
	std::map<std::string, char> combine_set;
	std::vector<char> invoke;

	std::cin >> t;
	for(int i=0; i < t; ++i)
	{
		combine.clear();
		combine_set.clear();
		opposite.clear();
		invoke.clear();

		std::cin >> c;
		while(c)
		{
			std::cin >> tmp;
			
			combine[tmp[0]] += tmp[1];
			combine[tmp[1]] += tmp[0];

			std::string key = tmp.substr(0, 2);
			combine_set[key] = tmp[2];
			std::reverse(tmp.begin(), tmp.end());
			key = tmp.substr(1, 2);
			combine_set[key] = tmp[0];

			--c;
		}

		std::cin >> d;
		while(d)
		{
			std::cin >> tmp;

			opposite[tmp[0]] += tmp[1];
			opposite[tmp[1]] += tmp[0];

			--d;
		}

		std::cin >> n;
		std::cin >> tmp;
		for(int j=0; j < n; ++j)
		{
			invoke.push_back(tmp[j]);
			int length = invoke.size();

			if(length >= 2 && combine.end() != combine.find(invoke.back()))
			{	
				for(int k=0, max=combine[tmp[j]].size(); k < max; ++k)
				{
					if(combine[tmp[j]][k] == invoke[length - 2])
					{
						str = invoke[length - 2];
						std::string key = str + tmp.substr(j, 1);

						invoke.erase(invoke.begin() + length - 1);
						invoke.erase(invoke.begin() + length - 2);
						invoke.push_back(combine_set[key]);

						break;
					}
				}
			}

			if(opposite.end() != opposite.find(invoke.back()))
			{
				bool f = false;
				char m = invoke.back();
				for(int k=0, max=opposite[m].size(); k < max; ++k)
				{
					for(int l=0, len=invoke.size(); l < len; ++l)
					{
						if(opposite[m][k] == invoke[l])
						{
							invoke.clear();
							f = true;
							break;
						}
					}
					if(f){ break; }
				}
			}
		}

		std::cout << "Case #" << i + 1 << ": [";
		ans = "";
		for(int j=0, max=invoke.size(); j < max; ++j)
		{
			tmp = invoke[j];
			ans += tmp + ", ";
		}
		ans = ans.substr(0, ans.size() - 2);
		ans += "]";
		std::cout << ans << std::endl;
	}

	return 0;
}
