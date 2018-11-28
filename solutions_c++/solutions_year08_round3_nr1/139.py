#include <fstream>
#include <iostream>
#define _max 1000
using namespace std;

int main()
{
	ifstream fin("problemA.in");
	ofstream fout("problemA.out");
	
	int test_case;
	int num_test_cases;
	
	long long i, j;
	long long temp;
	long long P, K, L;
	long long freq[_max];
	long long solution; 
	
	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{
		fin >> P >> K >> L;
		for(i = 0 ; i < L; i++)
		{
			fin >> freq[i];
		}
		
		// sort
		for(i = 0; i < L; i++)
		{
			for(j = i + 1; j < L; j++)
			{
				if(freq[i] < freq[j])
				{
					temp = freq[i];
					freq[i] = freq[j];
					freq[j] = temp;
				}
			}
		}
		
		solution = 0;
		for(i = 0; i < L; i++)
		{
			solution += (i / K + 1) * freq[i];
		}
		
		fout << "Case #" << test_case << ": " << solution << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}