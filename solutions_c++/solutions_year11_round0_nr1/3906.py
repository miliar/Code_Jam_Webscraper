#include <iostream>
#include <map>
#include <list>
#include <algorithm>
#include <sstream>

enum Bot
{
	Blue = 0,
	Orange = 1,

	BotMax
};

struct ButtonPress
{
	Bot bot;
	unsigned int button;
};

std::istream& operator >> (std::istream& stream, ButtonPress& press)
{
	typedef std::map<char, Bot> BotCharMap;
	BotCharMap botCharMap;
	botCharMap['B'] = Blue;
	botCharMap['O'] = Orange;

	char botChar = 0;
	stream >> botChar;
	press.bot = botCharMap[botChar];

	stream >> press.button;
	
	return stream;
}

typedef std::list<ButtonPress> ButtonPressList;

struct TestCase
{
	ButtonPressList buttonPresses;
};

std::istream& operator >> (std::istream& stream, TestCase& testCase)
{
	unsigned int N = 0;
	stream >> N;
	for (unsigned int n = 0; n < N; ++n)
	{
		ButtonPress press;
		stream >> press;
		testCase.buttonPresses.push_back(press);
	}
	return stream;
}

class BotIs
{
public:
	BotIs(Bot bot)
		:	m_bot(bot)
	{
	}

	bool operator() (ButtonPress const& press) const
	{
		return press.bot == m_bot;
	}

private:
	Bot const m_bot;
};

int main()
{
	// Read number of test cases
	unsigned int T = 0;
	std::cin >> T;

	// Read test cases
	for (unsigned int t = 0; t < T; ++t)
	{
		// Read test case
		TestCase testCase;
		std::cin >> testCase;
		typedef ButtonPressList::const_iterator GoalIterator;
		GoalIterator const goalBegin = testCase.buttonPresses.begin();
		GoalIterator const goalEnd = testCase.buttonPresses.end();

		// Initialize bot states
		struct BotState
		{
			unsigned int location;
			GoalIterator goal;
		};
		typedef std::map<Bot, BotState> BotStateMap;
		BotStateMap botStates;
		for (unsigned int b = 0; b < BotMax; ++b)
		{
			Bot const bot = static_cast<Bot>(b);
			BotState& state = botStates[bot];
			state.location = 1;
			state.goal = std::find_if(goalBegin, goalEnd, BotIs(bot));
		}

		// Solve test case
		unsigned int seconds = 0;
		for (GoalIterator iterGoal = goalBegin;
				iterGoal != goalEnd; // Until all buttons pressed (all goals achieved)
				++seconds) // count how many "seconds" it takes the bots to achieve all goals
		{
			bool buttonPressed = false; // Does a bot press a button during this second?

			// For each bot
			for (BotStateMap::iterator iterBot = botStates.begin(); iterBot != botStates.end(); ++iterBot)
			{
				Bot const bot = iterBot->first;
				BotState& state = iterBot->second;

				// Do nothing if this bot has already pressed all of ITS buttons!
				if (state.goal == testCase.buttonPresses.end())
				{
					continue;
				}

				// If the bot is at the location of the next button that IT needs to press.
				if (state.location == state.goal->button)
				{
					// If THIS bot is the one who needs to press its button next.
					if (bot == iterGoal->bot)
					{
						// This bot spends this second pressing its button!
						buttonPressed = true;

						// Find this bot's next goal, if any.
						GoalIterator next = state.goal; ++next;
						state.goal = std::find_if(next, goalEnd, BotIs(bot));
					} // Otherwise, this bot spends this second waiting at this button.
				}
				else // if this bot is not at the location of the next button that IT needs to press
				{
					// This bot will spend this second moving 1 meter towards the next button that IT needs to press.
					int const diff = (state.goal->button - state.location);
					state.location += (diff / abs(diff));
				}
			}

			if (buttonPressed)
			{
				++iterGoal; // we have achieved this goal, move on to the next (if any)
			}
		}

		std::ostringstream outputStream;
		outputStream << "Case #" << t + 1 <<": " << seconds << std::endl;
		std::string const output = outputStream.str();

		std::cout << output;
		std::cerr << output;
	}

	return 0;
}