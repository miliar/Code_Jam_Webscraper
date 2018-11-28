#include <iostream>
#include <vector>
using namespace std;

void main()
{
	FILE* Input = fopen("in.in","r");
	FILE* Output = fopen("out.txt","w+");

	int T = 0;

	int _N = 0;
	int _S = 0;
	int _P = 0;
	int _ti = 0;

	vector<int> N;
	vector<int> S;
	vector<int> P;
	vector<int> ti;
	vector<vector<int>> t;

	char buf[500];

	fscanf(Input, "%d\n", &T);

	for(int i=0; i<T; i++)
	{
		ti.clear();

		fscanf(Input, "%d %d %d", &_N, &_S, &_P);

		for(int j=0; j<_N; j++)
		{
			fscanf(Input, "%d", &_ti);
			ti.push_back(_ti);
		}

		N.push_back(_N);
		S.push_back(_S);
		P.push_back(_P);
		t.push_back(ti);
	}

	for(int i=0; i<T; i++)
	{
		int Ans = 0;
		int amb = 0;

		if(P[i]==0)
		{
			Ans = N[i];
		}

		else if(P[i] == 1)
		{
			for(int j=0; j<N[i]; j++)
			{
				if(t[i][j] > 0)
					Ans++;
			}
		}
		
		else if(P[i]>1)
		{
			for(int j=0; j<N[i]; j++)
			{
				if(t[i][j] >= 3*P[i]-2)
				{
					Ans++;
				}
				else if(t[i][j] == 3*P[i]-3 || t[i][j] == 3*P[i]-4)
				{
					amb++;
				}
			}

			if(amb > S[i])
				Ans+=S[i];
			else
				Ans+=amb;
		}

		fprintf(Output, "Case #%d: %d\n",i+1, Ans);
	}

}