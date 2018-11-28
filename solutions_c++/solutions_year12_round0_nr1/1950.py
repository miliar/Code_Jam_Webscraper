#include <iostream>
#include <string>

char map[256];
char map1[256];

int main()
{
	const char in[] =  "qz ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
	const char out[] = "zq our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

	for (size_t i = 0 ; i < sizeof(in) - 1 ; ++i)
	{
		if (map[in[i]])
		{
			if (map[in[i]] != out[i])
			{
				std::cout << "ERROR!!!!\n";
				return 1;
			}
		}
		else
		{
			map1[out[i]] = in[i];
			map[in[i]] = out[i];
		}
	}

	for (char i = 'a' ; i <= 'z' ; ++i)
	{
		//std::cout << i << ": " << map[i] << "\n";
		if (!map[i])
			std::cout << "No mapping for in " << i << "\n";
		if (!map1[i])
			std::cout << "No mapping for out " << i << "\n";
	}


	int T;
	std::cin >> T;
	std::string s;
	std::getline(std::cin, s);
	for (int t = 1 ; t <= T ; ++t)
	{
		std::string s;
		std::getline(std::cin, s);
		for (size_t i = 0 ; i < s.size() ; ++i)
		{
			s[i] = map[s[i]];
			if (!s[i])
			{
				std::cout << "ERROR!!!!\n";
				return 1;
			}
		}
		std::cout << "Case #" << t << ": " << s << "\n";
	}
	return 0;
}

