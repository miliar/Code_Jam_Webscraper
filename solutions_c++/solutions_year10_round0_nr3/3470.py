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
	string infile_name("K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Codejam2010\\C");
	string outfile_name("K:\\Settings And Documents\\Document\\Visual Studio 2008\\Projects\\Codejam2010\\C_out");
	fstream infile(infile_name.c_str(), fstream::in);
	fstream outfile(outfile_name.c_str(), fstream::out | fstream::trunc | fstream::binary);
	string buff;
	
	getline(infile, buff);
	istringstream first_line(buff);

	unsigned int n;
	first_line >> n;
	for(unsigned int count = 0; count < n; ++count )
	{
		int R, k ,N;
		getline(infile, buff);
		istringstream inputs(buff);
		inputs >> R >> k >> N;
		deque<unsigned int> group(N, 0);
		getline(infile, buff);
		istringstream inputs2(buff);
		istream_iterator<int> it(inputs2);
		istream_iterator<int> end;
		group.assign(it, end);
		int group_size= group.size();
		unsigned __int64 result = 0;
		for(int round = 0; round < R; ++round)
		{
			int k_tmp = k;
			int group_num = 0;
			while( k_tmp >= group.front() && group_num < group_size)
			{
				group.push_back(group.front());
				k_tmp -= group.front();
				result += group.front();
				group.pop_front();
				++group_num;
			}
		}
		outfile << "Case #" << count+1 << ": " << result << endl;
	}
	return 0;
}