/*
 * main.cpp
 *
 *  Created on: 2011/5/7
 *      Author: lauer
 */
#include<iostream>
#include<fstream>
#include<iomanip>
#include<cmath>
using namespace std;

int rob[2][1000];

int main()
{
	ofstream fout("ans");
	int t;
	int n,k,s,r,a;
	int turn,in_time;
	int ro1,ro2,ans;
	char w;
	cin >> t;
	for(int i=1;i<=t;i++)
	{
		cin >> n;
		ans = 0;
		for(int j=0;j<n;j++)
			rob[0][j] = rob[1][j] = 0;
		for(int j=0;j<n;j++)
		{
			cin >> w >> s;
			if(w=='O')
				rob[0][j] = s;
			else
				rob[1][j] = s;
		}
		ro1 = ro2 = 1;
		turn = -1;
		in_time = 0;
		for(int j=0;j<n;j++)
		{
			if(rob[0][j]!=0)
			{
				if(turn != 0)
				{
					ans += in_time;
					turn = 0;
					if(abs(rob[0][j]-ro1) > in_time)
					{
						in_time = abs(rob[0][j]-ro1)-in_time+1;
					}
					else
						in_time = 1;
					ro1 = rob[0][j];
				}
				else
				{
					in_time += abs(rob[0][j]-ro1)+1;
					ro1 = rob[0][j];
				}
			}
			else
			{
				if(turn != 1)
				{
					ans += in_time;
					turn = 1;
					if(abs(rob[1][j]-ro2) > in_time)
					{
						in_time = abs(rob[1][j]-ro2)-in_time+1;
					}
					else
						in_time = 1;
					ro2 = rob[1][j];
				}
				else
				{
					in_time += abs(rob[1][j]-ro2)+1;
					ro2 = rob[1][j];
				}
			}
		}
		ans += in_time;
		/*if(r!=0)
			fout << "Case #" << i << ": NO" << endl;
		else*/
		fout << "Case #" << i << ": " << ans << endl;
	}
}
