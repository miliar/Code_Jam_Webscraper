// ProblemA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
using namespace std;

int min(int A, int B)
{
	if (A>B) return B; else return A;
}

int max(int A, int B)
{
	if (A<B) return B; else return A;
}


int main(int argc, char* argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w", stdout);
	int N,C,O,B,M,T,min2,last,Odist,Bdist;
	char Ch;
	cin >> N;
	for(int cur=1;cur<=N;cur++)
	{
		last = 0;
		M = 0;
		O = 1;
		B = 1;
		Odist = 0;
		Bdist = 0;
		cin >> C;
		for (int i = 0; i < C; ++i)
		{
			cin >> Ch;
			cin >> T;
			if (Ch == 'O')
			{
				if (last == 0) 
				{
					Odist += abs(O - T) + 1;
					O = T;
				} else
				{
					if (Bdist > abs(O - T))
					{
						M += Bdist;
						O = T;
						Odist = 1;
					} else
					{
						M += Bdist;
						Odist = abs(O - T) - Bdist + 1;
						O = T;
					}
				}
				last = 0;
			} else
			{
				if (last == 1)
				{
					Bdist += abs(B - T) + 1;
					B = T;
				} else
				{
					if (Odist > abs(B - T))
					{
						M += Odist;
						B = T;
						Bdist = 1;
					} else
					{
						M += Odist;
						Bdist = abs(B - T) - Odist + 1;
						B = T;
					}
				}
				last = 1;
			}
		}
		if (last == 0) M+=Odist; else M+=Bdist;
		cout << "Case #" << cur << ": " << M << endl;
	}
	return 0;

}

