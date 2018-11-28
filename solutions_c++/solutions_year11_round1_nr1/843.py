#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
using namespace std;

void main(void)
{
	int T, Pd, Pg;
	long long N;

	ifstream fin("A-large.in");
	ofstream fout("output.txt");
	fin >> T;
	int tempT = T;
	while(T--)
	{
		fin >> N >> Pd >> Pg;
		if(Pg == 100 && Pd != 100)
		{
			fout << "Case #" << tempT - T <<": Broken" << endl;
			continue;
		}
		if(Pg == 0 && Pd > 0)
		{
			fout << "Case #" << tempT - T <<": Broken" << endl;
			continue;
		}
		if(Pg == 100 && Pd == 100 || Pd == 0)
		{
			fout << "Case #" << tempT - T <<": Possible" << endl;
			continue;
		}

		//bool flag = false;
		int i;
		for( i = 1; i <= N; ++i)
		{
			if( (i * Pd) % 100 == 0 )
			{
				//flag = true;
				fout << "Case #" << tempT - T <<": Possible" << endl;
				break;
			}
		}
		if( i > N )
			fout << "Case #" << tempT - T <<": Broken" << endl;
	}
}

