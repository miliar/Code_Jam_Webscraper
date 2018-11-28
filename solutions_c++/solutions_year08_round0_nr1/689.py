#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

const int MAXS = 101;
const int MAXQ = 1002;
const int INF = 100000;

int dp[MAXQ][MAXS];


int main()
{
	//ifstream inp("input.txt");
	//ofstream out("output.txt");

	//ifstream inp("A-small.in");
	//ofstream out("A-small.out");

	ifstream inp("A-large.in");
	ofstream out("A-large.out");

	int numCases;
	inp >> numCases;	
	for (int curCase = 1; curCase <= numCases; curCase++)
	{
		int s, q;
		inp >> s;
		string temp;
		getline(inp, temp);
		vector<string> names(s);
		
		for (int i = 0; i < s; i++) getline(inp,  names[i]);

		inp >> q;
		getline(inp, temp);
		string query;
		vector<int> queries(q, -1);
		for (int i = 0; i < q; i++) 
		{
			getline(inp, query);
			for (int j = 0; j < s; j++) 
				if (query == names[j])
				{
					queries[i] = j;
					break;
				}
			if (queries[i] == -1) out << "ERROR!!" << endl;
		}

		//Solution
		for (int i = 0; i < MAXQ; i++)
			for (int j = 0; j < MAXS; j++) dp[i][j] = INF;

		for (int j = 0; j < s; j++) dp[0][j] = 0;

		for (int i = 0; i < q; i++)
			for (int j = 0; j < s; j++)
					if (dp[i][j] != INF)
					{
						if (queries[i] == j)
						{
							for (int h = 0; h < s; h++)
								if (h != j) dp[i + 1][h] = min(dp[i][j] + 1, dp[i + 1][h]);
						}
						else dp[i + 1][j] = min(dp[i][j], dp[i + 1][j]);
					}
		int ans = INF;
		for (int i = 0; i < s; i++)
			ans = min(ans, dp[q][i]);

		out << "Case #" << curCase << ":" << " " << ans << endl;

	}

	return 0;
}