#include <iostream>

void create_deck(int K, int c)
{
	int deck[K];
	for (int i = 0; i < K; i++)
	{
		deck[i] = 0;		
	}

	int i = 0;
	int index = 0;
	int pos = 1;
	int actual = 1;
	
	while(i != K)
	{
		if(deck[index] == 0)
		{
			if(pos == actual)
			{
				deck[index] = actual;
				if(actual == K)
				{
					i = K;
				}
				actual += 1;
				pos = 1;
			}
			else
			{
				pos += 1;
			}
		}
		index += 1;
		if(index == K)
		{
			index = 0;
		}
	}

	std::cout << "Case #" << c << ": ";
	int n;
	std::cin >> n;
	for(int i = 0; i<n ; i++)
	{
		std::cin>>index;
		std::cout<<deck[index-1] << " ";
	}
	std::cout << "\n";

	/*for(int i = 0; i< K; i++)
	{
		std::cout << deck[i];
	}*/
}

int main()
{	
	int i = 0;
	int T,K;

	std::cin >> T;
	for(i=0;i<T;i++)
	{
		std::cin >> K;
		create_deck(K, i+1);
	}

	return 0;
}
