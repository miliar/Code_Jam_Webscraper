#include <iostream>
#include <string>
#include <math.h>
#include <string.h>


int main()
{
	int n=0;
	std::cin >> n;
	char str[101];
	for (int c=0;c<n;c++)
	{
		int S,Q;
		std::cin >> S;
		std::string search[S];
		std::cin.getline(str,101);
		for (int i=0;i<S;i++)
		{
			std::cin.getline(str,101);
			search[i] = str;
			//std::cout << "S:" << str << "\n";
		}

		std::cin >> Q;
		std::string query[Q];
		std::cin.getline(str,101);
		for (int i=0;i<Q;i++)
		{
			std::cin.getline(str,101);
			query[i] = str;
			//std::cout << "Q:" << str << "\n";
		}
		
		int num=0;
		int newj=0;
		while (1)
		{
			int best=0;
			int tempj=0;
			int j;
			for (int i=0;i<S;i++)
			{
				for (j=newj;j<Q;j++)
				{
					//std::cout << j << " : " << search[i] << " " << query[j] << " " << search[i].compare(query[j]) << "\n";
					if (search[i].compare(query[j])==0)
					{
						break;
					}
				}
				if (j>=tempj)
				{
					best = i;
					tempj = j;
				}
				if (j==Q)
					break;
			}
			if (j==Q)
				break;
			newj = tempj;
			num++;
		}
		std::cout << "Case #" << c+1 << ": " << num << "\n";
	}
	return 0;
}

