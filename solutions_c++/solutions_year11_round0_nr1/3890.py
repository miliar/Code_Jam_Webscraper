#include <iostream>

using namespace std;

#define SIGN(X) ( ((X) < 0) ? -1 : 1 )

void readCase(int *seq, int N)
{
	char c; int n;
	for (int i = 0; i<N; i++)
	{
		cin >> c >> n;
		seq[i] = (c == 'O' ? -1 : 1) * n;
	}
}

int target(int *seq, int N, int index, int turn)
{
	for (int i = index; i < N; i++)	
		if ( SIGN(seq[i]) == turn )
			return abs(seq[i]);
	return 0;
}

int main(int argc, char *argv[])
{
	int T = 0;
	cin >> T;

	for (int Case = 1; Case <= T; Case++)
	{
		int N = 0;
		cin >> N;
		int *seq = new int[N];

		readCase(seq, N);
				
		int result = 0;		
		int _pos[] = {1, 0, 1}; 
		int *pos = &_pos[1];		
		for (int i = 0; i<N; i++)
		{						
			int turn = SIGN(seq[i]);
			int moves = abs(abs(seq[i]) - pos[turn]) + 1;
			result += moves;
			pos[turn] = abs(seq[i]);

			int tar = target(seq, N, i, -turn);
			if (tar != 0)
			{
				int dir = SIGN( tar - pos[-turn] );
				int dist = abs( tar - pos[-turn] );
				pos[-turn] = dist > moves ? pos[-turn] + dir * moves : tar;					
			}			
		}		

		cout << "Case #" << Case << ": " << result << endl;

		delete [] seq;
	}

	return 0;
}