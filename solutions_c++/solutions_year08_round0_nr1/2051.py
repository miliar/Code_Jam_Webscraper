#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

int get_int(string str)
{
	stringstream s(str);
	int n;
	s >> n;
	return n;
}

int main()
{
	fstream fin("C:\\Projects\\GCJ\\input", std::ios_base::in);
	fstream fout("C:\\Projects\\GCJ\\output", std::ios_base::out);

	string temp;
	char ch;
	int N;
	getline(fin, temp, '\n');
	N = get_int(temp);
	int cases = N;
	while (N > 0)
	{
		N--;
		vector<string> s;
		int S;
		getline(fin, temp, '\n');
		S = get_int(temp);
		while (S > 0)
		{
			S--;
			getline(fin, temp, '\n');
			s.push_back(temp);
		}

		vector<string> q;
		int Q;
		getline(fin, temp, '\n');
		Q = get_int(temp);
		while (Q > 0)
		{
			Q--;
			getline(fin, temp, '\n');
			q.push_back(temp);
		}

		/*cout << s.size() << endl;
		for (int i=0;i<s.size();i++)
		{
			cout << s[i] << endl;
		}

		cout << q.size() << endl;
		for (int j=0;j<q.size();j++)
		{
			cout << q[j] << endl;
		}*/

		int dp[1001][101];
		int i,j;
		for (i=0;i<q.size();i++)
		{
			for (j=0;j<s.size();j++)
				dp[i][j] = 0;
		}

		for (i=q.size()-1;i>=0;i--)
		{
			for (j=s.size()-1;j>=0;j--)
			{
				if (i == q.size()-1)
				{
					if (q[i] == s[j])
						dp[i][j] = 1;
					continue;
				}

				int min = dp[i+1][j];
				if (q[i] == s[j])
				{
					min = 1000000;
					for (int k=0;k<s.size();k++)
					{
						if (k == j)
							continue;
						if (1 + dp[i+1][k] < min)
							min = 1 + dp[i+1][k];
					}
				}

				dp[i][j] = min;

				/*for (int a=0;a<q.size();a++)
				{
					for (int b=0;b<s.size();b++)
					{
						cout << dp[a][b] << " ";
					}
					cout << endl;
				}
				cin >> ch;*/
			}
		}

		int res = 1000000;
		for (i=0;i<s.size();i++)
		{
			if (dp[0][i] < res)
				res = dp[0][i];
		}

		if (q.size() == 0)
			res = 0;
		cout << "Case #" << (cases-N) << ": " << res << endl;
		fout << "Case #" << (cases-N) << ": " << res << endl;
	}

	fin.close();
	fout.close();
	cin >> ch;

	return 0;
}