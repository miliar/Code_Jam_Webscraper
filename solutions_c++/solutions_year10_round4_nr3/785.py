#include <cstdlib>
#include <cstdio>
#include <map>
#include <cstring>

int main()
{
	char* temp = NULL;
	size_t size = 0;
	size_t len = getline(&temp, &size, stdin);
	int cases = atoi(temp);

	int test;
	for (test = 0; test < cases; test++)
	{
		//fprintf(stdout,"Starting %i\n", test);
		int max_x = 0, max_y = 0;
		std::map<int,std::map<int,bool> > grid;
		std::map<int,int> row_alive;
		std::map<int,int> col_alive;

		unsigned long long alive = 0;
		len = getline(&temp, &size, stdin);
		int R = atoi(temp);
		for (int i = 0; i < R; i++)
		{
			len = getline(&temp, &size, stdin);
			char* line = temp;
			int x1 = atoi(strsep(&line, " \r\n"));
			int y1 = atoi(strsep(&line, " \r\n"));
			int x2 = atoi(strsep(&line, " \r\n"));
			int y2 = atoi(strsep(&line, " \r\n"));
			if (max_x < x1) max_x = x1;
			if (max_y < y1) max_y = y1;
			for (int i = x1; i <= x2; i++)
			{
				for (int j = y1; j <= y2; j++)
				{
					grid[i][j] = true;
					row_alive[i] ++;
					col_alive[i] ++;
				}
			}
			alive += (x2-x1+1)*(y2-y1+1);
		}

		int seconds = 0;
		for (; alive; seconds++)
		{
			std::map<int,std::map<int,bool> > newMap;

			//fprintf(stdout,"%llu alive at %i\n", alive, seconds);
			//find cells that are alive
			std::map<int,std::map<int,bool> >::iterator it = grid.begin();
			int rows_found = 0;
			for (; it != grid.end(); it++)
			{
				int i = it->first;
				if (grid[i].begin() == grid[i].end())
				{
					break;
				}
				rows_found ++;
				std::map<int,bool>::iterator alive_it = grid[i].begin();
				for(; alive_it != grid[i].end(); alive_it++)
				{
					if (!alive_it->second) continue;

					//bring neighbour to life if applicable
					if (!grid[i][alive_it->first+1] && grid[i-1][alive_it->first+1])
					{
						newMap[i][alive_it->first+1] = true;
						row_alive[i] ++;
						col_alive[alive_it->first+1] ++;
						alive++;
						//fprintf(stdout,"NOW ALIVE: %i,%i\n", i, alive_it->first+1);
					}

					//kill cell if needed
					if (!grid[i-1][alive_it->first] && !grid[i][alive_it->first-1])
					{
						//newMap[i][alive_it->first] = false;
						row_alive[i] --;
						col_alive[alive_it->first] --;
						alive--;
						//fprintf(stdout,"NOW DEAD: %i,%i\n", i, alive_it->first);
					}
					else
					{
						newMap[i][alive_it->first] = true;
						//fprintf(stdout,"STAYING ALIVE: %i,%i\n", i, alive_it->first);
					}
				}
			}

			if (rows_found == 0) break;
			grid = newMap;
		}

		printf("Case #%i: %i\n", test+1, seconds);
	}
}
