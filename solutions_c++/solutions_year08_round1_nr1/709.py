#include <fstream>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int T; // # of test case
	int n; // dimension of vectors
	int i, j;
	int test_case;
	int x_vector[800];
	int y_vector[800];
	long solution;
	
	fin >> T;
	for(test_case = 1; test_case <= T; test_case++)
	{
		fin >> n;
		for(i = 0; i < n; i++)
		{
			fin >> x_vector[i];
		}
		
		for(i = 0; i < n; i++)
		{
			fin >> y_vector[i];
		}
		
		sort(x_vector, x_vector + n);
		sort(y_vector, y_vector + n);
		solution = 0;
		for(i = 0; i < n; i++)
		{
			solution += x_vector[i] * y_vector[n - i - 1];
		}
		
		fout << "Case #" << test_case << ": " << solution << endl;
	}
	fout.close();
	fin.close();
	return 0;
}