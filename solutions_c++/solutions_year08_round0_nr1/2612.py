#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int SolveRest(vector<int>& Q, int ECount, int I);
int Solve(vector<int>& Q, int ECount, int E, int I);

int mem[100][1000];

int SolveRest(vector<int>& Q, int ECount, int I)
{
	int BestS = 1000000;

	if(I >= (int)(Q.size())) return 0;

	for(int i = 0; i < ECount; i++)
	{
		if(i == Q[I]) continue;
		
		int S = mem[i][I+1];

		if(S == -1)
		{
			S = Solve(Q, ECount, i, I+1);

			mem[i][I+1] = S;
		}

		if(S < BestS) BestS = S;
	}

	return BestS;
}

int Solve(vector<int>& Q, int ECount, int E = 0, int I = -1)
{
	//

	if(I == -1)
	{
		for(int i = 0; i < 100; i++)
			for(int j = 0; j < 1000; j++) mem[i][j] = -1;

		return SolveRest(Q, ECount, 0);
	}

	for(int i = I; i < (int)(Q.size()); i++)
	{
		if(E == Q[i])
		{
			return SolveRest(Q, ECount, i) + 1;
		}
	}
	
	return 0;
}

int main()
{
	ifstream File("A-large.in");
	ofstream OutFile("A-large.out");

	if(!File.good())
	{
		cout << "Bad file!" << endl;

		return 0;
	}

	int N = 0;

	File >> N;
	
	for(int i = 0; i < /*1*/ N; i++)
	{
		vector<string> Engines;
		vector<string> Queries;

		int E = 0;
		int Q = 0;

		File >> E;
		
		File.get();

		for(int j = 0; j < E; j++)
		{
			char Engine[128];

			File.getline(Engine, sizeof(Engine));

			Engines.push_back(Engine);

			//cout << Engine << endl;
		}

		File >> Q;

		File.get();

		for(int j = 0; j < Q; j++)
		{
			char Query[128];

			File.getline(Query, sizeof(Query));

			Queries.push_back(Query);

			//cout << Query << endl;
		}

		vector<int> IntQ(Queries.size());

		for(int j = 0; j < (int)(Queries.size()); j++)
		{
			for(int k = 0; k < (int)(Engines.size()); k++)
			{
				if(Queries[j] == Engines[k])
				{
					IntQ[j] = k;

					break;
				}
			}
		}

		int ans = Solve(IntQ, E);

		OutFile << "Case #" << (i+1) << ": " << ans << endl;

		cout << "Case #" << (i+1) << ": " << ans << endl;
	}

	File.close();
	OutFile.close();
}