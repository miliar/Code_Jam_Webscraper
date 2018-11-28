#include <cstdio>
#include <sstream>
#include <vector>
#include <list>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <iostream>
#include <functional>
#include <cstdlib>
#include <stack>
#include <queue>
#include <string>
#include <climits>

#pragma once
using namespace std;

bool isNotComplete(char grid[][4]) 
{
	for(int i = 0; i<4; i++) 
	{
		for(int j = 0; j<4; j++) 
		{
			if(grid[i][j] == '.') 
			{
				return true;
			}
		}
	}

	return false;
}

bool win(char grid[][4], char value)
{
	bool flag = false;
	int vCount = 0;
	
	for(int i = 0; i<4; i++) 
	{
		vCount = 0;
		for(int j = 0; j<4; j++) 
		{
			if(grid[i][j] == value || grid[i][j] == 'T') 
			{
				vCount++;
			}
		}

		if(vCount == 4) 
		{
			return true;
		}
	}

	for(int j = 0; j < 4; j++) 
	{
		vCount = 0;
		for(int i = 0; i<4; i++) 
		{
			if(grid[i][j] == value || grid[i][j] == 'T') 
			{
				vCount++;
			}
		}

		if(vCount == 4) 
		{
			return true;
		}
	}

	vCount = 0;

	if(grid[0][0] == value || grid[0][0] == 'T') vCount++;
	if(grid[1][1] == value || grid[1][1] == 'T') vCount++;
	if(grid[2][2] == value || grid[2][2] == 'T') vCount++;
	if(grid[3][3] == value || grid[3][3] == 'T') vCount++;

	if(vCount == 4) 
	{
		return true;
	}
	
	vCount = 0;

	if(grid[0][3] == value || grid[0][3] == 'T') vCount++;
	if(grid[1][2] == value || grid[1][2] == 'T') vCount++;
	if(grid[2][1] == value || grid[2][1] == 'T') vCount++;
	if(grid[3][0] == value || grid[3][0] == 'T') vCount++;

	if(vCount == 4) 
	{
		return true;
	}

	return false;
}




void main()
{
	int T = 0;
	bool w = false;

	FILE* fp = fopen("Q1-small.txt", "r");

	freopen("Q1-large.txt","r",  stdin);
	freopen("Q1-output.txt", "w", stdout);
	cin>>T;

	for(int i = 1; i <= T; i++)
	{
		w = false;
		char grid[4][4];
	
		for(int r = 0; r < 4; r++)
		{
			for(int c = 0; c < 4; c++)
			{
				cin>>grid[r][c];
			}
		}

		w = win(grid, 'X');
		if(w)
		{
			cout<<"Case #"<<i<<": X won" <<endl;
			continue;
		}
	
		w = win(grid, 'O');
		if(w)
		{
			cout<<"Case #"<<i<<": O won"<<endl;
			continue;
		}

		w = isNotComplete(grid);
		if(w)
		{
			cout<<"Case #"<<i<<": Game has not completed"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": Draw"<<endl;
		}
	}
}