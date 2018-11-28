// A.cpp : Defines the entry point for the console application.
//

#include <fstream>
#include <map>
#include <vector>
#include <string>

using namespace std;

ifstream in("A.in");
ofstream out("A.out");

int L, D, N;

vector <string> dict;

vector <vector <char> > P;
map <char, int> M;

int main()
{
	in >> L >> D >> N;
	dict.resize(D);
	for (int i=0; i<D; ++i)
	{
		in >> dict[i];
	}
	for (int i=0; i<N; ++i)
	{
		P.clear();
		string S;
		in >> S;
		P.resize(L);
		int x = 0;
		M.clear();
		int n = 1;
		for (int j=0; j<L; ++j)
		{
			if (S[x] == '(')
			{
				++x;
				while(S[x] != ')')
				{
					P[j].push_back(S[x]);
					if (M[S[x]] == 0)
					{
						M[S[x]] = n;
						++n;
					}
					++x;
				}
				++x;
			}
			else
			{
				P[j].push_back(S[x]);
				if (M[S[x]] == 0)
				{
					M[S[x]] = n;
					++n;
				}
				++x;
			}
		}

		vector <vector <int> > A;
		A.resize(L);
		for (int j = 0; j<A.size(); ++j)
		{
			A[j].resize(n+1);
		}
		for (int j = 0; j < L; ++j)
		{
			for (int k=0; k < P[j].size(); ++k)
			{
				A[j][M[P[j][k]]] = j+1;
			}
		}

		int col = 0;
		for (int j = 0; j < D; ++j)
		{
			int state = 0;
			int x = 0;
			while(true)
			{
				state = A[state][M[dict[j][x]]];
				if (state == 0 || state == L)
				{
					break;
				}
				++x;
			}
			if (state == L)
				++col;
		}
		out << "Case #" << i+1 << ": " << col << "\n";

	}
	return 0;
}

