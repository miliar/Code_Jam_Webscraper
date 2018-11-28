#include <iostream>

using namespace std;

int main(){
	
	int cases;
	cin >> cases;
	
	
	for(int T=1;T<=cases;T++){
		int turns;

		char who = NULL;
		char old_who;



		int current;
		int aim = 1;
		int time_sum = 0;
		int press_time = 0;
		int reach_time;
		int walk_time = 0;

		int other_current = 1;
		int temp_current;

		cin >> turns;

		for(int i=0;i<turns;i++){
			old_who = who;
			cin >> who;


			if(old_who == who){			
				current = aim;
				cin >> aim;
				reach_time = abs(aim-current);
				time_sum = time_sum + reach_time + 1;
				walk_time = walk_time + reach_time + 1;
				
				
				
			}
			else{
				current = aim;
				temp_current = current;
				current = other_current;
				other_current = temp_current;
				
				cin >> aim;
				reach_time = abs(aim-current);


				if(walk_time >= reach_time){
					time_sum = time_sum + 1;
					walk_time = 1;
				}
				else{
					time_sum = time_sum + (reach_time-walk_time) + 1;
					walk_time = (reach_time-walk_time) + 1;
				}
				
				
			}

		}



		cout << "Case #" << T << ": " << time_sum << endl;
	}
	

	
	
	return 1;
	
	
}

// Input 
//  	
// Output 
//  
// 3
// 4 O 2 B 1 B 2 O 4
// 3 O 5 O 8 B 100
// 2 B 2 B 1
// Case #1: 6
// Case #2: 100
// Case #3: 4
// 
