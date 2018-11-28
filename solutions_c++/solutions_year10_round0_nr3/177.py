#include<cstdio>
#include<cmath>
#include<fstream>
#include<iostream>
using namespace std;

struct Group
{
	int value;
	int to;
	long long sum;
} g[1010];

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt" );
	
	int T;
	fin >> T;

	long long result;
	int R, K, N;
	for(int i = 1; i <= T; ++i)
	{
		result = 0;
		fin >> R >> K >> N;
		long long sum = 0;
		for(int j = 0; j < N; ++j)
		{
			fin >> g[j].value;
			sum += g[j].value;
		}
		if(sum > K)
		{
			for(int i1 = 0; i1 < N; ++i1)
			{
				long long tmp = g[i1].value;
				if(tmp > K)
				{
					g[i1].sum = 0;
					continue;
				}
				int ite = i1+1;
				while(tmp + g[ite%N].value <= K)
					tmp += g[(ite++)%N].value;
				g[i1].to = ite%N;
				g[i1].sum = tmp;
			}
			int cur = 0;
			for(int i1 = 0; i1 < R; ++i1)
			{
				result += g[cur].sum;
				if(g[cur].sum == 0)
					break;
				cur = g[cur].to;
			}
		}
		else
		{
			result = sum * (long long)R;
		}
		fout << "Case #" << i << ": " << result << endl;
	}

	fin.close();
	fout.close();
	return 0;
}