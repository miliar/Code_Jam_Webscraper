#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("ProbelmA.out");

	int T;
	fin >> T;
	int i,j,k;
	int nChangeTemp;
	int N;
	int nCrossNum = 0;
	
	for (i=0;i<T;i++)
	{
		fin >> N;
		int   *A=new   int[N];
		int   *B=new   int[N];
		for (j=0;j<N;j++)
		{
			fin >> A[j] >> B[j];
		}
		for (j=0;j<N-1;j++)
		{
			for (k=j+1;k<N;k++)
			{
				if (A[j]>A[k])
				{
					nChangeTemp = A[j];
					A[j] = A[k];
					A[k] = nChangeTemp;
					nChangeTemp = B[j];
					B[j] = B[k];
					B[k] = nChangeTemp;
				}
			}
			A[j] = j;			
		}
		A[N-1] = N-1;

		for (j=0;j<N-1;j++)
		{
			for (k=j+1;k<N;k++)
			{
				if (B[j]>B[k])
				{
					nChangeTemp = A[j];
					A[j] = A[k];
					A[k] = nChangeTemp;
					nChangeTemp = B[j];
					B[j] = B[k];
					B[k] = nChangeTemp;
				}
			}		
		}

		nCrossNum = 0;
		for (j=0;j<N-1;j++)
		{
			for (k=j+1;k<N;k++)				
			{
				if (A[j]>A[k])								
					nCrossNum++;
			}
		}


		fout << "Case #" << i+1 << ": " << nCrossNum << endl;
	}
	fin.close();
	fout.close();
	return 0;
}