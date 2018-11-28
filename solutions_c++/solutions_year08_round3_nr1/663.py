#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

struct Coord
{
	int x;
	int y;
};


int main
(
	int argc,
	const char * argv[]
) {

	// check that we have sufficient arguments
	if (argc<3) return 1;

	// open files
	const char * fname_in = argv[1];
	const char * fname_out = argv[2];
	ifstream infile(fname_in);
	ofstream outfile(fname_out);

	// work
	string tmp;
	getline(infile, tmp, (char)'\n');
	int rounds = atoi(tmp.c_str());
	cout << "Rounds : " << rounds << endl;

	// loop through rounds
	for (int i = 0; i < rounds; i++)
	{

		int P, K, L, t;
		infile >> P >> K >> L;

		vector<int> lets;

		int * pk = new int[K];
		memset(pk, 0, K * sizeof(int));		

		for (int j = 0; j < L; j++)
		{		
			infile >> t;
			lets.push_back(t);
		}

		sort(lets.begin(), lets.end());

		long totpress = 0;

		// loop through keys
		for (int j = lets.size() - 1; j >= 0; j--)
		{
			
			int pos;
			bool found = false;

			// loop through pos
			for (int p = 0; p < P && !found; p++)
			{
				// allocate to 
				for (int k = 0; k < K && !found; k++)
				{
					if (pk[k]==p)
					{
						pos = p;
						pk[k]++;
						found = true;
					}
				}
			}

			totpress += (pos+1) * lets[j];

		}

		free(pk);

		// get the solution
		outfile << "Case #" << (i+1) << ": " << totpress << endl;

	}

	// close files
	infile.close();
	outfile.close();

}
