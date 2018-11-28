#include <iostream>
#include <vector>

int	recSearch(std::vector<std::string> grid, int i, int j, char &player, int nb_found, int type)
{
  if (i < 4 && j < 4)
    {
      if (player == 'T' && (grid[i][j] == 'X' || grid[i][j] == 'Y'))
	player = grid[i][j];
      if (grid[i][j] == player || grid[i][j] == 'T')
	{
	  if (nb_found == 2)
	    {
	      std::cout << player << " won" << std::endl;
	      return true;
	    }
	  if (type == 0)
	    return recSearch(grid, i, ++j, player, ++nb_found, type);
	  else if (type == 1)
	    return recSearch(grid, ++i, j, player, ++nb_found, type);
	  else if (type == 2)
	    return recSearch(grid, ++i, ++j, player, ++nb_found, type);
	  else
	    return recSearch(grid, ++i, --j, player, ++nb_found, type);
	}
    }
  return false;
}

void	algo()
{
  std::string line;
  std::vector<std::string> grid(4);

  for (int i = 0; i < 4; ++i)
    {
      std::cin >> grid[i]; 
    }
  bool drawPossible = false;
  bool X_winner = false;
  bool O_winner = false;
  bool result = false;
  for (int i = 0; i < 4; ++i)
    {
      for (int j = 0; j < 4; ++j)
	{
	  if (grid[i][j] == '.')
	    {
	      drawPossible = true;
	    }
	  if (grid[i][j] == 'X' || grid[i][j] == 'O' || grid[i][j] == 'T')
	    {
	      char player = grid[i][j];
	      if (recSearch(grid, i, j + 1, player, 0, 0)
		  || recSearch(grid, i + 1, j, player, 0, 1)
		  || recSearch(grid, i + 1, j + 1, player, 0, 2)
		  || recSearch(grid, i + 1, j - 1, player, 0, 3))
		{
		  result = true;
		  return;
		}
	    }

	}
    }
  if (drawPossible == true)
    std::cout << "Game has not completed" << std::endl;
  else
    std::cout << "Draw" << std::endl;
}

int	main()
{
  int nb_cases;

  std::cin >> nb_cases;
  for (int test_case = 1; test_case <= nb_cases; ++test_case)
    {
      std::cout << "Case #" << test_case << ": ";
      algo();
    }
}
