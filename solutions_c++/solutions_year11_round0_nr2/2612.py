#include <Windows.h>
#include <stdio.h>
#include <string.h>
#include <set>
#include <list>;

int main()
{
	int T, C, D, N;
	char Co[128][128];
	std::set<char> *De[128];
	std::list<char> evoke;
	char buffer[256];

	scanf("%d", &T);

	for(int i = 0; i < 128; i++)
	{
		De[i] = new std::set<char>();
	}


	for(int test = 1; test <=T; test++)
	{
		char c1, c2, cr;
		char d1, d2;

		memset(Co, 0, sizeof(Co));
		for(int i = 0; i < 128; i++)
		{
			De[i]->clear();
		}

		scanf("%d ", &C);
		for(int i = 0; i < C; i++)
		{
			scanf("%c%c%c ", &c1, &c2, &cr);
			Co[c1][c2] = cr;
			Co[c2][c1] = cr;
		}

		scanf("%d ", &D);
		for(int i = 0; i < D; i++)
		{
			scanf("%c%c ", &d1, &d2);
			De[d1]->insert(d2);
			De[d2]->insert(d1);
		}

		scanf("%d %s", &N, buffer);

		for(int i = 0; i < N; i++)
		{
			// lista vazia
			if(evoke.empty())
			{
				evoke.push_back(buffer[i]);
			}
			else
			{
				// combine
				if(Co[evoke.back()][buffer[i]] != 0)
				{
					char back = evoke.back();
					evoke.pop_back();
					evoke.push_back(Co[back][buffer[i]]);
				}
				// look for destruction
				else
				{
					char bomb = buffer[i];

					if(!De[bomb]->empty())
					{
						for(std::list<char>::iterator iter = evoke.begin(); iter != evoke.end(); iter++)
						{
							if( De[bomb]->find( *iter ) != (De[bomb])->end() )
							{
								evoke.clear();
								break;
							}
						}
					}
					// did not explode
					if( !evoke.empty())
					{
						evoke.push_back(buffer[i]);
					}
				}
			}
		}

		printf("Case #%d: [", test);

		while(!evoke.empty())
		{
			printf("%c", evoke.front());
			evoke.pop_front();
			if(!evoke.empty())
				printf(", ");
		}

		printf("]\n");
	}

	for(int i = 0; i < 128; i++)
	{
		delete De[i];
	}


	return 0;
}