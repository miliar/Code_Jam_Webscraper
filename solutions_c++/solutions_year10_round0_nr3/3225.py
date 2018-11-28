#include <fstream>
#include <iostream>
using namespace std;


int main (int argc, char **argv)
{
	if (2 != argc)
		return -1;

	ifstream file;

	file.open(argv[1]);
	if (false == file.is_open())
	{
		printf("\nCannot open file\n");
		return -1;
	}	
	unsigned int mas [1000];
	int p = 0;
	unsigned int j, i = 0, k = 0, R, N, z = 0, t = 1;
	unsigned long long np, d = 0;
	file >> t;
	while(false == file.eof()  && z !=t )
	{
		file >> R >> k >> N;
		d = 0; np = 0;
		for (i=0;i<N;i++)
		{
			file>>mas[i];
			np+=mas[i];
		}
		
		for (i = 0, p = 0; i < R; ++i)
		{
			j = 0;			
			for (; j <= k && (j < np); )
			{		
				j+=mas[p];
				p = (p+1) % N;				
			}
			if (j > k)
			{
				p = (p - 1);
				if (p<0) 
					p+=N;
				j -= mas[p];
			}
			d += j;
		}
		z++;		
		printf("Case #%d: %I64u \n", z, d);		
	};
	file.close();
	return 0;
}