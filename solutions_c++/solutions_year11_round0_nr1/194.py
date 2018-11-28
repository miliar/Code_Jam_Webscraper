#include <iostream>
#include <fstream>
#include <stdint.h>

using namespace std;
inline int abs(int a, int b){
	if(a > b)
		return a-b;
	return b-a;
}

int button_solve ( int n, char *r, int *b ) {
	int time = 0, Blue = 1, Orange = 1;
	int Blue_task = n , Orange_task = n ;
	for (int i = 0; i < n; i++)
		if(r[i] == 'B') {
			Blue_task = i;
			break;
		}

	for (int i = 0; i < n; i++)
		if(r[i] == 'O') {
			Orange_task = i;
			break;
		}
	
	for (int task = 0; task < n; task++) {
		if( r[task] == 'B' ) {
			int pass = abs(b[task] , Blue) + 1;

			if ( Orange_task != n ) {
				if( abs(Orange, b[Orange_task]) <= pass )
					Orange = b[Orange_task];
				else {
					if( Orange < b[Orange_task])
						Orange += pass;
					else
						Orange -= pass;
				}
			}
			Blue = b[task];
			time += pass;
			for ( Blue_task++; Blue_task < n; Blue_task++)
				if(r[Blue_task] == 'B')
					break;
		}
		else {
			int pass = abs(b[task], Orange) + 1;

			if( Blue_task != n ) {
				if( abs(Blue, b[Blue_task]) <= pass )
					Blue = b[Blue_task];
				else{
					if( Blue < b[Blue_task] )
						Blue += pass;
					else
						Blue -= pass;
				}
			}

			Orange = b[task];
			time += pass;
			for ( Orange_task++; Orange_task < n; Orange_task++)
				if(r[Orange_task] =='O')
					break;
		
		}
	}
	return time;

}

int main(int argc , char * argv[]){
	if (argc < 2)
		cout << "Enter input";
	
	ifstream input(argv[1]);

	int problem_count;
	input >> problem_count;

	for (int p = 1; p <= problem_count; p++) {
		int button_count;
		input >> button_count;
		char * robot = new char[button_count];
		int * button = new int[button_count];

		for (int i = 0; i < button_count; i++)
			input >> robot[i] >> button[i];


		cout << "Case #" << p << ": " << button_solve(button_count, robot, button) << endl;

		delete [] robot;
		delete [] button;
	}
	input.close();
	return 0;
}



