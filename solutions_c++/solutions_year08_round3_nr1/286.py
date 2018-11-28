#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void main()
{
	int N, P, K, L, n;
	long long re = 0;
	ifstream in("in.txt");
	ofstream out("out.txt");
	in>>N;
	for(int i = 0; i < N; ++ i)
	{
		in>>P>>K>>L;
		vector<int> times(L);
		for(int j = 0; j < L; ++ j) in>>times[j];
		sort(times.begin(), times.end());
		int t = 1;
		re = 0;
		for(int j = times.size() - 1; j >= 0; j -= K)
		{
			for(int k = 0; k < K; ++ k)
			{
				if(j-k >= 0) re += t * times[j-k];
			}
			++ t;
		}
		out<<"Case #"<<i+1<<": "<<re<<endl;
	}
	out.close();
	in.close();
	system("pause");
}