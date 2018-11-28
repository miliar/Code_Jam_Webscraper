#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>
#include <limits.h>

using namespace std;

bool occupied[10001];
int P, Q;

int main(int argc, char *argv[])
{
	int N;
	cin >> N;
	for (int n = 1; n <= N; n++)
	{
		cin >> P >> Q;
		
		vector<int> cells;
		
		for (int i = 0; i < Q; i++)
		{
			int x;
			cin >> x;
			cells.push_back(x);
		}
		
		int total = 0;
		int best = INT_MAX;
		do
		{
			/*for (int i = 0; i < cells.size(); i++)
				cout << "cells[" << i << "] = " << cells[i] << endl;*/
			for (int i = 0; i < 10001; i++)
			{
				occupied[i] = true;
			}
			total = 0;
			for (int i = 0; i < cells.size(); i++)
			{
				occupied[cells[i]] = false;
				int tally = 0;
				int j = cells[i] - 1;
				while (j >= 1 && occupied[j] == true)
				{
					tally++;
					j--;
				}
				j = cells[i] + 1;
				while (j <= P && occupied[j] == true)
				{
					tally++;
					j++;
				}
				total += tally;
			}
			//cout << "Got total " << total << endl;
			if (total < best)
				best = total;
			//cout << "Best is " << best << endl;
		} while (next_permutation(cells.begin(), cells.end()) != 0);
		
		cout << "Case #" << n << ": " << best << endl;
		
	}
	
	return 0;
}

