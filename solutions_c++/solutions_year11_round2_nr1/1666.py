#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <iomanip>

char const WON = '1';
char const LOST = '0';
char const NOT_PLAYED = '.';

double winPercent(std::string const& record, int excludeOpponent = -1)
{
	unsigned int gameCount = 0;
	unsigned int winCount = 0;
	for (unsigned int i = 0; i < record.length(); ++i)
	{
		if (static_cast<int>(i) == excludeOpponent)
		{
			continue;
		}

		char const result = record[i];
		if (result != NOT_PLAYED)
		{
			++gameCount;
			if (result == WON)
			{
				++winCount;
			}
		}
	}

	return static_cast<double>(winCount) / static_cast<double>(gameCount);
}

int main()
{
	unsigned int T = 0;
	std::cin >> T;

	for (unsigned int t = 0; t < T; ++t) // for each case
	{
		unsigned int N = 0;
		std::cin >> N;

		typedef std::vector< std::string > Schedule;
		Schedule schedule;

		// For each team, read their record
		for (unsigned int n = 0; n < N; ++n)
		{
			std::string record;
			std::cin >> record;
			schedule.push_back(record);
		}

		// Calculate all WP
		std::vector<double> wp;
		for (unsigned int n = 0; n < N; ++n)
		{
			std::string const& record = schedule[n];
			wp.push_back(winPercent(record));
		}

		// Calculate all OWP
		std::vector<double> owp;
		for (unsigned int n = 0; n < N; ++n) // for each team
		{
			std::string const& record = schedule[n];

			// for each opponent
			unsigned int opponentCount = 0;
			double owpSum = 0;
			for (unsigned int i = 0; i < record.length(); ++i)
			{
				char const result = record[i];
				if (result != NOT_PLAYED)
				{
					++opponentCount;
					owpSum += winPercent(schedule[i], n);
				}
			}
			owp.push_back(owpSum / static_cast<double>(opponentCount));
		}

		// Calculate all OOWP
		std::vector<double> oowp;
		for (unsigned int n = 0; n < N; ++n) // for each team
		{
			std::string const& record = schedule[n];

			// for each opponent
			unsigned int opponentCount = 0;
			double oowpSum = 0;
			for (unsigned int i = 0; i < record.length(); ++i)
			{
				char const result = record[i];
				if (result != NOT_PLAYED)
				{
					++opponentCount;
					oowpSum += owp[i];
				}
			}
			oowp.push_back(oowpSum / static_cast<double>(opponentCount));
		}

		// Calculate all RPI
		std::vector<double> rpi;
		for (unsigned int n = 0; n < N; ++n) // for each team
		{
			double const rpiHere = 0.25 * wp[n] + 0.5 * owp[n] + 0.25 * oowp[n];
			rpi.push_back(rpiHere);
		}

		// Output
		std::ostringstream outputStream;
		outputStream << "Case #" << t + 1 << ":" << std::endl;
		for (std::vector<double>::const_iterator iter = rpi.begin();
				iter != rpi.end();
				++iter)
		{
			outputStream << std::setprecision(12) << (*iter) << std::endl;
		}

		std::string const output = outputStream.str();
		std::cout << output;
		std::cerr << output;
	}

	return 0;
}