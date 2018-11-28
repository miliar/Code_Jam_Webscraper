#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
using namespace std;

template<typename T, typename S> T cast(S s) {
	stringstream ss;
	ss << s;
	T res;
	ss >> res;
	return res;
}

int main() {

	int icase = 0;
	int iround = 0;
	int ipeople = 0;
	int igroup = 0;
	vector<string> dic;
	fstream infile("A-small.in");
	string line;
	getline(infile, line);
	sscanf(line.c_str(), "%d", &icase);

	for(int i=0; i<icase; i++)
	{
		int res = 0;
		getline(infile, line);
		sscanf(line.c_str(), "%d %d %d", &iround, &ipeople, &igroup);
		getline(infile, line);
		vector<long> g(igroup);
		stringstream ss(line);
		long totalp = 0;
		for(int j=0; j<igroup; j++)
		{
			long t;
			ss >> t;
			g[j] = t;
			totalp += t;
		}

		vector<int> m(igroup, 0);
		int total = 0;
		int begin = 0;
		bool mark = true;
		int cnt = 0;
		while(cnt<iround)
		{
			cnt ++;
			m[begin] = cnt;
			long sum = 0;
			while((sum+g[begin] <= ipeople)&&(sum+g[begin] <= totalp))
			{
				sum += g[begin];
				begin = (begin+1)%igroup;
			}
			if(m[begin])
				mark = false;
			total += sum;
		}

		vector<int> mm(igroup, 0);
		mark = true;
		cnt = 0;
		while(mark)
		{
			cnt ++;
			mm[begin] = cnt;
			long sum = 0;
			while((sum+g[begin] <= ipeople)&&(sum+g[begin] <= totalp))
			{
				sum += g[begin];
				begin = (begin+1)%igroup;
			}
			if(mm[begin])
				mark = false;
		}


			res =  total + 0;
			cout << "Case #" << i+1 << ": " << res << endl;
	}

	return 0;
}
