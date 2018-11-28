#include <iostream>
#include <sstream>
#include <cstring>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <map>
#include <deque>
#include <set>
#include <algorithm>
#include <stdio.h>

using namespace std;

int dx[] = {0,1,1,1};
int dy[] = {1,-1,0,1};

int main()
{	
	ofstream fout("A-large.out");
	
	ifstream fin("A-large.in");
		
	int T;
	fin >> T;
	
	for(int t = 0; t < T; t++)
	{
		int N,K;
		fin >> N >> K;
		vector<string> V;
		
		for(int j = 0; j < N; j++)
		{
			string s;
			for(int k = 0; k < N; k++)
			{
				char c;
				fin >> c;
				if(c == 'R' || c == 'B')
					s += c;
			}
			reverse(s.begin(),s.end());
			V.push_back(s);
		}
		
		bool red = 0;
		bool blue = 0;
		for(int i = 0; i < N; i++)
		for(int j = 0; j < V[i].size(); j++)
		{
			for(int p = 0; p < 4; p++)
			{
				int x = i, y = j;
				
				bool isred = 1, isblue = 1;
				for(int u = 0; u < K; u++)
					if(x < 0 || x >= V.size() || y < 0 || y >= V[x].size())
					{
						isred = 0, isblue = 0;
						break;
					}
					else
					{
						if(V[x][y] == 'R') isblue = 0;
						if(V[x][y] == 'B') isred = 0;
						x += dx[p], y += dy[p];
					}
				if(isred) red = 1;
				if(isblue) blue = 1;
			}
		}
		
		fout << "Case #" << t+1 << ": ";
		if(red && blue) fout << "Both\n";
		else if(red) fout << "Red\n";
		else if(blue) fout << "Blue\n";
		else fout << "Neither\n";
	}
	
	return 0;
}