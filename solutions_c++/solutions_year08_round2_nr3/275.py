#include <iostream>
using namespace std;

int main(void)
{
	unsigned int num_casos, *deck;

	cin >> num_casos;
	for(unsigned int c = 1; c <= num_casos; c++)
	{
		unsigned int tam, n;

		cin >> tam >> n;
		deck = new unsigned int[tam + 1];
		memset(deck, 0, sizeof(unsigned int) * (tam + 1));

		for(unsigned int i = 1, j = 0; i <= tam; i++)
		{
			for(unsigned int k = 0; k < i; k++)
			{
				j = (j + 1) % tam;
				if(j == 0) j = tam;
				if(deck[j]) k--;
			}
			deck[j] = i;
		}

		cout << "Case #" << c << ":";
		for(unsigned int i = 1; i <= n; i++)
		{
			unsigned int search;
			cin >> search;
			cout << " " << deck[search];
		}
		cout << endl;
	}
}
		
