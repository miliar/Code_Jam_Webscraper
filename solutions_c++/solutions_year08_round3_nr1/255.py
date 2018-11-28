#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <list>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
#include <fstream>
using namespace std;


int main()
{
	ifstream fin("in.in");
	ofstream fout("out.out");
	int N;
	fin>>N;
	int P,K,L;
	for (int cc=1;cc<=N;++cc)
	{
		fin>>P>>K>>L;

//		fout<<"Case #"<<cc<<<": "<<"Impossible"<<endl;

		vector<int> frquency(L);
		for (int j=0;j<L;++j)
		{
			fin>>frquency[j];
		}
		sort(frquency.begin(),frquency.end(),greater<int>());
		long long ans=0;
		for (int j=0;j<frquency.size();++j)
		{
			int press=j/K+1;
			ans+=frquency[j]*press;
		}

		fout<<"Case #"<<cc<<": "<<ans<<endl;
	}

	return 0;
}

