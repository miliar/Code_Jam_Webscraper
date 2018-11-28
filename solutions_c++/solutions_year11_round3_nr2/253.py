#include <iostream>
#include <stdio.h>
#include <fstream>
#include <algorithm>
#include <math.h>
using namespace std;

int P[1000001];

int main()
{
	int T, L,N,C;
	int A[1001];

	int i,j,k, jind;

	__int64 time,t;
	long long rasst, time0;
	bool build;

	cin >> T;
	for (i=1;i<=T;i++)
	{
		cin >> L >> t >> N >> C;
		for (j=0;j<C;j++) cin >> A[j];

		rasst = 0;
		time = 0;
		build = false;
		k=0;
		jind = -1;
		for (j=0;j<N;j++)
		{
			if ((time + A[k]*2 >= t)&&(!build)) 
				{
					build = true;
					P[j] = A[k] - (t/2-rasst);
					jind = j;
					time = time + (t-time);
				}
			else
			{
				if (build)
				{
					P[j] = A[k];
				}
				else
				{
					rasst = rasst + A[k];
					time = time + A[k]*2;
				}
			}
	

			k++;
			if (k>=C) k = 0;
		}

		if (jind >= 0)
		{
		sort(P+jind,P+N);

		for (j=N-1;j>=jind;j--)
		{
			if (L>0)
			{
				L--;
				time = time + P[j];
			}
			else
			{
				time = time + 2*P[j];
			}
		}
		}
		cout << "Case #" << i << ": " << time << endl;
	}
}