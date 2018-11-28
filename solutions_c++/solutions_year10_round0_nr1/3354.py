/*
 * Olaf "Ritave" Tomalka
 * 2010 Google Code Jam
 */

#include <iostream>

int main()
{
	int n,k,p;
	std::cin >> n;
	for (int i=0;i<n;i++)
	{
		std::cin >> k >> p;

		int help=2;
		for (int j=1;j<k;j++)
		{
			help*=2;
		}
		help--;
		std::cout << "Case #" << i+1 << ": ";

		if (p==0)
		{
			std::cout << "OFF\n";
			continue;
		}
		if (k==1)
		{
			if (p%2==1)
			{
				std::cout << "ON\n";
			} else
				std::cout << "OFF\n";
			continue;
		}


		bool been=false;
		while (true)
		{
			if (p<0)
			{
				std::cout << "OFF\n";
				break;
			} else if (p==0)
			{
				std::cout << "ON\n";
				break;
			} else
			{
				p-=help;
				if (!been)
				{
					help++;
					been=true;
				}
			}
		}
	}

}
