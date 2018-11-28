#include <cstdio>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector< string > m, mm;
int N;

int ok(int y, int x )
{
	for(int i = y+1; i < N; i++)
		if( mm[x][i] )
			return 0;
	return 1;
}

void PrintMM()
{
	for(int i = 0; i < N; i++, printf("\n"))
		for(int j = 0; j < N; j++)
			printf("%c", mm[i][j] + '0');
}

int goV()
{
	//PrintMM();

	int res = 0;
	for(int i = 0; i < N; i++)
	{
		int j = i;
		while( j < N && !ok(i, j) )
			j++;

		if( i == j )
			continue;
		if( j == N )
			return 1000000;
		
		res += j-i;
		for(int k = j-1; k >= i; k--)
		{
		//	printf("trocando %d %d\n", k, k+1);
			swap( mm[k], mm[k+1] );
			//PrintMM();
		}
	}
	return res;
}

int go()
{
	mm = m;
	int res = goV();

	return res;
}

int main()
{
	int T;
	scanf("%d", &T);
	for(int t = 0; t < T; t++)
	{
		scanf("%d", &N);
		m.resize(N);
		for(int i = 0; i < N; i++)
			cin >> m[i];

		for(int i = 0; i < N; i++)
			for(int j = 0; j < N; j++)
				m[i][j] -= '0';

		printf("Case #%d: %d\n", t+1, go());
	}
}