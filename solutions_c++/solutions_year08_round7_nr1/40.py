#include <fstream>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>


using namespace std;
string r[1000];
int n;
int m[1000];
int solution;
string mix[1000][1000];

int find(int node)
{
	vector <int> ttt;
	ttt.clear();
	int max;
	int cnt;
	for(int i = 0 ; i < m[node]; i++)
	{
		if(mix[node][i].at(0) >= 'A' && mix[node][i].at(0) <= 'Z') {
			for(int j = 0; j < n; j++)
			{
				if(r[j] == mix[node][i]) 
				{
					ttt.push_back(find(j));
					break;
				}
			}
		}
	}
	sort(ttt.begin(), ttt.end());
	max = 1 + ttt.size();
	cnt = 0;
	for(int i = ttt.size() - 1; i >= 0; i--)
	{
		if(cnt + ttt[i] > max) max = cnt + ttt[i];
		cnt++;
	}
	return max;
}


int main()
{
	ifstream fin("problem1.in");
	ofstream fout("problem1.out");

	int C;

	fin >> C;
	for(int test_case = 1; test_case <= C; test_case++)
	{
		fout << "Case #" << test_case << ": ";
		fin >> n;
		for(int i = 0; i < n; i++)
		{
			fin >> r[i] >> m[i];
			for(int j = 0; j< m[i]; j++)
			{
				fin >> mix[i][j];
			}
		}
		solution = 0;
		fout << find(0) << endl;
	}

	fin.close();
	fout.close();
	return 0;
}