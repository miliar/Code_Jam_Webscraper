#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

int main(){

	long long cases;
	ifstream infile;
	ofstream outfile;
	infile.open ("C:\\codejam\\A-large.in");
	outfile.open ("C:\\codejam\\A-large.out");

	infile>>cases;

	long long tot;
	long long o_pos;
	long long b_pos;
	long long run_tot;
	long long cnt;
	char last_state;
	char state;
	long long button;

	for (int c = 0; c < cases; c++){
		infile>>cnt;

		tot = 0;
		o_pos = 1;
		b_pos = 1;
		run_tot = 0;

		infile>>state;
		infile>>button;

		if (state == 'O'){
			run_tot += abs(button - o_pos) + 1;
			o_pos = button;
		}
		else {
			run_tot += abs(button - b_pos) + 1;
			b_pos = button;
		}

		last_state = state;

		for(int i = 0; i < (cnt-1); i++){

			infile>>state;
			infile>>button;

			if (last_state != state){
				if (state == 'B'){
					if (run_tot >= abs(button-b_pos)){
						tot+=run_tot;
						run_tot = 1;
					}
					else{
						tot+=run_tot;
						run_tot = abs(abs(button-b_pos)-run_tot) + 1;
					}
					b_pos = button;
				}
				else {
					if (run_tot >= abs(button-o_pos)){
						tot+=run_tot;
						run_tot = 1;
					}
					else {
						tot+=run_tot;
						run_tot = abs(abs(button-o_pos)-run_tot) + 1;
					}
					o_pos = button;
				}
			}
			else{
				if (state == 'B'){
					run_tot += abs(button-b_pos) + 1;
					b_pos = button;
				}
				else {
					run_tot += abs(button-o_pos) + 1;
					o_pos = button;
				}
				
			}

			last_state = state;
		}

		tot+=run_tot;
		outfile<<"Case #"<<c+1<<": "<<tot<<endl;

	}

	return 0;
}