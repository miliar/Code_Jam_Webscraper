// \author martin.trenkmann@gmail.com
// $ g++ --std=c++0x gcj2011-r0-pA.cpp
#include <iostream>
#include <list>


struct button_type
{
	char     robot;
	unsigned position;
};

unsigned
min_seconds(std::list<button_type>& button_sequence)
{	
	std::list<unsigned> bs_blue;
	std::list<unsigned> bs_orange;
	for (auto it(button_sequence.begin()); it != button_sequence.end(); ++it)
	{
		switch (it->robot)
		{
		case 'B':
			bs_blue.push_back(it->position);
			break;
		case 'O':
			bs_orange.push_back(it->position);
			break;
		default:;
		}
	}
	
	unsigned seconds    = 0;
	unsigned pos_blue   = 1;
	unsigned pos_orange = 1;
	
	while (!button_sequence.empty())
	{
		++seconds;
		bool skip = false;
		if (button_sequence.front().robot == 'B' &&
		    button_sequence.front().position == pos_blue)
		{
			button_sequence.pop_front();
			bs_blue.pop_front();
			skip = true;
		}
		else if (bs_blue.front() > pos_blue)
		{
			++pos_blue;
		}
		else if (bs_blue.front() < pos_blue)
		{
			--pos_blue;
		}
		
		if (button_sequence.front().robot == 'O' &&
		    button_sequence.front().position == pos_orange && !skip)
		{
			button_sequence.pop_front();
			bs_orange.pop_front();
		}
		else if (bs_orange.front() > pos_orange)
		{
			++pos_orange;
		}
		else if (bs_orange.front() < pos_orange)
		{
			--pos_orange;
		}
	}
	return seconds;
}

int
main(int argc, char* argv[])
{
	unsigned test_case_count;
	std::cin >> test_case_count;
	
	button_type button;
	unsigned sequence_length;
	for (unsigned i = 0; i != test_case_count; ++i)
	{
		std::cin >> sequence_length;
		std::list<button_type> button_sequence;
		for (unsigned j = 0; j != sequence_length; ++j)
		{
			std::cin >> button.robot >> button.position;
			button_sequence.push_back(button);
		}
		std::cout << "Case #" << i+1 << ": "
			      << min_seconds(button_sequence) << std::endl;
	}
}

