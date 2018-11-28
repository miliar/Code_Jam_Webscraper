#include <iostream>
#include <fstream>
#include <queue>
#include <map>

using namespace std;

const int MAX_T = 100;
const int MAX_N = 1000;

int max_val;
int T, N;
int C[MAX_N];

typedef pair<int, int> state;

void solve(state sbit, state sint, int depth)
{
	if(depth == N)
	{
		if(sbit.first == sbit.second && sint.first != 0 && sint.second != 0)
		{
			if(max_val < sint.first)
			{
				max_val = sint.first;
			}
		}

		return;
	}

	solve(state((sbit.first^C[depth]), sbit.second), state(sint.first+C[depth], sint.second), depth+1);
	solve(state(sbit.first, (sbit.second^C[depth])), state(sint.first, sint.second+C[depth]), depth+1);
}

int main()
{
	ifstream ifs("input.txt", ios::in);
	ofstream ofs("output.txt", ios::out);

	ifs >> T;
	for(int t=0; t<T; t++)
	{
		ifs >> N;
		for(int n=0; n<N; n++)
		{
			ifs >> C[n];
		}

		max_val = -1;
		solve(state(0, 0), state(0, 0), 0);

		if(max_val != -1)
		{
			ofs << "Case #" << t+1 << ": " << max_val << endl;
		}
		else
		{
			ofs << "Case #" << t+1 << ": NO" << endl;
		}	
	}
}

