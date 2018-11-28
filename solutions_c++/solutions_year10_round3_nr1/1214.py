#include <iostream>
#include <fstream>
#include <string.h>
#include <math.h>
using namespace std;

void parsing(istream& input, int& count, int* &n, int** &A, int** &B);
int main()
{
	int count;
	int *n;
	int **A;
	int **B;
	ifstream input("a.txt");
	ofstream output("out.txt");
	parsing(input, count,n,A,B);

	for(int i = 0; i < count; i++)
	{
		int result = 0;
		for(int j = 0 ; j < n[i]; j++)
		{
			for(int k = 0 ; k < n[i]; k++)
			{
				if ( (A[i][k] > A[i][j]) && (B[i][k] < B[i][j]) )
				{
					result++;
				}

			}
		}
		cout <<	"Case #" << i+1 << ": " << result << endl;
		output <<	"Case #" << i+1 << ": " << result << endl;
	}
	
	
/*	cout <<	"Case #" << i+1 << ": " << result << endl;
	output <<	"Case #" << i+1 << ": " << result << endl;
	result = 0;
	}*/
	return 0;

}
void parsing(istream& input, int& count, int* &n, int** &A, int** &B)
{
	input >> count;
	n = new int[count];
	A = new int*[count];
	B = new int*[count];
	for (int i = 0; i < count; i++)
	{
		input >> n[i];
		A[i] = new int[n[i]];
		B[i] = new int[n[i]];
		for (int j = 0 ; j < n[i]; j++)
		{
			input >> A[i][j];
			input >> B[i][j];
		}
		
	}
}




