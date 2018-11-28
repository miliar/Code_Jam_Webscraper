#include <string>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

vector<string> getPath(string str)
{
	str = str + "/";
	vector<string> res;
	string curr;
	int i,len = str.length();
	for (i=1;i<len;i++)
	{
		if (str[i] == '/')
		{
			res.push_back(curr);
			curr="";
		}
		else curr = curr + str[i];
	}
	return res;
}

int main()
{
	int T, test;
	cin >> T;
	for (test=0;test<T;test++)
	{
		vector<map<string, int> > dir(1);

		int N, M, i, dirCount = 1, j;
		string str;
		cin >> N>> M;

		int pos= 0, res = 0;
		for (i=0;i<N;i++)
		{
			pos = 0;
			cin >> str;
			vector<string> path = getPath(str);
			for (j=0;j<path.size();j++)
			{
				if (dir[pos].find(path[j])==dir[pos].end() )
				{
					dir[pos][path[j]] = dirCount;
					dirCount++;
					dir.push_back(map<string, int>() );
				}
				pos = dir[pos][path[j]];
			}


		}

		for (i=0;i<M;i++)
		{
			pos = 0;
			cin >> str;
			vector<string> path = getPath(str);
			for (j=0;j<path.size();j++)
			{
				if (dir[pos].find(path[j])==dir[pos].end() )
				{
					res++;
					dir[pos][path[j]] = dirCount;
					dirCount++;
					dir.push_back(map<string, int>() );
				}
				pos = dir[pos][path[j]];
			}

		}
		cout << "Case #" << test+1 << ": " << res << endl;
	}

	return 0;
}