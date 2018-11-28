/*
   Built using boost 1.46.1 and gcc 4.4.3 on 10.04

   usage: ./friendlybots <inputname> > <outputname>
*/

#include <iostream>
#include <fstream>
#include <cstdio>
#include <list>
#include <string>
#include <boost/cstdint.hpp>
#include <boost/spirit/include/qi.hpp>
#include <boost/spirit/include/phoenix_core.hpp>
#include <boost/spirit/include/phoenix_operator.hpp>
#include <boost/spirit/include/phoenix_stl.hpp>

using namespace boost::phoenix;
using namespace boost::spirit;
using namespace boost::spirit::qi;
using namespace boost::spirit::ascii;

enum BotColor
{
	Orange = 0,
	Blue
};

static bool g_buttonPushed = false;
static std::list<std::pair<BotColor, boost::uint16_t> > g_orders;
static std::vector<std::list<std::pair<BotColor, boost::uint16_t> > > g_allCases;

class friendlyBot
{
public:
	friendlyBot(BotColor p_color, std::list<std::pair<BotColor, boost::uint16_t> >& p_orders) :
		m_color(p_color),
		m_currentPosition(1),
		m_positions(),
		m_allOrders(p_orders)
	{
		std::list<std::pair<BotColor, boost::uint16_t> >::iterator iter = p_orders.begin();
		for ( ; iter != p_orders.end(); ++iter)
		{
			if (iter->first == p_color)
			{
				m_positions.push_back(iter->second);
			}
		}
	}

	void doMove()
	{
		if (m_positions.empty())
		{
			return;
		}

		if (m_currentPosition < m_positions.front())
		{
			++m_currentPosition;
		}
		else if (m_currentPosition > m_positions.front())
		{
			--m_currentPosition;
		}
		else
		{
			if (m_allOrders.front().first == m_color &&
				!g_buttonPushed)
			{
				m_positions.pop_front();
				m_allOrders.pop_front();
				g_buttonPushed = true;
			}
		}
	}

private:
	BotColor m_color;
	boost::uint16_t m_currentPosition;
	std::list<int> m_positions;
	std::list<std::pair<BotColor, boost::uint16_t> >& m_allOrders;
};

int main(int argc, char** argv)
{
	if (argc != 2)
	{
		std::cerr << "You need to provide the .in file as input" << std::endl;
		return 1;
	}

	std::ifstream file;
	file.open(argv[1], std::ios::in);

	if (!file.is_open())
	{
		std::cerr << "Couldn't open specified file" << std::endl;
		return 1;
	}

	boost::uint16_t numberOfTestCases;
	std::string numberOfCases;
	
	std::getline(file, numberOfCases);
	if (!phrase_parse(numberOfCases.begin(), numberOfCases.end(), int_[ref(numberOfTestCases) = _1], boost::spirit::ascii::space))
	{
		std::cerr << "Failed to parse the first line in the file" << std::endl;
		return 1;
	}

	std::string testCase;
	for (std::size_t i = 0; i < numberOfTestCases; ++i)
	{
		std::getline(file, testCase);

		int movesInTest = 0;
		std::string::iterator stringIter = testCase.begin();
		std::vector<char> color;
		std::vector<int> moves;
		
		if (!phrase_parse(stringIter, testCase.end(), (int_[ref(movesInTest)= _1] >> +(boost::spirit::ascii::char_[push_back(ref(color), _1)] 
		>> int_[push_back(ref(moves), _1)])), boost::spirit::ascii::space))
		{
			std::cerr << "Failed parsing." << std::endl;
			return 1;
		}

		for (std::size_t i = 0; i < color.size(); ++i)
		{
			if (color[i] == 'O')
			{
				g_orders.push_back(std::make_pair(Orange, moves[i]));
			}
			else if (color[i] == 'B')
			{
				g_orders.push_back(std::make_pair(Blue, moves[i]));
			}
			else
			{
				std::cerr << "Invalid Input" << std::endl;
				return 1;
			}
		}

		g_allCases.push_back(g_orders);
		g_orders.clear();
	}

	for (std::size_t i = 0; i < g_allCases.size(); ++i)
	{
		friendlyBot orange(Orange, g_allCases[i]);
		friendlyBot blue(Blue, g_allCases[i]);
		boost::uint32_t totalMoves = 0;
		for ( ; !g_allCases[i].empty(); ++totalMoves)
		{
			orange.doMove();
			blue.doMove();
			g_buttonPushed = false;
		}

		std::cout << "Case #" << i + 1 << ": " << totalMoves << std::endl;
	}
}
