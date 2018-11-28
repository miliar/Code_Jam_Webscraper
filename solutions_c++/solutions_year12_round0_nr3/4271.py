#include <iostream>
#include <fstream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int T, A, B;
	int y;
	vector<int> ys;
	
	ifstream inFile( "C-small-attempt0.in" );
	ofstream outFile( "C-small.txt" );

	inFile >> T;

	for(int i = 0; i < T; i++)
	{
		y = 0;
		int digits = 0;
		inFile >> A >> B;

		int temp = A;
		while (temp) 
		{
			temp /= 10;
			digits++;
		}

		for(int j = A; j <= B; j++)
		{
			int temp = j;
			int ten = pow(10, double(digits-1));
			for(int k=digits-1; k>0; k--)
			{
				temp = int(temp/10) + int((temp%10)*ten);
				for(int k = j+1; k <=B; k++)
				{
					if(temp==k)
					{
						y++;
						break;
					}
				}
			}
		}

		ys.push_back(y);
	}

	for(int i = 0; i < T; i++)
	{
		outFile << "Case #" << i+1 << ": " << ys[i] << endl;
	}

	return 0;
}
