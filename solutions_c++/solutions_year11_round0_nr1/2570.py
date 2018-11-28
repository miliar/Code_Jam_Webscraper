#include <iostream>
using namespace std;
#include <math.h>
int main(){
	int Times;
	int n_input;
	cin >> Times;
	for(int i_t = 0 ; i_t < Times; i_t++){
		cin >> n_input;
		int o_count = 0;
		int b_count = 0;
		int t_count = 0;
		int location = 0;
		int o_last_location = 1;
		int b_last_location = 1;
		int step = 0;
		char rob = ' ';
		char last_command = ' ';
		for(int i = 0; i < n_input;i++){
			//cout << t_count << endl;
			cin >> rob >> location;
			if(rob == 'O'){
				step = abs(location - o_last_location);
				o_last_location = location;
				if(rob==last_command){
					o_count += step+1;
					t_count += step+1;
				}
				else{
					if(step > b_count){
						o_count += step - b_count +1;
						t_count += step - b_count +1;
					}
					else {
						o_count  = 1;
						t_count += 1;
					}
					b_count  = 0;
				}
			}
			if(rob == 'B'){
				step = abs(location - b_last_location);
				b_last_location = location;
				if(rob==last_command){
					b_count += step+1;
					t_count += step+1;
				}
				else {
					
					if(step > o_count){
						b_count += step - o_count+1;
						t_count += step - o_count+1;
					}
					else {
						b_count  = 1;
						t_count += 1;
					}
					o_count = 0;
				}
			}
			last_command = rob;
		}
		//cout << "Case #"<<i_t+1<<": "<<t_count<<endl;
		cout << "Case #"<<i_t+1<<": "<<t_count<<endl;
	}
}