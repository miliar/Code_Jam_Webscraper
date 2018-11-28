#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

int main()
{
	int T;
	cin>>T;

	for(int i = 0; i < T; ++i)
	{
		int N;
		cin>>N;

		map<int,int> A;
		for(int j = 0; j < N; ++j)
		{
			int a,b;
			cin>>a>>b;

			A.insert(make_pair(a,b));
		}

		int ret = 0;
		for(map<int,int>::iterator j = A.begin(); j != A.end(); ++j)
		{
			int h = j->second;
			map<int,int>::iterator k = j;
			for( ++k; k != A.end(); ++k)
				if(h > k->second)
					++ret;
		}

		cout<<"Case #"<<i+1<<": "<<ret<<endl;
	}
}