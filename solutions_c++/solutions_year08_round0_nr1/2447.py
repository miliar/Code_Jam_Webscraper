#include <iostream>
#include <vector>
#include <fstream>
#include<string>
using namespace std;
#define MIN(a,b) ((a<b)?(a):(b))

class abcd
{
	public:
		int abc[1000][100];
		vector<string> engine;
		vector<string> query;
		int min_sw(int q, int e)
		{
			if (q == query.size())
				return 0;
			if (abc[q][e] != -1)
				return abc[q][e];
			if (query[q] != engine[e])
			{
				abc[q][e] = min_sw(q + 1, e);
				return abc[q][e];
			}
			int ans = 5000;
			for (int i = 0; i < engine.size(); i ++)
			{
				if (i == e)
					continue;
				ans = MIN(ans,min_sw(q,i));
			}
			if (ans == 5000)
			{
				abc[q][e] = 0;
				return 0;
			}
			abc[q][e] = 1 + ans;
			return abc[q][e];
		}
};

int main()
{
	ifstream fin("inp.in");
	ofstream fout("op.out");
	int n;
	char buffer [200];
	fin >> n;
	abcd univ;
	for (int i = 0; i < n; i++)
	{
		univ.engine.clear();
		univ.query.clear();
		int szeng,szquery;
		fin >> szeng;
		fin.getline(buffer,200);
		for (int j = 0; j < szeng; j ++)
		{
			fin.getline(buffer,200);
			univ.engine.push_back(buffer);
		}
		fin >> szquery;
		fin.getline(buffer,200);
		for (int k = 0; k < szquery; k++)
		{
			fin.getline(buffer,200);
			univ.query.push_back(buffer);
		}
		//Initialize array...
		for (int l = 0; l < szquery; l++)
			for (int m = 0; m < szeng; m++)
				univ.abc[l][m] = -1;
		int ans = 5000;
		for (int m = 0; m < szeng; m ++)
		{
			ans = MIN(ans,univ.min_sw(0,m));
		}
		fout<< "Case #" << i + 1<< ": " <<ans<<endl;
//		for (int i = 0; i < univ.engine.size(); i ++)
//			cout << univ.engine[i] << endl;
	}
	return 0;
}
