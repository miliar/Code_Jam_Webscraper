#include <iostream>

char	c[256];
char	d[256];
char	c_out[800];


inline int cb_id(int a, int b)
{
	return (26*(a - 'A') + (b-'A'));
}

void	init()
{
	for(int i = 'A'; i <= 'Z'; i++)
	{
		c[i] = 0;
		c_out[i] = 0;
		d[i] = 0;
	}

	//Combine table
	int nb_comb;
	std::cin >> nb_comb;
	while(nb_comb-- > 0)
	{
		char a, b, r;
		std::cin >> a >> b >> r;
		c[a] = b;
		c[b] = a;
		c_out[cb_id(a, b)] = r;
		c_out[cb_id(b, a)] = r;
	}

	//Delete table
	int nb_del;
	std::cin >> nb_del;
	while(nb_del-- > 0)
	{
		char a, b;
		std::cin >> a >> b;
		d[a] = b;
		d[b] = a;
	}
}

void	display(char *str, int l)
{
	if(l == 0)
		return;
	int i = 0;
	for(; i < l - 1; i++)
		std::cout << str[i] << ", ";
	std::cout << str[i];
}

void out()
{
	char	string[200];

	//On each character
	int nb;
	std::cin >> nb;

	//Store the first character
	std::cin >> string[0];
	int i = 1;
	while(--nb)
	{
		std::cin >> string[i];

		//Combine!
		if(i > 0)
		{
			const char cur_l = string[i];
			const char old_l = string[i-1];

			if(c[old_l] == cur_l)
			{
				string[i-1] = c_out[cb_id(cur_l, old_l)];
				i--;
			}
		}

		/// OK, i don't read the word "whole" in the suject. So, it become a little bit easier...
		// //Delete
		// int j = i-1;
		// while(j >= 0)
		// {
		// 	if(d[string[j]] == string[i])
		// 	{
		// 		i = j-1;
		// 		j--;
		// 		break;
		// 	}
		// 	j--;
		// }

		//Delete
		int j = i;
		while(--j >= 0)
			if(d[string[j]] == string[i])
			{
				i = -1;
				break;
			}

		//Next character
		i++;
	}

	display(string, i);
}

int main(void)
{
	int nb_cases;

	//For each cases
	std::cin >> nb_cases;
	for(int i = 1; i <= nb_cases; i++)
	{
		//Initialise hash tabs
		init();

		std::cout << "Case #" << i << ": [";
		out();
		std::cout << "]\n";
	}
	return 0;
}
