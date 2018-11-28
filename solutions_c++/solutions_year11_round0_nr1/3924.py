#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	int T;

	cin >> T;

	for(int i=0; i<T; i++)
	{
		int N;
		char curr_char;
		int curr_button;
		int curr_index;
		int state[2] = {1, 1};
		int steps[2] = {0, 0};

		cin >> N;

		for(int j =0; j <N; j++)
		{
			cin >> curr_char;
			cin >> curr_button;
			
			curr_index = (curr_char == 'O')?0:1;
			int num_steps = abs(state[curr_index] - curr_button) + 1 ;
			
			steps[curr_index] += num_steps;
			state[curr_index] = curr_button;

			if (steps[curr_index]<steps[(curr_index+1)%2]+1) {
				steps[curr_index] = steps[(curr_index+1)%2] + 1;
			}
			
		}
		cout <<"Case #" << i+1  << ": " << steps[curr_index] << endl;


	}
}