#include <map>
#include <set>
#include <string>
#include <iostream>

using std::string;

int main()
{
	int t;
	std::cin >> t;
	for (int currtest = 1; currtest <= t; currtest++)
	{
		std::map<string, char> comb;
		std::set<string> anih;
		
		int ncomb;
		std::cin >> ncomb;
		for (int i = 0; i < ncomb; i++)
		{
			string s;
			std::cin >> s;
			comb[s.substr(0, 2)] = s[2];
			char x = s[0]; s[0] = s[1]; s[1] = x;
			comb[s.substr(0, 2)] = s[2];
		}
		
		int nanih;
		std::cin >> nanih;
		for (int i = 0; i < nanih; i++)
		{
			string s;
			std::cin >> s;
			anih.insert(s);
			char x = s[0]; s[0] = s[1]; s[1] = x;
			anih.insert(s);
		}
		
		int len;
		std::cin >> len;
		
		string s;
		std::cin >> s;
		
		string curr;
		for (int i = 0; i < (int)s.size(); i++)
		{
			if (!curr.size()) {curr += s[i]; continue;}
			
			string l2 = "  ";
			l2[0] = curr[curr.size()-1];
			l2[1] = s[i];
			
			if (comb.find(l2) != comb.end()) {curr[curr.size()-1] = comb[l2]; continue;}
			
			bool exit = false;
			for (int j = 0; j < (int)curr.size(); j++)
			{
				string l2 = "  ";
				l2[0] = s[i];
				l2[1] = curr[j];
				
				if (anih.find(l2) != anih.end()) {curr = ""; exit = true; break;}
			}
			
			if (!exit) curr += s[i];
		}
		
		std::cout << "Case #" << currtest << ": [";
		for (int i = 0; i < (int)curr.size(); i++)
		{
			if (i) std::cout << ", ";
			std::cout << curr[i];
		}
		std::cout << "]\n";
	}

	return 0;
}
