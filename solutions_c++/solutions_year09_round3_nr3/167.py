/*************************
 * jhurwitz              *
 * Round 1C              *
 * "Bribe the Prisoners" *
 *************************/

#include <fstream>
#include <cstring>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("C-large.out");

void bribe(int casenum)
{
	int P, Q;
	fin >> P >> Q;
	int locs[105];
	locs[0] = 0;
	for (int i=1; i<=Q; i++)
		fin >> locs[i];
	locs[Q+1] = P+1;
	int dp[105][105]; //min cost of releasing ith through jth if there are no empty cells
	memset(dp, 0, sizeof(dp)); //can init with 0 because dp[i][i+1]=0
	for (int diff=2; diff<=Q+1; diff++)
		for (int a=0, b=diff; b<=Q+1; a++, b++) //want to find dp[a][b]
		{
			dp[a][b]=1000000000;
			for (int k=a+1; k<=b-1; k++)
				if (dp[a][b]>dp[a][k]+dp[k][b])
					dp[a][b]=dp[a][k]+dp[k][b];
			dp[a][b] += locs[b]-locs[a]-2;
		}
	fout << "Case #" << casenum << ": " << dp[0][Q+1] << endl;
}

int main()
{
	int T;
	fin >> T;
	for (int i=0; i<T; i++)
		bribe(i+1);
}

