#include <iostream>
#include <iomanip>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <numeric>
using namespace std;
typedef long long LL;


int solve(vector<string>& F, int M, int N)
{
	vector<int> dp(1<<N, -1); // ok_pattern --> max_person
	dp[(1<<N)-1] = 0;

	for(int i=0; i!=F.size(); ++i)
	{
		int mask = (1<<N)-1;
		for(int j=0; j!=F[i].size(); ++j)
			if( F[i][j] == 'x' )
				mask &= ~(1<<j);

		vector<int> dp2(1<<N, -1);

		for(int j=0; j!=dp.size(); ++j) if(dp[j] != -1)
		{
			int okp = j & mask;
			for(int mypat=0; mypat<(1<<N); ++mypat)
				if( (mypat & okp) == mypat )
				{
					// no tonari condition
					if( mypat & (mypat<<1) )
						continue;
					int bitpop = 0;
					for(int k=0; k<N; ++k)
						if( mypat & (1<<k) )
							bitpop ++;

					int nextpat = ((1<<N)-1) & ~(mypat<<1) & ~(mypat>>1);
					dp2[nextpat] = max(dp2[nextpat], dp[j]+bitpop);
				}
		}

		dp.swap(dp2);
	}

	return *max_element(dp.begin(), dp.end());
}



int main()
{
	int NUM_CASE; cin >> NUM_CASE;
	for(int caseID=1; caseID<=NUM_CASE; ++caseID)
	{
		int M, N;
		cin >> M >> N;
		vector<string> F(M);
		for(int i=0; i!=M; ++i)
			cin >> F[i];

		cout << "Case #" << caseID << ": " << solve(F, M, N) << endl;
	}
}
