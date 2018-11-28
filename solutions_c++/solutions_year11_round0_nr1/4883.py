#include <iostream>
#include <fstream>
#include <cassert>
#include <sstream>
#include <list>

using namespace std;

void bot(const string& filename, stringstream& out)
{
	ifstream input;
	input.open(filename.c_str());
	assert(input);

	size_t test_cases = 0;
	input >> test_cases;
	assert(test_cases > 0);

	struct SPos
	{
		SPos(size_t position, size_t priority) :  pos(position), prio(priority) {}
		size_t pos;
		size_t prio;
	};

	for (size_t tcase = 1; tcase <= test_cases; ++tcase)
	{
		list<SPos> o_positions;
		list<SPos> b_positions;

		size_t num_buttons;
		input >> num_buttons;
		size_t prio = 0;
		for (size_t button = 0; button < num_buttons; ++button)
		{
			string bot;
			size_t button_num;

			input >> bot;
			input >> button_num;

			assert(bot == "O" || bot == "B");
			assert(button_num > 0 && button_num <= 100);

			if (bot == "O")
				o_positions.push_back(SPos(button_num, ++prio));
			else
				b_positions.push_back(SPos(button_num, ++prio));
		}

		size_t o_pos = 1;
		size_t b_pos = 1;
		bool o_pushed = false;
		bool b_pushed = false;

		SPos o_dest(1,0);
		SPos b_dest(1,0);

		if (!o_positions.empty())
		{
			o_dest = o_positions.front(); o_positions.pop_front();
		}
		else
		{
			o_pushed = true;
		}
		
		if (!b_positions.empty())
		{
			b_dest = b_positions.front(); b_positions.pop_front();
		}
		else
		{
			b_pushed = true;
		}

		size_t time = 0;
		while (!(o_positions.empty() && b_positions.empty() && o_pushed && b_pushed))
		{
			++time;

			if (o_pos == o_dest.pos && o_pushed)
			{
				if (!o_positions.empty())
				{
					o_dest = o_positions.front(); o_positions.pop_front();
					o_pushed = false;
				}
			}

			if (b_pos == b_dest.pos && b_pushed)
			{
				if (!b_positions.empty())
				{
					b_dest = b_positions.front(); b_positions.pop_front();
					b_pushed = false;
				}
			}
			
			if (o_pos == o_dest.pos && (o_dest.prio < b_dest.prio || b_pushed) && !o_pushed)
				o_pushed = true;
			else if (b_pos == b_dest.pos && (b_dest.prio < o_dest.prio || o_pushed) && !b_pushed)
				b_pushed = true;
			
			if (o_pos != o_dest.pos)
				o_pos += o_pos > o_dest.pos ? -1 : 1;
			if (b_pos != b_dest.pos)
				b_pos += b_pos > b_dest.pos ? -1 : 1;
		}

		out << "Case #" << tcase << ": " << time << endl;
	}
}


int main(int argc, char* argv[])
{
	stringstream out;
	bot(".\\A-large.in", out);

	cout << out.str();

	ofstream out_file;
	out_file.open(".\\A-large.out");
	assert(out_file);

	out_file << out.str();

	return 0;
}

