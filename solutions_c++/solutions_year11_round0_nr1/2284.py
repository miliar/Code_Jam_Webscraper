#include <iostream>
#include <utility>
#include <vector>
#include <fstream>

typedef std::pair<char, int> Pair; 
typedef std::vector<Pair> Sequence;



int getFirstTargetOf(Sequence& sequence, int start, char type)
{
	for (int i = start ; i < sequence.size() ; ++i)
	{
		if (sequence[i].first == type)
		{
			return sequence[i].second;
		}
	}
	return 0;
}

int signOfDirection(int start, int end)
{
	if (start <= end)
	{
		return 1;
	}
	return -1;
}

int solveSequence(Sequence& sequence)
{
	int currentBPosition = 1;
	int currentOPosition = 1;
	int totalTime = 0;

	for (int i = 0 ; i < sequence.size(); ++i)
	{
		if (sequence[i].first == 'B')
		{
			int timeOfMovement =  std::abs(sequence[i].second - currentBPosition);
			currentBPosition = sequence[i].second;
			int timePassed = timeOfMovement + 1;
			totalTime += timePassed;
			
			int nextOTarget = getFirstTargetOf(sequence, i + 1, 'O');
			if (std::abs(nextOTarget - currentOPosition) >= timePassed)
			{
				currentOPosition += signOfDirection(currentOPosition, nextOTarget) * timePassed;
			}
			else
			{
				currentOPosition = nextOTarget;
			}
		}
		else
		{
			int timeOfMovement =  std::abs(sequence[i].second - currentOPosition);
			currentOPosition = sequence[i].second;
			int timePassed = timeOfMovement + 1;
			totalTime += timePassed;

			int nextBTarget = getFirstTargetOf(sequence, i + 1, 'B');
			if (std::abs(nextBTarget - currentBPosition) >= timePassed)
			{
				currentBPosition += signOfDirection(currentBPosition, nextBTarget) * timePassed;
			}
			else
			{
				currentBPosition = nextBTarget;
			}
		}
	}

	return totalTime;
}



Sequence readData(std::ifstream& stream)
{
	Sequence sequence;
	int sequenceSize = 0;
	stream >> sequenceSize;

	for (int i = 0; i < sequenceSize ; ++i)
	{
		Pair p;
		stream >> p.first;
		stream >> p.second;
		sequence.push_back(p);
	}
	return sequence;
}

void writeResult(std::ofstream& stream, int i, int result)
{
	stream << "Case #" << i << ": " << result << std::endl;
}

int main()
{
	int T = 0;
	
	std::ofstream resultStream("ResultL.txt");
	std::ifstream stream("DataL.in");
	stream >> T;

	for (int i = 0 ; i < T ; ++i)
	{
		Sequence sequence = readData(stream);
		int result = solveSequence(sequence);
		writeResult(resultStream, i + 1, result);
	}

	return 0;
}