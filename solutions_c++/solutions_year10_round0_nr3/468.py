#include <iostream>
#include <fstream>
#include <cstring>

#define INPUT fin
#define OUTPUT fout

using namespace std;

long long g[1001], sum[1005], nextPos[1001], mark[1001];

void outputAr(int x[], int N)
{
	for(int i=0;i<N;i++)
	{
		cout<<x[i]<<" ";
	}
	cout<<"\n";
}

int main()
{
	int T;
	ifstream fin("c.in");
	ofstream fout("c.out");
	INPUT>>T;
	for(int t=1;t<=T;t++)
	{
		long long R, k, res=0;
		int N, pos=0;
		INPUT>>R>>k>>N;
		
		//sum is the sum of all group size before this group
		sum[0] = 0;
		for(int i=0;i<N;i++)
		{
			INPUT>>g[i];
			sum[i+1] = sum[i] + g[i];
		}
		
		for(int i=0;i<N;i++)
		{
			long long tot=0;
			int j;
			for(j=0;j<N;j++)
			{
				if(tot + g[(i+j)%N] > k)
				{
					break;
				}
				else
				{
					tot += g[(i+j)%N];
				}
			}
			nextPos[i] = (i+j)%N;
		}
		
		//pos is the position of the next group
		int reps=0;
		long long tot=0;
		memset(mark,-1,sizeof(mark));
		for(reps=0, tot=0; mark[pos] == -1; reps++)
		{
			mark[pos] = reps;
			tot += (sum[nextPos[pos]] - sum[pos] + sum[N]) % sum[N];
			if(nextPos[pos] == pos)	tot += sum[N];
			pos = nextPos[pos];
		}
		for(int k=0;k!=pos;k=nextPos[k])
		{
			tot -= (sum[nextPos[k]] - sum[k] + sum[N]) % sum[N];
			R--;
			res += (sum[nextPos[k]] - sum[k] + sum[N]) % sum[N];
		}
		
		res += (R / (reps - mark[pos])) * tot;
		R %= (reps - mark[pos]);
		
		for(int i=0;i<R;i++)
		{
			res += (sum[nextPos[pos]] - sum[pos] + sum[N]) % sum[N];
			pos = nextPos[pos];
		}
		
		OUTPUT<<"Case #"<<t<<": "<<res<<"\n";
	}
	return 0;
}
