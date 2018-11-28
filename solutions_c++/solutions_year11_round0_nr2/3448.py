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

#include <unordered_map>
#include <unordered_set>

#include <assert.h>
using namespace std;

typedef pair <string, char> inPair;

unordered_map<string, char> hm_combine;
unordered_set<string> hs_clear;

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

	for (nCur = 0; nCur < nTest; nCur++)
	{
		int nC = 0;
		int nD = 0;	
		int nN = 0;	
		string datai;

		hm_combine.clear();
		hs_clear.clear();

		in_file >> nC;
		for (int i = 0; i < nC; i++)
		{
			string tmp;
			in_file >> tmp;

			string key(tmp, 0, 2);	
			char value = tmp[2];

			hm_combine.insert(pair<string, char>(key, value));
		}

		in_file >> nD;
		for (int i = 0; i < nD; i++)
		{
			string tmp;
			in_file >> tmp;
			hs_clear.insert(tmp);
		}

		in_file >> nN;

		datai.clear();
		in_file >> datai;

		for (int i = 1; i < nN; i++)
		{
			string combine_rse; 
			combine_rse.clear();
			combine_rse += datai[i];
			combine_rse += datai[i-1];

			string combine;
			combine.clear();
			combine	+= datai[i-1];
			combine += datai[i];

			unordered_map<string, char>::iterator itr = hm_combine.find(combine);
			unordered_map<string, char>::iterator itr_rev = hm_combine.find(combine_rse);
			if (itr != hm_combine.end())
			{
				datai[i-1] = itr->second;
				datai[i] = 0;
				continue;
			}
			if (itr_rev != hm_combine.end())
			{
				datai[i-1] = itr_rev->second;
				datai[i] = 0;
				continue;
			}
			for (int j=0; j<i; j++)
			{
				string str_clear;
				str_clear.clear();
				str_clear += datai[j];
				str_clear += datai[i];

				string clear_rse; 
				clear_rse.clear();
				clear_rse += datai[i];
				clear_rse += datai[j];

				if ( (hs_clear.find(str_clear) != hs_clear.end()) 
						|| (hs_clear.find(clear_rse) != hs_clear.end()) )
				{
					for(int idx = 0; idx <= i; idx++)
					{
						datai[idx] = 0;
					}
					break;
				}
			}
		}

		out_file << "Case #" << nCur + 1 << ": ["; 
		int idx_i = 0;
		while (idx_i < nN)
		{
			if (datai[idx_i] != 0)
			{
				out_file << datai[idx_i];
				break;
			}
			idx_i ++;
		}
		for (int i = idx_i+1; i < nN; i++)
		{
			if (datai[i] == 0)
				continue;
			out_file << ", " << datai[i] ;
		}

		out_file << "]" << endl;
	}

	in_file.close();
	out_file.close();

	return 0;
}
