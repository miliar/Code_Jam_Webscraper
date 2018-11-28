#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int N, M, A;
int main()
{
	ifstream fin("problemB.in");
	ofstream fout("problemB.out");
	
	int test_case;
	int num_test_cases;
	long long value;
	bool find_solution;
	int x1, y1, x2, y2, x3, y3;
	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{	
		fin >> N >> M >> A;
		find_solution = false;
		for(long long a = 0; a <= N; a++)
		{
			for(long long b = 0; b <= M; b++)
			{
				for(long long x = 0; x <= N - a; x++)
				{
					for(long long y = 0; y <= M; y++)
					{
						value = a * y + b * x;
						if(value == A)
						{
							x1 = a;
							y1 = 0;
							x2 = 0;
							y2 = b;
							x3 = a + x;
							y3 = y;
							find_solution = true;
							break;
						}
					}
					if(find_solution) break;
				}
				if(find_solution) break;
			}
			if(find_solution) break;
		}
		if(find_solution)
		{
			fout << "Case #" << test_case << ": " << x1 << " " << y1 << " " << x2 << " " << y2 << " " << x3 << " " << y3 << endl;
		}
		else
		{
			fout << "Case #" << test_case << ": IMPOSSIBLE" << endl;
		}
	}
	
	fin.close();
	fout.close();
	return 0;
}