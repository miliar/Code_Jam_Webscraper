#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	int T, C, D, N;
	string Cs, Ds, Ns;
	vector<char> C1, C2, C3, D1, D2, N1, N2;
	ifstream inFile( "B-small-attempt2.in" );
	ofstream outFile( "B-small.txt" );

	inFile >> T;

	for(int i = 0; i < T; i++)
	{
		C1.clear();
		C2.clear();
		C3.clear();
		D1.clear();
		D2.clear();
		N1.clear();
		N2.clear();

		inFile >> C;
		if(C)
		{
			for(int j = 0; j < C; j++)
			{
				inFile >> Cs;
				C1.push_back(Cs[0]);
				C2.push_back(Cs[1]);
				C3.push_back(Cs[2]);
			}
		}

		inFile >> D;
		if(D)
		{
			for(int j = 0; j < D; j++)
			{
				inFile >> Ds;
				D1.push_back(Ds[0]);
				D2.push_back(Ds[1]);
			}
		}

		inFile >> N >> Ns;
		for(int j = 0; j < N; j++)
		{
			N1.push_back(Ns[j]);
		}

		for(int j = 0; j < N; j++)
		{
			N2.push_back(N1[j]);
			int last = N2.size()-1;
			if(N2.size()>1)
			{
				for(int k = 0; k < C1.size();k++)//buscar si forma una no-base
				{
					if(N2[last]==C1[k])
					{
						if(N2[last-1]==C2[k])//si forma, buscar su no-base y reemplazar.
						{
							N2.pop_back();
							last--;
							N2[last] = C3[k];
						}
						break;//dejar de buscar
					}
					if(N2[last]==C2[k])
					{
						if(N2[last-1]==C1[k])//si forma, buscar su no-base y reemplazar.
						{
							N2.pop_back();
							last--;
							N2[last] = C3[k];
						}
						break;//dejar de buscar
					}
				}

				for(int k = 0; k < D1.size(); k++)//buscar si tiene opuesto
				{
					if(N2[last]==D1[k])
					{
						for(int l = N2.size()-1; l >= 0; l--)
						{
							if(N2[l]==D2[k])
							{
								N2.clear();
								break;
							}
						}
						break;//dejar de buscar
					}
					if(N2[last]==D2[k])
					{
						for(int l = N2.size()-1; l >= 0; l--)
						{
							if(N2[l]==D1[k])
							{
								N2.clear();
								break;
							}
						}
						break;//dejar de buscar
					}
				}
			}
		}
		outFile << "Case #" << i+1 << ": [";
		for(int j = 0; j < N2.size(); j++)
		{
			outFile << N2[j];
			if(j<N2.size()-1)
				outFile << ", ";
		}
		outFile << "]" << endl;
	}

	return 0;
}