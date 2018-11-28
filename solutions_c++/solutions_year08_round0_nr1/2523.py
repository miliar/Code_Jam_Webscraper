#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

class Case
{
public:
	Case()
	{
	}
	Case(std::istream& ins)
	{
		int n = 0;
		char buff[128];
		ins >> n;
		ins.getline(buff, 100);
		while(n)
		{
			ins.getline(buff, 100);
			SEngs.push_back(buff);
			--n;
		}
		ins >> n;
		ins.getline(buff, 100);
		while(n)
		{
			ins.getline(buff, 100);
			Quers.push_back(buff);
			--n;
		}
	}

	vector<string> SEngs;
	vector<string> Quers;
};



int CalcSwitch(Case& c)
{
	int res = 0;
	int curr_seng = 0;
	map<int, string> mpos;
	
	while(c.Quers.size())
	{
		mpos.clear();
		for(int i = 0; i < c.SEngs.size(); ++i)
		{
			vector<string>::iterator itr = find(c.Quers.begin(), c.Quers.end(), c.SEngs[i]);
			if(itr == c.Quers.end())
				return res;
			else
			{
				int p = itr - c.Quers.begin();
				mpos[p] = c.SEngs[i];
			}
		}
		++res;

		c.Quers.erase(c.Quers.begin(), c.Quers.begin() + mpos.rbegin()->first );
	}
	
	return res;
}

int main()
{
	int nCases = 0;
	cin >> nCases;
	if(!nCases)
		return -1;
	
	int n = nCases;
	vector<Case> vecCases;
	while(n)
	{
		vecCases.push_back(Case(cin));
		--n;
	}

	for(int i = 0; i < nCases; ++i)
	{
		cout << "Case #" << i+1 << ": " << CalcSwitch(vecCases[i]) << std::endl;
	}

	return 0;
}
