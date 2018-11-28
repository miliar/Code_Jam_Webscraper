#include <iostream>

#define	at(i, j)	((i) * 50 + (j))

char	wk[51*51];

void	aff(int r, int c)
{
	for(int i = 0; i < r; i++)
	{
		for(int j = 0; j < c; j++)
			std::cout << wk[at(i, j)];
		std::cout << "\n";
	}
}

void	calc_case(int id)
{
	int r, c;
	std::cin >> r >> c;

	for(int i = 0; i < r; i++)
	{
		int j;
		for(j = 0; j < c; j++)
			std::cin >> wk[at(i, j)];
		wk[at(i, j)] = 0;
		wk[at(i, j)] = 0;
		wk[at(i+1, j-1)] = 0;
	}

//	std::cout << "Convert : \n";
//	aff(r, c);


	for(int i = 0; i < r; i++)
		for(int j = 0; j < c; j++)
		{
			if (wk[at(i, j)] == '#')
			{
				if(wk[at(i+1, j)] != '#' || wk[at(i, j + 1)] != '#'
				   || wk[at(i + 1, j + 1)] != '#')
				{
					std::cout << "Case #" << id << ":\n";
					std::cout << "Impossible\n";
//					aff(r, c);
					return;
				}
				wk[at(i, j)] = '/';
				wk[at(i, j + 1)] = '\\';
				wk[at(i + 1, j)] = '\\';
				wk[at(i + 1, j + 1)] = '/';
				j += 1;
			}
			else
			{
				if (wk[at(i, j)] == '/' || wk[at(i, j)] == '\\')
					j += 1;
			}
		}
//	std::cout << "To : \n";
//	aff(r, c);

	std::cout << "Case #" << id << ":\n";

	aff(r, c);
}

int	main(void)
{
	int	t;

	std::cin >> t;
	for(int i = 0; i < t; i++)
		calc_case(i + 1);
	
	return 0;
}
