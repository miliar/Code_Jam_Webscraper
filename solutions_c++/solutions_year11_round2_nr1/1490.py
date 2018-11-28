#include <iostream>
#include <utility>
#include <vector>
#include <fstream>


typedef std::vector<std::vector<char>> Schedule; 

double calculateRow(std::vector<char>& row, int skip)
{
	int totalWin = 0;
	int totalMatch = 0;
	for(int k = 0 ; k < row.size() ; ++k)
	{	
		if (k == skip)
		{
			continue;
		}
		if (row[k] != '.')
		{
			totalMatch++;
			if (row[k] != '0')
			{
				totalWin++;
			}
		}
	}
	return static_cast<double>(totalWin)/totalMatch;
}

std::vector<double> calculateWP(Schedule& schedule)
{
	std::vector<double> WP;
	WP.resize(schedule.size());
	for(int i = 0 ; i < schedule.size() ; ++i)
	{
		WP[i] = calculateRow(schedule[i], -1);
	}

	return WP;
}

std::vector<double> calculateOWP(Schedule& schedule)
{
	std::vector<double> OWP;
	OWP.resize(schedule.size());
	for(int i = 0 ; i < schedule.size() ; ++i)
	{
		double result = 0.0;
		int opponentCount = 0;
		for(int k = 0; k < schedule[i].size() ; ++k)
		{	
			if (schedule[i][k] != '.')
			{
				opponentCount++;
				 result += calculateRow(schedule[k], i);
			}
		}
		OWP[i] = result / opponentCount;
	}
	return OWP;
}

std::vector<double> calculateOOWP(Schedule& schedule, std::vector<double>& OWP)
{
	std::vector<double> OOWP;
	OOWP.resize(schedule.size());
	for(int i = 0 ; i < schedule.size() ; ++i)
	{
		double result = 0.0;
		int opponentCount = 0;
		for(int k = 0; k < schedule[i].size() ; ++k)
		{	
			if (schedule[i][k] != '.')
			{
				opponentCount++;
				result += OWP[k];
			}
		}
		OOWP[i] = result / opponentCount;
	}
	return OOWP;
}

std::vector<double> solveRPI(Schedule& schedule)
{
	std::vector<double>	WP = calculateWP(schedule);
	std::vector<double>	OWP = calculateOWP(schedule);
	std::vector<double>	OOWP = calculateOOWP(schedule, OWP);

	std::vector<double> RPI;
	RPI.resize(schedule.size());
	for (int i = 0 ; i < schedule.size() ; ++i)
	{
		RPI[i] = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
	}
	return RPI;
}

Schedule readData(std::ifstream& stream)
{
	Schedule schedule;
	int N;
	stream >> N;
	schedule.resize(N);
	for (int i = 0 ; i < N ; ++i)
	{
		schedule[i].resize(N);
		for(int k  = 0; k < N ; ++k)
		{
			char c;
			stream >> c;
			schedule[i][k] = c;
		}
	}
	return schedule;
}

void writeResult(std::ofstream& stream, int i, std::vector<double>& result)
{
	stream.setf(0,std::ios::floatfield);            
	stream.precision(10);
	stream << "Case #" << i << ": " << std::endl;
	for (int i = 0 ; i < result.size() ; ++i)
	{
		stream << result[i] <<std::endl;
	}
}

int main()
{
	int T = 0;

	std::ofstream resultStream("outL.txt");
	std::ifstream stream("A-large.in");
	stream >> T;

	for (int i = 0 ; i < T ; ++i)
	{
		Schedule schedule = readData(stream);
		std::vector<double> result = solveRPI(schedule);
		writeResult(resultStream, i + 1, result);
	}

	return 0;
}