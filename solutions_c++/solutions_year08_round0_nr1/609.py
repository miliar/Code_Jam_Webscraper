#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <limits>
#include <iterator>

using namespace std;

int main()
{
	ifstream In("A-large.in");
	ofstream Out("A-large.out");
	unsigned int N = 0;
	In >> N;
	In.ignore(std::numeric_limits<std::streamsize>::max(), In.widen ('\n'));
	for(unsigned int i = 0; i < N; ++i)
	{
		vector<string> Engines;
		unsigned int S = 0;
		In >> S;
		In.ignore(std::numeric_limits<std::streamsize>::max(), In.widen ('\n'));
		for(unsigned int j = 0; j < S; ++j)
		{
			string Engine;
			getline(In, Engine);
			Engines.push_back(Engine);
		}
		vector<string> Queries;
		unsigned int Q = 0;
		In >> Q;
		In.ignore(std::numeric_limits<std::streamsize>::max(), In.widen ('\n'));
		for(unsigned int j = 0; j < Q; ++j)
		{
			string Query;
			getline(In, Query);
			Queries.push_back(Query);
		}
		int Switches = -1;
		while(Queries.size())
		{
			map<string, unsigned int> Occurence;
			for(unsigned int j = 0; j < Engines.size(); ++j)
			{
				Occurence[Engines[j]] = Queries.size();
			}
			for(int j = Queries.size() - 1; j >= 0; --j)
			{
				Occurence[Queries[j]] = j;
			}
			unsigned int Index = 0;
			for(map<string, unsigned int>::const_iterator iter = Occurence.begin(); iter != Occurence.end(); ++iter)
			{
				if(iter->second > Index)
					Index = iter->second;
			}
			++Switches;
			if(Index == 0 || Index == Queries.size())
				break;
			Queries.erase(Queries.begin(), Queries.begin() + Index);
		}
		if(Switches == -1)
			Switches = 0;
		if(i != 0)
			Out << endl;
		Out << "Case #" << i + 1 << ": " << Switches;
	}
	return 0;
}