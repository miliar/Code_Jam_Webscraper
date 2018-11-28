/*
ID: BlackMagic
PROG: A
LANG: C++
*/
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

const int MAXQ = 1010;
int q[MAXQ],dp[MAXQ][110],pos[MAXQ][110];

int N,S,Q;

int go()
{
	memset(dp, -1, sizeof(dp));
	for(int i = 0; i < 110; i++)
		dp[0][i] = 0;
	for(int i = 1; i <= Q; i++)
	{		
		for(int j = 0; j < S; j++)
		{
			for(int k = 0; k < S; k++)
			{
				if(j != k && k != q[i])
				{
					if(dp[i][j] < 0 || dp[i][j] > dp[i-1][k]+1)
						dp[i][j] = dp[i-1][k]+1;
				}
				else if(j == k && k != q[i])
				{
					if(dp[i][j] < 0 || dp[i][j] > dp[i-1][k])
						dp[i][j] = dp[i-1][k];
				}
			}

		}
	}

	//for(int i = 0; i <= Q; i++)
	//{
	//	for(int j = 0; j < S; j++)
	//		fout << dp[i][j] << "\t";
	//	fout << endl;
	//}

	int best = 10000;
	for(int i = 0; i < S; i++)
		if(dp[Q][i] >= 0 && dp[Q][i] < best)
			best = dp[Q][i];
	return best;
}

int main() {
    ofstream fout ("A.out");
    ifstream fin ("A.in");
	string s;

	fin >> N;
	map<string, int> msi;
	for(int k = 1; k <= N; k++)
	{
		fin >> S;
		msi.clear();
		getline(fin, s);
		for(int i = 0; i < S; i++)
		{
			getline(fin, s);
			msi.insert(make_pair(s,i));
		}
		fin >> Q;
		getline(fin, s);
		for(int i = 1; i <= Q; i++)
		{
			getline(fin, s);
			q[i] = msi.find(s)->second;
		}

		int res = go();
		fout << "Case #" << k << ": " << res << endl;
	}
    return 0;
}