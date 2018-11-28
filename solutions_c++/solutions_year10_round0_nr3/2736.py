#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char * argv[])
{
	fstream infile, outfile;
	infile.open("C.in", ios_base::in);
	outfile.open("C.out", ios_base::out);

	int T, R, k, N, g[1000] = {0};
	
	infile >> T;

	for( int l = 0; l < T; l++)
	{
		infile >> R >> k >> N;
		for( int fuck = 0; fuck < N; fuck++ )
			infile >> g[fuck];

		int income = 0;
		int delay = 0;
		int i  = 0;

		while( R > 0 )
		{
			int awaits = N;

			for( int room = k; room > 0; )
			{
				if( room < g[i%N] || awaits == 0)
					break;
				else
				{
					room -= g[i%N];
					income += g[i%N];
					i++;
					awaits--;
				}
			}

			R--;
		}
		outfile << "Case #" << l+1 << ": " << income << endl;
	}
	infile.close();
	outfile.close();

	return 0;
}