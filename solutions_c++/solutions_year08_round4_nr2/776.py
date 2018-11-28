#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <ctime>
#include <fstream>

using namespace std;


int main()
{
	ifstream input("input.txt");
	ofstream outputfile("output.txt");
	int sz ;
	
	input >> sz ;

	for( int casen = 1 ; casen <= sz;  ++casen)
	{
		int k ;
		string s;
		input >> k >> s;
		vector<int> perm;
		for( int i = 0 ; i < k ; ++i) perm.push_back(i);
		int res = 10000000;
		
		do
		{
			string work = s;
			for( int i = 0 ; i < s.size(); i += k )
			{
				for( int j = 0 ; j <  k ; ++j)
				{
					work[i + j ] = s[i + perm[j]] ;
				}

			}

			int tres = 1;

			char last = work[0];
			
			for( int i = 1 ; i < work.size();++i)
			{
				if(last != work[i] ) ++tres;
				last = work[i];
			}
			
			res = min(res,tres);

		}while(next_permutation(perm.begin(),perm.end()));



		outputfile << "Case #" << casen << ": "  << res << endl;
	}
	getchar();
	return 0;
}
