#include <list>
#include <fstream>
#include <stack>
#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

const int size = 101;

ifstream fin("input.txt");
ofstream fout("output.txt");

map<string, int> queryCount;
vector<string> queryList;
vector<string> engineList;

int dp[size][size];

int search(int p, int start, int end)
{
	int res = -1;
	bool flag = true;
	for (int i=start; i<end; i++)
	{
		if (queryList[i] == engineList[p])
		{
			flag = false;
			for (int j=0; j<engineList.size(); j++)
			{
				if (j == p)
				{
					continue;
				}
				int t;
				if (dp[j][i] != -1)
				{
					t = dp[j][i] + 1;
				}else
					t = search(j, i, end) + 1;
				if (res == -1 || res > t)
				{
					res = t;
				}
			}
			break;
		}
	}
	if (flag)
	{
		res = 0;
	}
	dp[p][start] = res;
	return res;
}

int main()
{
	int n;
	
	char temp[size];
	fin.getline(temp, size);
	n = atoi(temp);
	int i, j, k;
	for (int m=0; m<n ; m++)
	{
		queryCount.clear();
		queryList.clear();
		engineList.clear();
		memset(dp, -1, size*size*sizeof(int));
		
		string word = "";
		int num;
		fin.getline(temp, size);
		num = atoi(temp);
		for (int x=0; x<num; x++)
		{
			word = "";
			memset(temp, '\0', size*sizeof(char));
			fin.getline(&temp[0], size);
			word += temp;
			//cout << temp << ", "<<word<<endl;
			engineList.push_back(word);
		}
		fin.getline(temp, size);
		num = atoi(temp);
		for (int x=0; x<num; x++)
		{
			word = "";
			memset(temp, '\0', size*sizeof(char));
			fin.getline(&temp[0], size);
			word += temp;
			//cout << temp << ", "<<word<<endl;
			queryCount[word]++;
			queryList.push_back(word);
		}
		int res = -1;
		//res = search(0, 0, queryList.size());
		//cout << m+1<<" res: " << res << endl;
		for (int j=0; j<engineList.size(); j++)
		{
			int t = search(j, 0, queryList.size());
			if (res == -1 || res > t)
			{
				res = t;
			}
		}
		if (res == -1)
		{
			res = 1;
		}
		fout << "Case #"<< m+1 <<": "<<res << endl;
	}
	return 0;
}