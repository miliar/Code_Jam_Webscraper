#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	//========read in input==========//
	char* testinput = "e:\\test.txt";
	char* input = "e:\\B-large.in";
	ifstream fin;
	fin.open(input,ios_base::binary);   //now test
	//========create output=========//
	ofstream fout;
	fout.open("output_L.txt");
	
	//==========begin here==========//
	int C;
	fin >> C;
	int N, K , B, T;
	for(int c = 1; c <= C; c++)
	{
		fout<< "Case #" << c <<": ";

		fin >> N;
		fin >> K;
		fin >> B;
		fin >> T;
		
		int *X = new int[N];
		for(int i = 0; i < N ; i++)
		{
			fin>> X[i];
		}
		int *V = new int[N];
		for(int i = 0; i < N ; i++)
		{
			fin>> V[i];
		}

		int *reach = new int[N];
		int rock = 0;
		int totalcount = 0;
		for(int i = N-1; i >= 0 ; i--)
		{
			if(X[i] + V[i] *T >= B)
			{
				reach[i] = rock;
				totalcount ++;
			}
			else 
			{
				reach[i] = -1;
				rock++;
			}
		}
		
		if(totalcount < K)
		{
			fout<<"IMPOSSIBLE" <<endl;
		}
		else
		{
			int swaps = 0;
			int k = K;
			int p = N-1;
			while(k!=0)
			{
				while(p >= 0)
				{
					if(reach[p] >=0)
					{
						swaps += reach[p];
						p--;
						break;
					}
					else 
						p--;
				}
				k--;
			}

			fout<< swaps<<endl;
		}

	}

	return 0;
}