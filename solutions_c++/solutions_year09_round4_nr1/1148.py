#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int vals[50];
int N = 0;

bool valid()
{
	bool valid = true;
	for (int i = 0; i < N; i++)
	{
		if (vals[i] > i+1)
			valid = false;
	}
	return valid;
}

int main(int argc, char *argv[])
{
	int C;
	cin >> C;
	for (int c = 1; c <= C; c++)
	{
		cin >> N;
		for (int n = 0; n < N; n++)
		{
			string row;
			cin >> row;
			int lastpos = -1;
			for (int x = 0; x < N; x++)
			{
				if (row[x] == '1')
					lastpos = x;
			}
			vals[n] = lastpos + 1; 
		}
		
		/*for (int n = 0; n < N; n++)
		{
			cout << "Val: " << vals[n] << endl;
		}*/
		
		/*cout << "Valid is: " << valid() << endl;*/
		
		int moves = 0;
		
		while (!valid())
		{
			bool problem = false;
			int problevel = 0;
			for (int i = 0; i <= N-2; i++)
			{
				if (vals[i] > (i+1) && !problem)
				{
					problem = true;
					problevel = i;
				}
				if ((vals[i] > vals[i+1]) && (vals[i+1] <= (i+1)) && problem && (vals[i+1] <= (problevel+1)))
				{
					int temp = vals[i];
					vals[i] = vals[i+1];
					vals[i+1] = temp;
					moves++;
					break;
				}
			}
		}
		
		cout << "Case #" << c << ": " << moves << endl;
		
	}
	
	return 0;
}

