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
#include <cstdio>

using namespace std;

int dx[] = {0,1,1,1};
int dy[] = {1,-1,0,1};

bool G[105][105];

int main()
{	
	ofstream fout("C-small0.out");
 	ifstream fin("C-small-attempt0.in");
//	ifstream fin("C-test.in");
	
		
	int T;
	fin >> T;
	
	for(int t = 0; t < T; t++)
	{
		memset(G,0,sizeof G);
		
		int R;
		fin >> R;
		for(int p = 0; p < R; p++)
		{
			int x1,y1,x2,y2;
			fin >> x1 >> y1 >> x2 >> y2;
			for(int t = x1; t <= x2; t++)
			for(int u = y1; u <= y2; u++)
				G[t][u] = 1;
		}
		
		int cnt = 0;
		
		while(1)
		{
			
			int done = 1;
			for(int i = 0; i < 105; i++) if(done)
			for(int j = 0; j < 105; j++)
				if(G[i][j])
				{
					done = 0;
					break;
				}
			
			if(done == 1) break;
			
			for(int i = 0; i < 7; i++)
			{
				for(int j = 0; j < 7; j++)
					cout << G[i][j];
				cout << endl;
			}
			cout << endl;
			
			cnt++;
			for(int i = 104; i >= 0; i--)
			for(int j = 104; j >= 0; j--)
			{
				if(G[i][j] == 1)
				{
					if(i >= 1 && j >= 1 && G[i-1][j] == 0 && G[i][j-1] == 0)
						G[i][j] = 0;
				}
				else if(G[i][j] == 0)
				{
					if(i >= 1 && j >= 1 && G[i-1][j] == 1 && G[i][j-1] == 1)
						G[i][j] = 1;
				}
			}
			
			done = 1;
			for(int i = 0; i < 105; i++) if(done)
			for(int j = 0; j < 105; j++)
				if(G[i][j])
				{
					done = 0;
					break;
				}
			
			if(done == 1) break;
		}
		
		cout << cnt << endl;
		fout << "Case #" << t+1 << ": " << cnt << endl;
	}
	
	return 0;
}