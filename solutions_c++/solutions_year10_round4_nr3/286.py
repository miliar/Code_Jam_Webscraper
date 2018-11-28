#include <vector>
#include <string>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <sstream>
#include <map>
#include <ctime>
#include <cassert>

using namespace std;

ofstream fout("../../output.txt");
ifstream fin("../../input.txt");

bool nowgrid[101][101][2];

int main(void)
{
	int ttt;
	fin >> ttt;
	int ct = 0;
	string s;
	
	while(ttt>0)
	{
		ct++;
		ttt--;
		int n,i,j,k;
		int r;
		memset(nowgrid,0,sizeof(nowgrid));
		fin >> r;
		int x1,x2,y1,y2;
		for(i=0; i<r; i++)
		{
			fin >> x1 >> y1 >> x2 >> y2;
			for(j=x1; j<=x2; j++)
			{
				for(k=y1; k<=y2; k++)
				{
					nowgrid[j][k][0]=true;
				}
			}
		}
		int ans = 0;
		
		int isok = 1;
		int curr = 0;
		
		while(isok>0)
		{
			isok=0;
			int next = 1-curr;
			for(i=1; i<=100; i++)
			{
				for(j=1; j<=100; j++)
				{
					nowgrid[i][j][next]=false;
					if(nowgrid[i-1][j][curr] && nowgrid[i][j-1][curr])
					{
						nowgrid[i][j][next]=true;
					}
					if(nowgrid[i][j][curr] && (nowgrid[i-1][j][curr] || nowgrid[i][j-1][curr]))
					{
						nowgrid[i][j][next]=true;
					}
					if(nowgrid[i][j][next])
						isok++;
				}
			}
			ans++;
			curr=next;
		}
						
		
		
		cout << "Case #" << ct << ":" << " " << ans << endl;
		fout << "Case #" << ct << ":" << " " << ans << endl;
		
	}
	
	
	return 0;
}

