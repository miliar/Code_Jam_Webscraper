#include <iostream>
#include <utility>
#include <vector>
#include <fstream>
#include <map>

typedef std::vector<char> Sequence;
typedef std::map<std::pair<char,char>, char> BaseElements;
typedef std::vector<std::pair<char, char>> OpposeElements;

struct MagicSet
{
	BaseElements base;
	OpposeElements oppose;
	Sequence sequence;
};

bool checkSequence(OpposeElements& opposeElements, char first, char second)
{
	for (int i = 0 ; i < opposeElements.size() ; ++i)
	{
		bool aCase = opposeElements[i].first == first && opposeElements[i].second == second;
		bool bCase = opposeElements[i].second == first && opposeElements[i].first == second;
		if (aCase || bCase)
		{
			return true;
		}
	}
	return false;
}

bool checkOppose(MagicSet& set, Sequence invoke, char first)
{
	for (int i = 0 ; i < invoke.size() ; ++i)
	{
		char invokechar = invoke[i];
		if (checkSequence(set.oppose, invokechar, first))
		{
			return true;
		}
	}
	return false;
}

std::pair<bool, char> combine(MagicSet& set, char first, char second)
{
	std::map<std::pair<char,char>, char>::iterator result
		= set.base.find(std::make_pair(first, second));
	if (result == set.base.end())
	{
		result = set.base.find(std::make_pair(second, first));
	}
	if (result == set.base.end())
	{
		return std::make_pair(false, 'O');
	}
	return std::make_pair(true, result->second); 
}

Sequence solveSet(MagicSet& set)
{
	Sequence invoke;
	for (int i = 0 ; i < set.sequence.size() ; ++i)
	{
		if (invoke.size() == 0)
		{
			invoke.push_back(set.sequence[i]);
		}
		else 
		{
			char lastInvoke = invoke[invoke.size() - 1];
			char nextInvoke = set.sequence[i];
			std::pair<bool, char> result = combine(set, lastInvoke, nextInvoke);
			if (result.first)
			{
				invoke.pop_back();
				invoke.push_back(result.second);
			}
			else if (checkOppose(set, invoke, nextInvoke))
			{
				invoke.clear();
			}
			else 
			{
				invoke.push_back(nextInvoke);
			}
		}
	}
	return invoke;
}


void readData(std::ifstream& stream, MagicSet& set)
{
	int C = 0;
	stream >> C;
	for (int i = 0; i < C ; ++i)
	{
		std::pair<char, char> compound;
		char result;
		
		stream >> compound.first;
		stream >> compound.second;
		stream >> result;

		set.base[compound] = result;
	}
	int D = 0;
	stream >> D;
	for (int i = 0; i < D ; ++i)
	{
		char oppose1;
		char oppose2;
		stream >> oppose1 >> oppose2;
		set.oppose.push_back(std::make_pair(oppose1,oppose2));
	}
	int N = 0;
	stream >> N;
	for (int i = 0 ; i < N ; ++i)
	{
		char v;
		stream >> v;
		set.sequence.push_back(v);
	}
}

void writeResult(std::ofstream& stream, int i, Sequence result)
{
	stream << "Case #" << i << ": [";

	for (int i = 0 ; i < result.size() ; ++i)
	{
		if (i != result.size() - 1)
		{
			stream << result[i] << ", ";
		}
		else 
		{
			stream << result[i];
		}
	}

	stream << "]" <<std::endl;
}

int main()
{
	int T = 0;

	std::ofstream resultStream("resultL.txt");
	std::ifstream stream("dataL.in");
	stream >> T;

	for (int i = 0 ; i < T ; ++i)
	{
		MagicSet set;
		readData(stream, set);
		Sequence result = solveSet(set);
		writeResult(resultStream, i + 1, result);
	}

	return 0;
}