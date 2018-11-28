#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
using namespace std;

vector <string>	engines;
vector <string> queries;
int	min_switch[2000][2000];
int	cmp[2000];

int main()
{
	int	T,cs;
	int	N,M;
	int	i,j,k;
	char	name[1000];

	scanf("%d",&T);

	for(cs = 1; cs <= T; cs++)
	{
		scanf("%d",&N);
		gets(name);

		engines.clear();
		queries.clear();

		while(N--)
		{
			gets(name);
			engines.push_back(name);
		}

		scanf("%d",&M);
		gets(name);

		while(M--)
		{
			gets(name);
			queries.push_back(name);
		}

//		printf("%d %d\n",queries.size(),engines.size());

		for(j = 0; j < queries.size(); j++)
		{
//			printf("Q: %d %s\n",j,queries[j].c_str());

			for(i = 0; i < engines.size(); i++)
			{
				if(queries[j] == engines[i])
					break;
			}

			cmp[j] = i;			
		}


		for(j = 0; j < engines.size(); j++)
			min_switch[queries.size()][j] = 0;

		for(i = queries.size() - 1; i >= 0; i--)
		{
			for(j = 0; j < engines.size(); j++)
			{
				min_switch[i][j] = queries.size();

				for(k = 0; k < engines.size(); k++)
				{
					int	x;

					if(cmp[i] == j) continue;

					if(j == k)
						x = min_switch[i+1][k];
					else
						x = 1 + min_switch[i+1][k];

					min_switch[i][j] = min(min_switch[i][j],x);
				}
			}
		}

		int	m = queries.size() + 1;

		for(i = 0; i < engines.size(); i++)
		{
			m = min(min_switch[0][i],m);
		}

		printf("Case #%d: %d\n",cs,m);
	}

	return 0;
}
