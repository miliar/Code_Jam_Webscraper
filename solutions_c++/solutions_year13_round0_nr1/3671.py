#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <algorithm>
#include <utility>

using namespace std;

enum pion
{
	X, O, empty, T
};


// 0 if X wins
// 1 if O wins
// 2 if Draw
// 3 if not complete
int Resolve_grid(const std::vector<pion>& grid)
{
	bool has_won = true;
	int decale = 0;
	
	// Let's check lines
	for(int line = 0; line < 4; ++line)
	{
		has_won = true;
		pion temp = grid[line * 4];
		if(temp == T)
		{
			temp = grid[line * 4 + 1];
			decale = 1;
		}
		if(temp == empty) continue;
		for(int i = line * 4 + 1 + decale; i < line * 4 + 4; ++i)
		{
			if(grid[i] != temp && grid[i] != T)
			{
				has_won = false;
				break;
			}
		}

		if(has_won) 
		{
			if (temp == X) return 0;
			else return 1;
		}
	}

	// Now columns
	for(int column = 0; column < 4; ++column)
	{
		decale = 0;
		has_won = true;
		pion temp = grid[column];
		if(temp == T)
		{
			temp = grid[column + 4];
			decale = 1;
		}
		if(temp == empty) continue;
		for(int i = 1 + decale; i <  4 ; ++i)
		{
			if(grid[column+ 4*i] != temp && grid[column+ 4*i] != T)
			{
				has_won = false;
				break;
			}
		}
		if(has_won) 
		{
			if (temp == X) return 0;
			else return 1;
		}
	}

	//Diagonales !
	decale = 0;
	has_won = true;
	pion temp = grid[0];
	if(temp == T)
	{
		temp = grid[5];
		decale = 1;
	}
	if(temp != empty)
	{
		for(int i = 1 + decale; i <  4 ; ++i)
		{
			if(grid[4*i + i] != temp && grid[4 * i + i] != T)
			{
				has_won = false;
				break;
			}
		}
		if(has_won) 
		{
			if (temp == X) return 0;
			else return 1;
		}
	}

	// other one
	decale = 0;
	has_won = true;
	temp = grid[3];
	if(temp == T)
	{
		temp = grid[6];
		decale = 1;
	}
	if(temp != empty)
	{
		for(int i = 1 + decale; i <  4 ; ++i)
		{
			if(grid[3+ 4*i - i] != temp && grid[3+ 4*i - i] != T)
			{
				has_won = false;
				break;
			}
		}
		if(has_won) 
		{
			if (temp == X) return 0;
			else return 1;
		}
	}

	// If here no winners, finished ?

	if(std::find(grid.begin(),grid.end(),empty) == grid.end())
		return 2;

	return 3;
}

int main()
{
	std::ifstream file("A-small-attempt0 (3).in", std::ifstream::in);
	std::ofstream file2("out.txt", std::ofstream::out);

	int nb;
	file >> nb;

	for(int i = 0; i < nb; ++i)
	{
		std::vector<pion> grille(16);

		for(int j = 0; j < 16; j++)
		{
			char c;

			file >> c;

			if(c == 'X') grille[j] = X;
			else if (c == 'O') grille[j] = O;
			else if (c == 'T') grille[j] = T;
			else if (c == '.') grille[j] = empty;
			else
			{
				std::cout << "Erreur input" << std::endl;
				system("pause");
			}
		}

		int res = Resolve_grid(grille);
		
		if(res == 0)
		{
			file2 << "Case #" << i + 1 << ": " << "X won" << std::endl;
		}
		else if(res == 1)
		{
			file2 << "Case #" << i + 1 << ": " << "O won" << std::endl;
		}
		else if(res == 2)
		{
			file2 << "Case #" << i + 1 << ": " << "Draw" << std::endl;
		}
		else
		{
			file2 << "Case #" << i + 1 << ": " << "Game has not completed" << std::endl;
		}
	}


}