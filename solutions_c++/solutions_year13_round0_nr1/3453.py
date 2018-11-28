#include <fstream>

using namespace std;
enum state{not_over = 1, draw, finished};
state check_line(char *line, char &winner)
{
	char temp = 0;
	state curr_state = state::finished;
	for(int i=0; i < 4; i++)
	{
		if(line[i]=='T')
		{
			continue;
		}
		if(line[i] == '.')
		{
			curr_state = state::not_over;
			break;
		}
		if(!temp)
		{
			temp = line[i];
			continue;
		}
		
		if(temp != line[i])
		{
			curr_state = state::draw;
		}
	}

	if(curr_state == state::finished)
	{
		winner = temp;
	}
	return curr_state;
}

void print_state(int test_id, state curr_state, char winner)
{
	if(curr_state == state::finished)
	{
		printf("Case #%d: %c won\n", test_id, winner);
	}
	else if(curr_state == state::draw)
	{
		printf("Case #%d: Draw\n", test_id);
	}
	else
	{
		printf("Case #%d: Game has not completed\n", test_id);
	}
}
int main(int argc, char * argv[])
{
	char str_game_state[4][5];
	char temp[10];

	fstream file;
	file.open(argv[1]);
	if(file.is_open())
	{
		int total_test = 0;
		file.getline(temp, 10);
		total_test = atoi(temp);

		for(int itr_test = 1; itr_test <= total_test; itr_test++)
		{
			char winner = 0;
			state game_state = state::draw;

			for(int i = 0; i < 4; i++)
			{
				file.getline(str_game_state[i], 5);
				state line_state = check_line(str_game_state[i], winner);
				if(line_state == state::finished)
				{
					game_state = line_state;
					for(++i; i < 4; i++)
					{
						file.getline(str_game_state[i], 5);
					}
					break;
				}

				if(game_state == state::draw)
				{
					game_state = line_state;
				}
			}

			if(game_state != state::finished)
			{
				char lines[6][4] = {{str_game_state[0][0], str_game_state[1][0], str_game_state[2][0], str_game_state[3][0]},
				{str_game_state[0][1], str_game_state[1][1], str_game_state[2][1], str_game_state[3][1]},
				{str_game_state[0][2], str_game_state[1][2], str_game_state[2][2], str_game_state[3][2]},
				{str_game_state[0][3], str_game_state[1][3], str_game_state[2][3], str_game_state[3][3]},
				{str_game_state[0][0], str_game_state[1][1], str_game_state[2][2], str_game_state[3][3]},
				{str_game_state[0][3], str_game_state[1][2], str_game_state[2][1], str_game_state[3][0]}};
				char line[4] = {0};

				for (int i = 0; i < 6; i++)
				{
					state line_state = check_line(lines[i], winner);
					if(line_state == state::finished)
					{
						game_state = line_state;
						break;
					}

					if(game_state == state::draw)
					{
						game_state = line_state;
					}
				}
			}

			print_state(itr_test, game_state, winner);
			file.getline(str_game_state[0], 4);
		}

		file.close();
	}
}