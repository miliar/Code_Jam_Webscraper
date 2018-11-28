#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <deque>
#include <strstream>
#include <cmath>
#include <bitset>

using namespace std;

struct Like
{
	int index;
	int flag;
};

int main()
{
	int casenum;
	ifstream fin("B-small.in");
	ofstream fout("B-small.out");
	fin >> casenum;
	vector<Like> rec[100];
	bitset<10> bs;
	for(int ind = 1; ind <= casenum; ind++)
	{
		int N;
		fin >> N;
		int M;
		fin >> M;
		for(int i = 0; i < 100; i++)
			rec[i].resize(0);
		for(int i = 0; i < M; i++)
		{
			int num;
			fin >> num;
			for(int j = 0; j < num; j++)
			{
				Like tmpLk;
				fin >> tmpLk.index >> tmpLk.flag;
				rec[i].push_back(tmpLk);
			}
		}
		int up = (int)pow(2.0,(double)N);
		int res(-1),mininum(1000);
		for(int i = 0; i < up; i++)
		{
			bs = i;
			bool flags = true;
			for(int j = 0; j < M; j++)
			{
				int k;
				for(k = 0; k < rec[j].size(); k++)
					if(bs[rec[j][k].index-1] == rec[j][k].flag)
						break;
				if(k == rec[j].size())
				{
					flags = false;
					break;
				}
			}
			if(!flags) continue;
			if(bs.count() < mininum)
			{
				mininum = bs.count();
				res = i;
			}
		}
		fout << "Case #" << ind << ": ";
		if(res == -1)
			fout << "IMPOSSIBLE" << endl;
		else
		{
			bs = res;
			for(int i = 0; i < N; i++)
			{
				fout <<bs[i];
				if(i != N-1)
					fout << ' ';
			}
			fout << endl;
		}
	}
	return 1;
}

