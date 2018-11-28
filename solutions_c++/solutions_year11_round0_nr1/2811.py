#include <iostream>
#include <list>

struct SequencePoint
{
	bool blue;
	int button;
	
	SequencePoint(bool b, int bu)
	:blue(b), button(bu)
	{}
};

void update_position(int& cur_pos, int target_pos)
{
	if (cur_pos < target_pos) {cur_pos++;}
	else {if (cur_pos > target_pos) {cur_pos--;}}
}

int get_target(const std::list<SequencePoint>& sequence, bool blue)
{
	for (auto i = sequence.begin(); i != sequence.end(); ++i)
	{
		if (i->blue == blue)
		{
			return i->button;
		}
	}
	
	return -1;
}

unsigned int run_sequence(std::list<SequencePoint>& sequence)
{
	int blue_position = 1;
	int orange_position = 1;
	
	int blue_target = get_target(sequence, true);
	int orange_target = get_target(sequence, false);
	
	bool orange_buttoned = false;
	bool blue_buttoned = false;
	
	unsigned int time_count = 0;
	
	while (sequence.size())
	{
		blue_buttoned = orange_buttoned = false;
		if (sequence.front().blue)
		{
			if (blue_position == blue_target)
			{
				sequence.pop_front();
				blue_target = get_target(sequence, true);
				blue_buttoned = true;
			}
		}
		else
		{
			if (orange_position == orange_target)
			{
				sequence.pop_front();
				orange_target = get_target(sequence, false);
				orange_buttoned = true;
			}
		}

		if (blue_position != blue_target && blue_target > 0 && !blue_buttoned) {update_position(blue_position, blue_target);}
		if (orange_position != orange_target && orange_target > 0 && !orange_buttoned) {update_position(orange_position, orange_target);}
		time_count ++;
	}
	
	return time_count;
}

void read_sequence()
{
	unsigned int sequence_size = 0;
	std::cin >> sequence_size;
	
	std::list<SequencePoint> sequence;
	
	for (sequence_size; sequence_size > 0; --sequence_size)
	{
		char colour;
		int button;
		
		std::cin >> colour;
		std::cin >> button;
		
		sequence.push_back(SequencePoint(colour=='B', button));
	}
	
	std::cout << run_sequence(sequence);
}

int main()
{
	unsigned int num_tests = 0;
	std::cin >> num_tests;
	
	for (int i = 0; i < num_tests; i++)
	{
		std::cout << "Case #" << i+1 << ": ";
		read_sequence();
		std::cout << std::endl;
	}
	
	return 0;
}
