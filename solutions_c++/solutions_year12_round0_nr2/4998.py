#include <fstream>
using namespace std;

/*
6
	3 2 1 (*) 	-> 3 -> k
	2 2 2 		-> 2 -> k-1

7
	3 3 1 (*)	-> 3 -> k
	2 2 3		-> 3 -> k
	
8
	4 2 2 (*) 	-> 4 -> k+1
	3 3 2		-> 3 -> k
*/

int main()
{
	ifstream read("input.txt");
	ofstream write("output.txt");
	int T;
	read >> T;
	for (int i = 0; i < T; i ++)
	{
		int N, S, p, t;
		int max = 0, sOffset = 0, doubtCases = 0;
		read >> N >> S >> p;
		for (int j = 0; j < N; j ++)
		{
			read >> t;
			int k = t/3;
			if (t == 0)
			{
				if (p == 0)
				{
					max ++;
				}
			}
			else if (t == 1)
			{
				if (p <= 1)
				{
					max ++;
				}
			}
			else if (t == 29 || t == 30)
			{
				max ++;
			}
			else if (t%3 == 1)
			{
				sOffset ++;
				if (k >= p-1)
				{
					max ++;
				}
			}
			else if (t%3 == 0)
			{
				if (k >= p)
				{
					max ++;
					sOffset ++;
				}
				else if (k < p-1)
				{
					sOffset ++;
				}
				else 
				{
					doubtCases ++;	//max++ and s++ or do nothing
				}
			}
			else if (t%3 == 2)
			{
				if (k >= p-1)
				{
					max ++;
					sOffset ++;
				}
				else if (k < p-2)
				{
					sOffset ++;
				}
				else 
				{
					doubtCases ++;	//max++ and s++ or do nothing
				}
			}
		}
		
		if (doubtCases >= S)
		{
			max += S;
		}
		else 
		{
			max += doubtCases;
		}
			
		write << "Case #" << i + 1 << ": " << max << endl;
	}
	read.close();
	write.close();
	
	return 0;
}