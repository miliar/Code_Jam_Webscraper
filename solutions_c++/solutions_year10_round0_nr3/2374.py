#include <fstream>
using namespace std;

int main()
{
	int T, R, k, N;
	int sta, sum, res;
	int g[1000];
	ifstream fin("test.in");
	ofstream fout("test.out");

	fin>>T;
	for(int i=1; i<=T; i++)
	{
		res = 0;
		sum = 0;
		fin>>R>>k>>N;
		for(int j=0; j<N; j++)
		{
			fin>>g[j];
			sum += g[j];
		}
		fout<<"Case #"<<i<<": ";
		if( sum < k )
		{
			fout<<sum*R<<endl;
			continue;
		}
		sta = 0;
		for(int j=1; j<=R; j++)
		{
			int cnt=0, t;
			for(int jj=0; jj<N; jj++)
			{
				t = (sta+jj)%N;
				if( cnt+g[t] <= k )
					cnt += g[t];
				else
				{
					t = (t-1)%N;
					break;
				}
			}
			sta = (t+1)%N;
			res += cnt;
		}
		fout<<res<<endl;
	}

	return 0;
}
