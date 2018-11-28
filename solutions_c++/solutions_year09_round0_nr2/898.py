#include <iostream>
#include <fstream>
#include <iomanip>
#include <string>
#include <vector>

int main()
{
	std::ifstream in("input.txt");

	int map_count;
	in >> map_count;

	int neighbours[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};

	std::ofstream out("output.txt");
	for (int map_index = 0; map_index < map_count; ++map_index)
	{
		int width, height;
		in >> height >> width;

		std::vector<std::vector<int> > map(height);
		std::fill(map.begin(), map.end(), std::vector<int>(width));

		for (int y = 0; y < height; ++y)
		{
			for (int x = 0; x < width; ++x)
			{
				int alt;
				in >> alt;

				map[y][x] = alt;
			}
		}

		std::vector<std::vector<int> > basins(height);
		std::fill(basins.begin(), basins.end(), std::vector<int>(width));
		int basin_index = 0;
		for (int y = 0; y < height; ++y)
		{
			for (int x = 0; x < width; ++x)
			{
				basins[y][x] = basin_index++;
			}
		}

		for (int start_y = 0; start_y < height; ++start_y)
		{
			for (int start_x = 0; start_x < width; ++start_x)
			{
				int x = start_x, y = start_y;
				for (;;)
				{
					int min_alt = map[y][x];
					int min_neighbour_index = -1;
					for (int neighbour_index = 0; neighbour_index < 4; ++neighbour_index)
					{
						int neighbour_x = x + neighbours[neighbour_index][0], neighbour_y = y + neighbours[neighbour_index][1];
						if (neighbour_x >= 0 && neighbour_x < width && neighbour_y >= 0 && neighbour_y < height)
						{
							int neighbour_alt = map[neighbour_y][neighbour_x];
							if (neighbour_alt < min_alt)
							{
								min_alt = neighbour_alt;
								min_neighbour_index = neighbour_index;
							}
						}
					}

					if (min_neighbour_index < 0)
						break;
					{
						int neighbour_x = x + neighbours[min_neighbour_index][0], neighbour_y = y + neighbours[min_neighbour_index][1];
						x = neighbour_x;
						y = neighbour_y;
					}
				}

				int basin_id = basins[y][x];
				basins[start_y][start_x] = basin_id;
			}
		}

		out << "Case #" << map_index + 1 << ":\n";

		int next_label = 0;
		std::vector<int> basin_labels(width * height);
		std::fill(basin_labels.begin(), basin_labels.end(), -1);
		for (int y = 0; y < height; ++y)
		{
			for (int x = 0; x < width; ++x)
			{
				int basin_id = basins[y][x];
				if (basin_labels[basin_id] == -1)
					basin_labels[basin_id] = next_label++;
				int basin_label = basin_labels[basin_id];
				char basin_char = 'a' + basin_label;

				out << basin_char;
				if (x < width - 1)
					out << ' ';
			}

			out << "\n";
		}
	}
}
