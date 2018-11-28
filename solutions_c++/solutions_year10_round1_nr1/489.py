#include <stdio.h>
#include <iostream>
#include <vector>

using namespace std;
void print(vector<vector<char> >& A, int N);
void rotate(vector<vector<char> >& A, int N)
{
	vector<vector<char> > T(N, vector<char>(N));
	

	
	// rotate
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			T[j][i] = A[N-i-1][j];
		}
	}
	
	
	////print(T, N);
	////printf("qq\n");
	// gravity
	bool bNext = true;
	while(bNext)
	{
		bNext = false;
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				if (j-1 < 0)
					continue;
				if (T[j][i] == '.' && T[j-1][i] != '.')
				{
					T[j][i] = T[j-1][i];
					T[j-1][i] = '.';
					bNext = true;
				}
			}
		}
	}
	
	
	A = T;
	
}

int check(vector<vector<char> >& A, int N, int K)
{
	int r = 0;
	for(int i=0;i<N;i++)
	{
		for(int j=0;j<N;j++)
		{
			char T = A[i][j];
			
			if (T=='.') 
				continue;
			
			// ->
			if (i+K-1 < N)
			{
				bool bWin = true;
				for(int k=0;k<K;k++)
				{
					if (A[i+k][j] != T)
					{
						bWin = false;
						break;
					}
				}
				if (bWin)
				{
					//printf("win1, %d, %d\n", i,j);
					if (T=='R')
						r |= 0x01;
					if (T=='B')
						r |= 0x02;
				}
			}

			// \
			// ->
			if ( (i+K-1 < N) && (j+K-1 < N) )
			{
				bool bWin = true;
				for(int k=0;k<K;k++)
				{
					if (A[i+k][j+k] != T)
					{
						bWin = false;
						break;
					}
				}
				if (bWin)
				{
				//printf("win2, %d, %d\n", i,j);
					if (T=='R')
						r |= 0x01;
					if (T=='B')
						r |= 0x02;
				}
			}	
					
			// |
			if ( (j+K-1 < N) )
			{
				bool bWin = true;
				for(int k=0;k<K;k++)
				{
					if (A[i][j+k] != T)
					{
						bWin = false;
						break;
					}
				}
				if (bWin)
				{
				//printf("win3, %d, %d\n", i,j);
					if (T=='R')
						r |= 0x01;
					if (T=='B')
						r |= 0x02;
				}
			}	
			
			// /
			if ( (i+K-1 < N) && (j-K+1 >= 0) )
			{
				bool bWin = true;
				for(int k=0;k<K;k++)
				{
					if (A[i+k][j-k] != T)
					{
						bWin = false;
						break;
					}
				}
				if (bWin)
				{
				//printf("win4, %d, %d\n", i,j);
					if (T=='R')
						r |= 0x01;
					if (T=='B')
						r |= 0x02;
				}
			}		
	
		}
	}
	return r;
};

void print(vector<vector<char> >& A, int N)
{
	for(int j=0;j<N;j++)
	{
		for(int k=0;k<N;k++)
			cout << A[j][k];

		cout << "\n";
	}
};

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int i=0;i<T;i++)
	{
		int N, K;
		scanf("%d %d", &N, &K);
		vector<vector<char> > vecA(N, vector<char> (N));
		
		//cout << "next:\n";
		for(int j=0;j<N;j++)
		{
			for(int k=0;k<N;k++)
				cin >> vecA[j][k];
		}
		
		//printf("k = %d\n", K);
		//print(vecA, N);
		
		//printf("after r\n");
		rotate(vecA, N);
		
		//print(vecA, N);
		
		int r = check(vecA, N, K);
		//printf("r = %d\n", r);
		switch(r)
		{
		case 0:
			printf("Case #%d: Neither\n", i+1);
			break;
		case 1:
			printf("Case #%d: Red\n", i+1);
			break;
		case 2:
			printf("Case #%d: Blue\n", i+1);
			break;
		case 3:
			printf("Case #%d: Both\n", i+1);
			break;
		break;
		}
	
		
	}
};
