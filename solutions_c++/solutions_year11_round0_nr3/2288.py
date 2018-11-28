#include <iostream>
#include <utility>
#include <vector>
#include <fstream>
#include <map>
#include <algorithm>

typedef std::vector<int> Sequence;



std::pair<bool, int> solveSet(Sequence& sequence)
{
	int wrongSum = 0;
	int normalSum = 0;
	std::sort(sequence.begin(), sequence.end());
	std::reverse(sequence.begin(), sequence.end());

	int wrongTotal = 0;
	for (int i = 0 ; i < sequence.size() ; ++i)
	{
		wrongTotal ^= sequence[i];
	}

	if (wrongTotal % 2 == 1)
	{
		return std::make_pair(false, 0);
	}

	wrongTotal /= 2;
	for (int i = 1 ; i < sequence.size() ; ++i)
	{
		int wrongSum = 0;
		int normalSum = 0;
		int wrongMySum = 0;
		for (int k = 0 ; k < sequence.size() - i; ++k)
		{
			normalSum += sequence[k];
			wrongMySum ^= sequence[k];
		}
		for (int k = sequence.size() - 1 ; k >= sequence.size() - i; --k)
		{
			wrongSum ^= sequence[k];
		}
		if (wrongSum == wrongMySum)
		{
			return std::make_pair(true, normalSum);
		}
	}
	return std::make_pair(false, 0);
}

void readData(std::ifstream& stream, Sequence& sequence)
{
	int N = 0;
	stream >> N;
	for (int i = 0 ; i < N ; ++i)
	{
		int value;
		stream >> value;
		sequence.push_back(value);
	}
}

void writeResult(std::ofstream& stream, int i, bool result, int value)
{
	stream << "Case #" << i << ": ";
	if (result)
	{
		stream << value;
	}
	else
	{
		stream << "NO";
	}
	
	stream << std::endl;
}

int main()
{
	int T = 0;

	std::ofstream resultStream("resultL.txt");
	std::ifstream stream("dataL.in");
	stream >> T;

	for (int i = 0 ; i < T ; ++i)
	{
		Sequence seq;
		readData(stream, seq);
		std::pair<bool, int> result = solveSet(seq);
		writeResult(resultStream, i + 1, result.first, result.second);
	}

	return 0;
}