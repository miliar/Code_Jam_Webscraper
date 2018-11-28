#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	int T;
	
	int *N;
	int *S;
	int *p;
	int **t;
	int *result;

	ifstream fin("B-large.IN");
	fin >> T;

	N = new int [T];
	S = new int [T];
	p = new int [T];
	t = new int* [T];
	result = new int [T];

	for (int i=0; i<T; i++)
	{
		fin >> N[i];
		t[i] = new int[N[i]];
		fin >> S[i];
		fin >> p[i];

		for (int j=0; j<N[i]; j++)
		{
			fin >> t[i][j];
		}
	}



	// Sorting
	for (int i=0; i<T; i++)
	{
		int in, out;

		for (out=1; out<N[i]; out++)
		{
			int temp = t[i][out];
			in = out;

			while (in>0 && t[i][in-1] <= temp)
			{
				t[i][in] = t[i][in-1];
				--in;
			}

			t[i][in] = temp;
		}
	}


	for (int i=0; i<T; i++)
	{
		result[i] = 0;
	}


	for (int i=0; i<T; i++)
	{
		for (int j=0; j<N[i]; j++)
		{
			if (t[i][j] == 0)
			{
				if (p[i]==0)
				{
					result[i]++;
				}
				continue;
			}

			if (t[i][j]%3 == 0)
			{
				if (t[i][j]/3 >= p[i])
				{
					result[i]++;
					continue;
				}
			}

			else if (t[i][j]%3 == 1)
			{
				if (((t[i][j]-1)/3) +1 >= p[i])
				{
					result[i]++;
					continue;
				}
			}

			else if (t[i][j]%3 == 2)
			{
				if (((t[i][j]-2)/3) +1 >= p[i])
				{
					result[i]++;
					continue;
				}
			}

			if (S[i]>0)
			{
				if (t[i][j]%3 == 0)
			{
				if ((t[i][j]/3)+1 >= p[i])
				{
					result[i]++;
					S[i]--;
				}
			}

			else if (t[i][j]%3 == 1)
			{
				if (((t[i][j]-1)/3) +1 >= p[i])
				{
					if (t[i][j]!=1)
					{
					result[i]++;
					S[i]--;
					}
				}
			}

			else if (t[i][j]%3 == 2)
			{
				if (((t[i][j]-2)/3) +2 >= p[i])
				{
					result[i]++;
					S[i]--;
				}
			}
			}
		}
	}


	ofstream fout ("B.txt");

	for (int j=0; j<T; j++)
	{
		fout << "Case #";
		fout << j+1;
		fout << ": " ;
		fout << result[j];
		fout << endl;
	}

	delete [] result;
	delete [] N;
	delete [] S;
	delete [] p;
	delete [] t;

	for (int i=0; i<T; i++)
	{
		delete [] t[i];
	}
	return 0;
}