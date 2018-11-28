#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>

using namespace std;

int main(int argc, char** argv)
{
	int T, n;
	char matches[101][101];
	int games[100], wins[100];
	double wp[100], bowp[100][100], owp[100], oowp[100], sum, gamesd;
	char c, sbuf[1000];
	
	scanf("%d", &T);
	
	for(int i = 1; i <= T; i++)
	{
		scanf("%d", &n);
		
		memset(games, 0, sizeof(int) * 100);
		memset(wins, 0, sizeof(int) * 100);
		
		//read games
		
		for(int j = 0; j < n; j++) // team
		{
			scanf("%s", sbuf);
			for(int k = 0; k < n; k++) //opponent
			{
				c = sbuf[k];
				matches[j][k] = c;
				
				if(c == '1')
				{
					games[j]++;
					wins[j]++;
				}
				else if(c == '0')
					games[j]++;
			}
		}
		
		// calculates wp, owp, oowp
		
		for(int j = 0; j < n; j++) // team
		{
			wp[j] = (double)wins[j]/(double)games[j];
			for(int k = 0; k < n; k++)
			{
				if(j != k)
				{
					if(matches[j][k] == '1')
						bowp[j][k] = (double)(wins[j] - 1)/(double)(games[j] - 1);
					else if(matches[j][k] == '0')
						bowp[j][k] = (double)(wins[j])/(double)(games[j] - 1);
					else
						bowp[j][k] = (double)wins[j]/(double)games[j];
				}
			}
		}
		
		for(int j = 0; j < n; j++) // team
		{
			sum = gamesd = 0.0;
			for(int k = 0; k < n; k++)
			{
				if((k != j) && (matches[j][k] != '.'))
				{
					sum += bowp[k][j];
					gamesd++;
				}
			}
			owp[j] = sum/gamesd;
		}
		
		for(int j = 0; j < n; j++) // team
		{
			sum = gamesd = 0;
			for(int k = 0; k < n; k++)
			{
				if((k != j) && (matches[j][k] != '.'))
				{
					sum += owp[k];
					gamesd++;
				}
			}
			oowp[j] = sum/gamesd;
		}
		
		printf("Case #%d:\n", i);
		for(int j = 0; j < n; j++) // team
		{
			printf("%.12lf\n", 0.25 * wp[j] + 0.50 * owp[j] + 0.25 * oowp[j]);
		}
	}
	
	return 0;
}
