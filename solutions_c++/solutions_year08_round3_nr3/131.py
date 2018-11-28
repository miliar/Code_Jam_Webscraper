#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream fin("problemC.in");
	ofstream fout("problemC.out");
	
	int test_case;
	int num_test_cases;
	
	int i, j;
	int n, m;
	long long X, Y, Z;
	long long sequence[1000];
	long long A[100];
	long long table[1000];
	long long solution;
	long long t_mod = 1000000007;
	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{
		fin >> n >> m >> X >> Y >> Z;
		for(i = 0; i < m; i++)
		{
			fin >> A[i];
		}
		
		for(i = 0; i < n; i++)
		{
			sequence[i] = A[i % m];
			A[i % m] = (X * A[i % m] + Y * (i + 1)) % Z;
		}
		
		for(i = 0; i < n; i++)
		{
			table[i] = 1;
			for(j = 0; j < i ;j++)
			{
				if(sequence[j] < sequence[i])
				{
					table[i] = (table[i] + table[j]) % t_mod;
				}
			}
		}
		
		solution = 0;
		for(i = 0; i < n; i++)
		{
			solution = (solution + table[i]) % t_mod;
		}
		
		fout << "Case #" << test_case << ": " << solution<< endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}