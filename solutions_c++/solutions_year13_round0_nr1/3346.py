#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char **argv)
{
  ifstream in_file;
  ofstream out_file;
  string read;
  int read_number;

  int nb_test;
  char square[4][4];
  int nb_x = 0;
  int nb_o = 0;
  bool is_draw = true;

  if (argc != 3)
    {
      cout << "Wrong number of arguments" << endl;
      return 1;
    }

  in_file.open(argv[1]);
  out_file.open(argv[2]);

  if (in_file.is_open() == false || out_file.is_open() == false)
    {
      cout << "File cannot be open" << endl;
      return 1;
    }

  in_file >> read_number;
  nb_test = read_number;

  for (int i = 0; i < nb_test; i++)
    {
      in_file >> square[0];
      in_file >> square[1];
      in_file >> square[2];
      in_file >> square[3];

      for (int x = 0; x < 4; x++)
	{
	  for (int y = 0; y < 4; y++)
	    {
	      if (square[x][y] == 'X')
		nb_x++;
	      else if (square[x][y] == 'O')
		nb_o++;
	      else if (square[x][y] == 'T')
		{
		  nb_x++;
		  nb_o++;
		}
	      else
		is_draw = false;
	    }

	  if (nb_x >= 4 || nb_o >= 4)
	    break;
	  nb_x = 0;
	  nb_o = 0;

	  for (int y = 0; y < 4; y++)
	    {
	      if (square[y][x] == 'X')
		nb_x++;
	      else if (square[y][x] == 'O')
		nb_o++;
	      else if (square[y][x] == 'T')
		{
		  nb_x++;
		  nb_o++;
		}
	    }

	  if (nb_x >= 4 || nb_o >= 4)
	    break;
	  nb_x = 0;
	  nb_o = 0;

	  for (int y = 0; y < 4; y++)
	    {
	      if (square[y][y] == 'X')
		nb_x++;
	      else if (square[y][y] == 'O')
		nb_o++;
	      else if (square[y][y] == 'T')
		{
		  nb_x++;
		  nb_o++;
		}
	    }
	  
	  if (nb_x >= 4 || nb_o >= 4)
	    break;
	  nb_x = 0;
	  nb_o = 0;

	  for (int y = 0; y < 4; y++)
	    {
	      if (square[3 - y][y] == 'X')
		nb_x++;
	      else if (square[3 - y][y] == 'O')
		nb_o++;
	      else if (square[3 - y][y] == 'T')
		{
		  nb_x++;
		  nb_o++;
		}
	    }

	  if (nb_x >= 4 || nb_o >= 4)
	    break;
	  nb_x = 0;
	  nb_o = 0;
	}

      out_file << "Case #" << i + 1 << ": ";
      if (nb_x >= 4)
	out_file << "X won" << endl;
      else if (nb_o >= 4)
	out_file << "O won" << endl;
      else if (is_draw)
	out_file << "Draw" << endl;
      else
	out_file << "Game has not completed" << endl;

      nb_x = 0;
      nb_o = 0;
      is_draw = true;
    }
  
  in_file.close();
  out_file.close();

  return 0;
}
