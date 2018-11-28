

#include <iostream>
#include <fstream>
#include <climits>
using namespace std;

void main()
{
	ifstream infile;
	infile.open("in.txt", ios::in);
	ofstream outfile;
	outfile.open("out.txt", ios::out | ios::trunc);
	int T, N;
	int candy[1000];
	
	infile>>T;
	int test = 0;
	while(++test <= T)
	{
		infile>>N;
		int result = 0;
		for(int i = 0; i < N; ++i)
		{
			infile>>candy[i];
			result ^= candy[i];
		}
		result ^= 0;
		if(result == 0)
		{
			int min = INT_MAX, sum = 0;
			for(i = 0; i < N; ++i)
			{
				sum += candy[i];
				if(min > candy[i])
					min = candy[i];
			}
			sum -= min;
			outfile<<"Case #"<<test<<": "<<sum<<endl;
		}else{
			outfile<<"Case #"<<test<<": NO"<<endl;
		}
	}
	infile.close();
	outfile.close();
	return;
}