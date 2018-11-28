// testcpp.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include "windows.h"


#include "stdio.h"
#include "stdlib.h"
#include "signal.h"
#include "process.h"
#include "malloc.h"

#include "fstream"
#include "list"
#include "vector"
#include "algorithm"
#include "time.h"

#include "queue"
#include "stack"

using namespace std;


typedef  __int64 Int64;

typedef struct Node
{
Node * child, *sibling;
char name[105];

Node(char* n)
{
	strcpy(name, n);
	child = sibling = 0;
}

} Node;


int X[55];
int V[55];
int main()
{

	int T;
	cin >> T;

	int N,K,B,Time;
	for(int t = 1; t <= T; ++t)
	{
		cin >> N >> K >> B>>Time;
		for (int i =0; i < N; ++i)
			cin >> X[i];
		for (int i = 0; i < N; ++i) cin >> V[i];

		Int64 res = 0;
		int r = N-1;
		while(r>=0 && N-1 -r < K)
		{
			double D = B;
			D-= X[r];
			D /= V[r];

			if (D > Time)
			{
				int j = r-1;
				while (j >=0)
				{
					D = B;
					D -= X[j];
					D /= V[j];
					if (D <= Time)
					{
						swap(V[j],V[r]);
							res += r -j;
						break;
					}
					--j;
				}
				if ( j < 0 )
					break;

			}
			--r;
		}

		cout << "Case #" <<t <<": ";

		if (N-1-r >= K)
			cout << res ;
		else 
			cout << "IMPOSSIBLE";
		if (t < T)
			cout << endl;
	}


	return 0;
} 