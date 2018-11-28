#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <numeric>
#include <iterator>

using namespace std;

int main()
{
	string infile_name("K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Codejam2010\\A");
	string outfile_name("K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Codejam2010\\A_out");
	fstream infile(infile_name.c_str(), fstream::in);
	fstream outfile(outfile_name.c_str(), fstream::out | fstream::trunc | fstream::binary);
	string buff;
	istringstream buff_stream;

	getline(infile, buff);
	buff_stream.str(buff);

	unsigned int n;
	buff_stream >> n;
	for(unsigned int count = 1; count <= n; ++count )
	{
		getline(infile, buff);
		istringstream buff_stream2(buff);
		unsigned int K, N;
		buff_stream2 >> N >> K;

		vector<int> state(N, 0);
		for(unsigned int snap = 0; snap < K; ++snap)
		{
			for(unsigned int device = 0; device < N; ++device)
			{
				if(state[device] == 0)
				{ state[device] = 1; break; }
				else
				{ state[device] = 0; }
			}
		}
		bool powered = true;
		for(unsigned int device = 0; device < N && powered == true; ++device)
		{
			powered &= (state[device] == 1);
		}

		outfile << "Case #" << count << ": ";
		if(powered)
		{ outfile << "ON"; }
		else
		{ outfile << "OFF"; }
		outfile << endl;
	}
	return 0;
}