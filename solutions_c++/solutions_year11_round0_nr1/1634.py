#include <boost/format.hpp>
#include <boost/lexical_cast.hpp>
#include <iostream>
#include <string>
#include <list>

typedef std::list<std::pair<int, int>> cmd_t;


void advance_sim(
	int & time,
	int & seq,
	const int distO,
	const int distB,
	cmd_t & cmdO,
	cmd_t & cmdB,
	int & locO,
	int & locB
	)
{
	int dT = distO+1;

	if(distB < dT)
	{
		locB = cmdB.front().second;
	}
	else
	{
		if(cmdB.front().second - locB > 0)
		{						
			locB += dT;
		}
		else
		{
			locB -= dT;
		}
	}

	locO = cmdO.front().second;

	time += dT;
	++seq;
}


void finish_sim(
	int & time,
	int & seq,
	cmd_t cmd,
	int & loc)
{
	while(!cmd.empty())
	{
		int dist = abs(cmd.front().second - loc);

		time += dist+1;
		loc = cmd.front().second;

		seq++;
		cmd.pop_front();
	}
}

int main(int argc, char * argv[])
{
	std::string line;

	std::getline(std::cin, line);

	int T = boost::lexical_cast<int>(line);

	std::stringstream buf;

	for(int i = 0; i < T; ++i)
	{
		cmd_t cmdO;
		cmd_t cmdB;
		std::getline(std::cin, line);

		buf.clear();
		buf.str(line);

		int N;
		buf >> N;

		for(int j = 0; j < N; ++j)
		{
			char bot;
			int button;
			buf >> bot >> button;

			switch(bot)
			{
			case 'O':
				cmdO.push_back(std::make_pair(j, button));
				break;
			case 'B':
				cmdB.push_back(std::make_pair(j, button));
				break;
			default:
				throw;
			}
		}

		int seq = 0;

		int locO = 1;
		int locB = 1;
		int time = 0;
		while(1)
		{
			if(cmdO.empty() && cmdB.empty()) break;
			
			if(cmdO.empty())
			{
				finish_sim(
					time,
					seq,
					cmdB,
					locB);
				break;
			}
			if(cmdB.empty())
			{
				finish_sim(
					time,
					seq,
					cmdO,
					locO);
				break;
			}
			int distO = abs(cmdO.front().second - locO);
			int distB = abs(cmdB.front().second - locB);

			if(cmdO.front().first == seq)
			{
				advance_sim(
					time,
					seq,
					distO,
					distB,
					cmdO,
					cmdB,
					locO,
					locB);

				cmdO.pop_front();
			}
			else if(cmdB.front().first == seq)
			{				
				advance_sim(
					time,
					seq,
					distB,
					distO,
					cmdB,
					cmdO,
					locB,
					locO);

				cmdB.pop_front();
			}
			else
				throw;
		}

		std::cout << boost::format("Case #%d: %d\n") % (i+1) % time;
	}

	return 0;
}
