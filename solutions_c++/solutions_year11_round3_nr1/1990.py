#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
#include <utility>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>

using namespace std;

int T,C,R;
char pic[52][52];
char ans[52][52];

bool check()
{
	int C_count = 0,R_count = 0;
	
	for(int i =1;i <= R;i ++)
		{
		R_count = 0;
		for(int j = 1;j <= C; j++)
			if(pic[i][j]=='#')
				{
				if(j>1 && j < R && pic[i][j-1]=='.' && pic[i][j+1]=='.')
						return false;
						
				if(j==1&& j < R && pic[i][j+1]=='.')
						return false;
				
				if(j==R && j>1 && pic[i][j-1]=='.')
						return false;
				
				R_count++;
				}
				
				
		if(R_count%2 == 1)
			return false;
		else continue;
		}
	
	for(int j =1;j <= C;j ++)
		{
		C_count = 0;
		for(int i = 1;i <= R; i++)
			if(pic[i][j]=='#')
				{
				if(i>1 && i < R && pic[i-1][j]=='.'&&pic[i+1][j]=='.')
						return false;
				if(i==1 && i < R &&pic[i+1][j]=='.')
						return false;
				if(i>1 && i == R && pic[i-1][j]=='.')
						return false;
				C_count++;
				}
		if(C_count%2 == 1)
			return false;
		else continue;
		}
	return true;
}


int main()
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	fin>>T;
	
	int i = 1;
	for(i = 1;i <= T;i++)
	{	
		fin>>R>>C;
		bool flag = false;
		for(int j =1; j <= R; j++)
			for(int k = 1;k <= C;k++)
				{fin>>pic[j][k];
				ans[j][k] = pic[j][k];
				}
		flag = check();
		fout<<"Case #"<<i<<":"<<endl;
	
		if(!flag)
			fout<<"Impossible"<<endl;
		else
			{
			for(int j =1; j <= R; j++)
				{for(int k = 1;k <= C;k++)
					{
					if(ans[j][k]=='#')
						{	
						ans[j][k]='/';
						ans[j][k+1]='\\';
						ans[j+1][k]='\\';
						ans[j+1][k+1]='/';
						}
						
					fout<<ans[j][k];
					}
				
				fout<<endl;
				}
					
			}
	}
	return 0;
}











