#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
	freopen("a.in.txt" , "r" ,stdin);
	//ifstream fin;
	//fin.open()
	int casenum;
	cin >> casenum;
	for (int casecount = 0; casecount < casenum; casecount++)
		{
			map<string, int> engine;
			vector<int> q;
			engine.clear();
			int engnum;
			cin >> engnum; getchar();
			for (int engcount = 0; engcount < engnum; engcount++)
			{
				string temp;
				getline(cin, temp);
				//cout << temp << endl;
				engine[temp]=engcount;
			}
			int qnum;
			cin >> qnum; getchar();
			for (int qcount = 0; qcount < qnum; qcount++)
			{
				string temp;
				getline(cin, temp);
				//cout << temp << endl;
				if (engine.count(temp) > 0) // searching a engine!
					q.push_back( engine[temp] );
			}
			//for (int i = 0; i < q.size(); i++)
			//	cout << q[i] << " ";
			//cout << endl;
			int res = 999999999;
			int dp[1000][100];
			for (int i = 0; i < 1000; i++)
				for (int j = 0; j < 100; j++)
					dp[i][j] = 999999999;
				
			int qsize = q.size();
			if (qsize == 0)
			{
				res = 0;
				cout << "Case #" << casecount + 1 << ": " << res << endl;
				continue;
			}
			for (int i = 0; i < engnum; i++)
			{
				if (q[0] != i)
					dp[0][i] = 0;
			}
			
			for (int i = 1; i < qsize; i++)
				for (int j = 0; j < engnum; j++)
					for (int k = 0; k < engnum; k++)
					{
						if (j == q[i]) 
						{
							continue;
						}
						if (k == j)
						{
							dp[i][j] = min(dp[i][j], dp[i-1][k]);
						}
						else
						{
							dp[i][j] = min(dp[i][j], dp[i-1][k] + 1);
						}
					}
					
			for (int i = 0; i < engnum; i++)
				res = min(res, dp[qsize-1][i]);
			cout << "Case #" << casecount + 1 << ": " << res << endl;
			/*for (int i = 0; i < qsize; i++)
			{
				int engused = 0;
				int tempres = 9999999;
				for (int j = 0; j < engnum; j++)
					if (dp[i][j] < tempres)
					{
						tempres = dp[i][j];
						engused = j;
					}
				cout << "query for : " << q[i] << "; enging used: " << engused << endl;
			}
			cout << endl;*/
		}
		
	return 0;
}
