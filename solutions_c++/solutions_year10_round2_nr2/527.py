#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <ios>
#include <functional>

using namespace std;
typedef unsigned long long ull;

int main()
{
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");
	
	if(ifs.is_open() && ofs.is_open())
	{
		int T;
		ifs>>T;
		int t=0;
		while(ifs.good() && t<T)
		{
			int N, K, B, T;
			ifs>>N>>K>>B>>T;
			int *X = new int[N];
			int *V = new int[N];
			int *Fast = new int[N];
			memset(Fast, 0, N*sizeof(int));
			for(int i=0;i<N;i++)
				ifs>>X[i];
			for(int i=0;i<N;i++)
				ifs>>V[i];

			int count = 0;
			for(int i=0;i<N;i++)
				if(X[i]+T*V[i]>=B)
				{
					count++;
					Fast[i] = 1;
				}

			if(count<K)
			{
				ofs<<"Case #"<<++t<<": "<<"IMPOSSIBLE"<<"\n";
			}
			else
			{
				int res = 0;
				int fast = 0;
				int slow_count = 0;
				for(int i = N-1; i>=0; i--)
				{
					if(!Fast[i])
						slow_count++;
					else
					{
						res+=slow_count;
						fast++;
					}
					if(fast == K)
						break;
				}
				ofs<<"Case #"<<++t<<": "<<res<<"\n";
			}
			cout<<t<<" complited\n";
			delete X;
			delete V;
			delete Fast;

		}
	}
	ifs.close();
	ofs.close();
	return 0;
}