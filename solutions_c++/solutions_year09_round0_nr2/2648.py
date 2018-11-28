#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using std::vector;

class Map
{
public:
	struct Cell
	{
		Cell * sink;
		Cell * trickle_from;
		char sink_label;
		int altitude;
		int h,w;
	};
	Map(int h, int w):height(h),width(w)
	{
		cells.resize(height);
		for(int i = 0; i < height; i++)
		{
			cells.at(i).resize(width);
			for(int j = 0; j < width; j++)
			{
				Cell cell = {NULL,NULL,' ',0,i,j};
				cells.at(i).at(j) = cell;
			}
		}
		label = 'a';
	}
	void set(int h, int w, int val)
	{
		cells[h][w].altitude = val;
	}
	void idBasins()
	{
		for(int h = 0; h<height; h++)
		{
			for(int w = 0; w<width; w++)
			{
				//if the sink isn't NULL, continue;
				if(cells[h][w].sink) continue;
				//else, if the sink is NULL, look for the lower dude until you find the sink
				else
				{
					Cell * current = &cells[h][w];
					Cell * next;
					while(!current->sink)
					{
						//find the lower plane
						int alt = current->altitude;
						char lowest = 'm';
						if(current->h != 0 && cells[current->h-1][current->w].altitude < alt)
						{
							lowest = 'n';
							alt = cells[current->h-1][current->w].altitude;
						}
						if(current->w != 0 && cells[current->h][current->w-1].altitude < alt)
						{
							lowest = 'w';
							alt = cells[current->h][current->w-1].altitude;
						}
						if(current->w != width-1 && cells[current->h][current->w+1].altitude < alt)
						{
							lowest = 'e';
							alt = cells[current->h][current->w+1].altitude;
						}
						if(current->h != height-1 && cells[current->h+1][current->w].altitude <alt)
						{
							lowest = 's';
							alt = cells[current->h+1][current->w].altitude;
						}

						//if nobody else was lower...
						if(lowest == 'm')
						{
							current->sink = current;
							while(current->trickle_from)
							{
								current->trickle_from->sink = current->sink;
								current = current->trickle_from;
							}
							break;
						}

						if(lowest == 'n')
						{
							next = &cells[current->h-1][current->w];
						}
						else if(lowest == 'w')
						{
							next = &cells[current->h][current->w-1];
						}
						else if(lowest == 'e')
						{
							next = &cells[current->h][current->w+1];
						}
						else
						{
							next = &cells[current->h+1][current->w];
						}

						if(next->sink)
						{
							current->sink = next->sink;
							while(current->trickle_from)
							{
								current->trickle_from->sink = current->sink;
								current = current->trickle_from;
							}
							break;
						}
						next->trickle_from = current;
						current = next;
					}
				}
			}
		}
	}

	void labelBasins()
	{
		for(int h = 0; h<height; h++)
		{
			for(int w = 0; w<width; w++)
			{
				if(cells.at(h).at(w).sink->sink_label == ' ')
				{
					cells.at(h).at(w).sink->sink_label = label;
					label++;
				}
				cells.at(h).at(w).sink_label = cells.at(h).at(w).sink->sink_label;
			}
		}
	}
	char getLabel(int h, int w)
	{
		return cells[h][w].sink_label;
	}
	char label;
	const int height;
	const int width;
	vector<vector<Cell> > cells;
};

int main(int argc, char ** argv)
{
	std::ifstream input;	input.open(argv[1]);
	std::ofstream output;	output.open(argv[2]);

	int num_cases;
	input >> num_cases;

	for(int i = 0; i<num_cases; i++)
	{
		int width, height;
		input >> height >> width;
		Map map(height, width);
		int value;

		for(int h = 0; h < height; h++)
		{
			for(int w = 0; w < width; w++)
			{
				input >> value;
				map.set(h,w,value);
			}
		}

		map.idBasins();
		map.labelBasins();

		output << "Case #" << i+1 << ":" << std::endl;
		for(int h = 0; h < height; h++)
		{
			for(int w = 0; w < width; w++)
			{
				output << map.getLabel(h,w) << ' ';
			}
			output << std::endl;
		}
	}
}