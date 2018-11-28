#include <fstream>
#include <vector>
#include <map>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#include <assert.h>
using namespace std;

#define MAX_NUM 100
char n_icolor[MAX_NUM];
int n_inum[MAX_NUM];
int objo;
int curo;
int objb;
int curb;

int main( int argc, char* argv[] )
{
	if( argc != 3 )
	{
		return -1;
	}

	ifstream in_file( argv[1], ifstream::in );
	ofstream out_file( argv[2], ofstream::out|ofstream::trunc );

	int nTest, nCur;

	in_file >> nTest;
	int nN;

	for (nCur = 0; nCur < nTest; nCur++)
	{
		in_file >> nN;
		curb = 1;
		curo = 1;

		for (int i = 0; i < nN; i++)
		{
			in_file >> n_icolor[i];
			in_file >> n_inum[i];
		}

		int ans = 0;

		int j = 0;
		while (j < nN)
		{
			int steps = 0;

			if (n_icolor[j] == 'O')
			{
				objo = n_inum[j];
				steps += abs(objo - curo) + 1;
				curo = objo;
			}
			else
			{
				objb = n_inum[j];

				steps += abs(objb - curb) + 1;

				curb = objb;
			}

			ans += steps;
			for (int k = j+1; k < nN; k++)
			{
				if (n_icolor[k] != n_icolor[j])
				{
					if (n_icolor[k] =='O')
					{
						objo = n_inum[k];

						if (curo == objo)
							break;

						if (curo < objo)
						{
							curo += steps;
							if (curo > objo)
							{
								curo = objo;
							}
						}
						else
						{
							curo -= steps;
							if (curo < objo)
							{
								curo = objo;
							}
						}
					}
					else
					{
						objb = n_inum[k];

						if (curb == objb)
							break;

						if (curb < objb)
						{
							curb += steps;
							if (curb > objb)
							{
								curb = objb;
							}
						}
						else
						{
							curb -= steps;
							if (curb < objb)
							{
								curb = objb;
							}
						}
					}
					break;
				}
			}
			j++;
		}

		//output the result
		out_file << "Case #" << nCur + 1 << ": " << ans << endl;
	}

	in_file.close();
	out_file.close();

	return 0;
}
