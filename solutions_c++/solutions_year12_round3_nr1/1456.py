#include <iostream>
#include <vector>
#include <map>
#include <list>

using namespace std;

bool M[1000][1000];
int  K[1000][1000];

int N;

int getNumberOfPathes(int i, int j)
{
	int result = 0;

	// printf("%d %d\n", i, j);

	if( K[i][j] != -1 ) return M[i][j];

	if( i == j ) return 1; //?

	for(int k = 0; k < N; k++)
	{
		if( M[i][k] ) result += getNumberOfPathes(k, j);
	}

	return result;
}

void processCase()
{
	memset(M, 0, sizeof(M));

	cin >> N;

	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < N; j++)
		{
			K [i][j] = -1; // not calculated
		}
	}

	for(int i = 0; i < N; i++)
	{
		int Mc;

		cin >> Mc;
		for(int j = 0; j < Mc; j++)
		{
			int Mj;

			cin >> Mj;
			Mj--;
			M[i][Mj] = true;
		}
	}


	for(int i = 0; i < N; i++)
	{
		for(int j = 0; j < N; j++)
		{
			if(getNumberOfPathes(i, j) > 1) 
			{
				printf("Yes");
				return;
			}	
		}
	}
	
	printf("No");
}

int main(int argc, const char * argv[])
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
			processCase();
		printf("\n");
	}
	
    return 0;
}
