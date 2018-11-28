#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <utility>
#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

int TT, NN;
int N, M;
vector<char> Malted;
vector<int> Wanted;
vector<int> Degrees;
vector<vector<int> > Links;

int main()
{
	cin >> TT;
	for (NN = 1; NN <= TT; NN++)
	{
		cin >> N >> M;
		Wanted.assign(M, -1);
		Degrees.assign(M, 0);
		Links.assign(N, vector<int>());
		for (int I = 0; I < M; I++)
		{
			int T;
			cin >> T;
			while (T-- > 0)
			{
				int X, Y;
				cin >> X >> Y;
				X--;
				if (Y == 0)
				{
					Degrees[I]++;
					Links[X].push_back(I);
				}
				else
					Wanted[I] = X;
			}
		}
		Malted.assign(N, 0);
		bool Failed = false;
		vector<int> Queue;
		for (int I = 0; I < M; I++) if (Degrees[I] == 0) Queue.push_back(I);
		for (int I = 0; I < (int)Queue.size(); I++)
		{
			int J = Wanted[Queue[I]];
			if (J == -1)
			{
				Failed = true;
				break;
			}
			if (Malted[J]) continue;
			Malted[J] = true;
			for (int K = 0; K < (int)Links[J].size(); K++)
			{
				int L = Links[J][K];
				Degrees[L]--;
				if (Degrees[L] == 0) Queue.push_back(L);
			}
		}
		cout << "Case #" << NN << ":";
		if (Failed) cout << " IMPOSSIBLE";
		else
			for (int I = 0; I < N; I++)
				cout << " " << (int)Malted[I];
		cout << endl;
	}
	return 0;
}
