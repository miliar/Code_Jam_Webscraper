#include <cstdio>
#include <map>
#include <vector>
#include <string>

using namespace std;

const int MAX_LENGTH = 100;
char buffer[MAX_LENGTH+1];
string aux;

int main()
{
	int N;
	scanf("%d",&N);
	for (int i=0;i<N;i++)
	{
		int S;
		scanf("%d",&S);
		getchar(); //EOL

		map<string,int> engines;
		
		for (int j=0;j<S;j++)
		{
			gets(buffer);
			aux = string(buffer);
			engines[aux] = j;
		}

		int Q;
		scanf("%d",&Q);
		getchar(); //EOL
		
		vector<int> switches(S,0);		
		int min = 0;

		for (int j=0;j<Q;j++)
		{
			gets(buffer);
			int k = engines[string(buffer)];
			int minaux = Q+1;

			for(int l=0;l<S;l++)
			{
				if (l==k) switches[l] = -1;
				else
				{
					if (switches[l] == -1) switches[l] = min + 1;
					if (switches[l] < minaux) minaux = switches[l];
				}
			}

			min = minaux;
		}

		printf("Case #%d: %d\n",i+1,min);
	}
	return 0;
}