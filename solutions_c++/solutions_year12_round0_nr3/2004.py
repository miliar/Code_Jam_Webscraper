#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
using namespace std;

#define maxDigits (8)
int rotate(int N, int j)
{
	int M = 0;
	M=(N%((int)pow((float)10,j))*((int)pow((float)10,(int)log10((float)N)+1-j))+(N/((int)pow((float)10,j))));
	return M;
}

int _tmain(int argc, _TCHAR* argv[])
{
		std::ifstream infile("C-large.in");	
		std::ofstream outfile("C-large.out");
		cout<<setprecision(7);


		int totalCases = 0;

		infile>>totalCases;


		for (int i = 1;i<=totalCases;i++)
		{
			int recycledPairs = 0;
			int A,B,N,M;
			infile>>A>>B;
			{
				int pastMValues[maxDigits];
				for (N=A;N<B;N++)
					for (int j = 1;j<(int)log10((float)N)+1;j++)
					{
						M = rotate(N,j);
						pastMValues[j] = M;
						bool mIsUnique = true;
						for (int k = 1;k<j;k++)
						{
							if (pastMValues[k]==pastMValues[j])
							{
								mIsUnique=false;
							}
						}
						if (A<=N &&N<M &&M<=B && mIsUnique)
							recycledPairs++;
					}



			}
			outfile<<"Case #"<<i<<": "<<recycledPairs<<endl;


		}
		return 0;

}