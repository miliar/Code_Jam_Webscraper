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
ifstream fin("in.txt");
ofstream fout("out.txt");

int main()
{
	int N;
	fin>>N;
	long long ans=0;

	for (int cc=1;cc<=N;++cc)
	{
		int m;
		fin>>m;
		vector<long long> A(m);
		vector<long long> B(m);
		for (int i=0;i<m;++i)
		{
			fin>>A[i];
		}
		for (int i=0;i<m;++i)
		{
			fin>>B[i];
		}
		sort(A.begin(),A.end(),less<long long>());
		sort(B.begin(),B.end(),greater<long long>());
		ans=0;
		for (int i=0;i<m;++i){
			ans+=A[i]*B[i];
		}
		fout<<"Case #"<<cc<<": "<<ans<<endl;


	}
	return 0;
}

