#include <iostream>

#define MAX(x, y)	((x) > (y) ? (x) : (y))

//Time to walk from robot's position to the position pos.
inline int walk_time(int &robot_pos, int pos)
{
	const int r = robot_pos - pos;
	robot_pos = pos;
	return (r > 0 ? r : -r);
}

//Read a button
inline int read_button(int &count)
{
	int button;

	std::cin >> button;
	count--;
	return button;
}

//Hash tab, to store bot's pos
static int	pos[256];

int calc_time()
{
	//Number of instructions
	int count;
	std::cin >> count;

	//Totalised time
	int total_time = 0;

	int cml_time = 0;
	char last_bot = 0;
	while(count > 0)
	{
		//Select the bot
		char bot;
		std::cin >> bot;

		int wlk_time = 0;

		//Time to walk and push the button
		int button = read_button(count);
		wlk_time += walk_time(pos[bot], button);

		//If the last robot isn't the same
		if(last_bot != bot)
		{
			if(cml_time > wlk_time)
				wlk_time = 0;
			else
				wlk_time -= cml_time;
			cml_time = 0;
			last_bot = bot;
		}
		cml_time += wlk_time + 1;
		total_time += wlk_time + 1;
	}
	return total_time;
}

int main(void)
{
	int nb_cases;

	//For each cases
	std::cin >> nb_cases;
	for(int i = 1; i <= nb_cases; i++)
	{
		//Get the right time
		pos['O'] = 1;
		pos['B'] = 1;
		int time = calc_time();

		std::cout << "Case #" << i << ": " << time << "\n";
	}
	return 0;
}
