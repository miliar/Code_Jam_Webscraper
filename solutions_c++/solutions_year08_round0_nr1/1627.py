#include <algorithm>
#include <sstream>
#include <vector>
#include <string>
#include <iostream>
#include <math.h> 
#include <queue>
#include <fstream>

using namespace std;

int main(void)
{
	ifstream in("A-large.in");
	ofstream out("A-large.out");
	int N; in >> N;
	for(int tst=1; tst<N+1; tst++)
	{
		string tem;
		int S; in >> S; getline(in,tem);
		vector <string> engines;
		for(int i=0; i<S; i++)
		{
			string tem; getline(in,tem); 
			engines.push_back(tem);
		}
		int Q; in >> Q; getline(in,tem);
		vector <int> queries;
		if(Q==0) { out << "Case #" << tst << ": " << 0 << endl; continue; }
		for(int i=0; i<Q; i++)
		{
			string tem; getline(in,tem);
			for(int j=0; j<engines.size(); j++)
			{
				if(tem==engines[j]) queries.push_back(j);
			}
		}

		vector <int> b(Q,100000);
		vector <vector<int> > dp(S,b);
		for(int i=0; i<S; i++)
		{
			dp[i][Q-1] = 0;
			if(queries[Q-1]==i) dp[i][Q-1] = 100000;
		}
		// cout << "here" << endl;
		for(int i=Q-1; i>0; i--)
		{
			for(int j=0; j<S; j++)
			{
				if(queries[i]==j) { dp[j][i] = 100000; continue; }
				else
				{
					for(int k=0; k<S; k++)
					{
						if(queries[i-1]!=k)
						{
							dp[k][i-1] = min(dp[k][i-1],1-(k==j)+dp[j][i]);
						}
					}
				}
			}
		}
		int best = 100000;
		for(int i=0; i<S; i++)
		{
			best = min(best,dp[i][0]);
		}
		// cout << tst << " is done" << endl;
		out << "Case #" << tst << ": " << best << endl;
	}
	return -1;
}


				

