#include <iostream>
#include<string>
#include<iostream> 
#include<algorithm>
#include<queue>
#include<stack>
#include<numeric>
#include<vector>
#include<set>
#include<sstream>
#include<cstring>
#include<string>
#include<stdio.h>
#include<cmath>
#include<cstdlib>
#include<map>
using namespace std;

int checker[3][40];
void makeChecker()
{
	int i, j, k, diff, tt, mm, nn,sum;
	vector<int> temp;
	for(i=0;i<=10;i++)
	{
		for(j=0;j<=10;j++)
		{
			for(k=0;k<=10;k++)
			{
				temp.push_back(i);
				temp.push_back(j);
				temp.push_back(k);
				mm = *max_element(temp.begin(), temp.end());
				nn = *min_element(temp.begin(), temp.end());
				diff = mm - nn;
				sum = i+j+k;
				if(diff == 1 || diff == 0)
				{
					if(checker[0][sum] < mm)
						checker[0][sum] = mm;
				}
				else if(diff == 2)
				{
					if(checker[1][sum] < mm)
						checker[1][sum] = mm;
				}
				temp.clear();
			}
		}
	}
}
int main()
{
	int test;

	int i;
	int sur, noSur, comSur, totalSur;
	freopen("d:\\B-large.in", "r", stdin);
	freopen("d:\\outlarge.txt", "w", stdout);
	makeChecker();
	cin >> test;
	int output;
	int S, K, N, temp;
	for(int t = 1;t<=test;t++)
	{
		output = 0;
		cout << "Case #"<< t<<": ";
		sur = noSur = comSur = 0;

		cin >> N >> S >> K;
		;
		for(i=1;i<=N;i++)
		{
			cin >> temp;
			if(checker[0][temp] >= K && checker[1][temp] >= K)
			{
				output++;
				comSur++;
				continue;
			}
			else if(checker[0][temp] >= K && checker[1][temp] < K)
			{
				output++;
				comSur++;
				continue;
			}
			else if(checker[0][temp] < K && checker[1][temp] >= K)
			{
				if(S>0)
				{	S--;
					output++;
				}
				comSur++;
				continue;
			}
		}
		cout << output << endl;



	}
	return 0;
}