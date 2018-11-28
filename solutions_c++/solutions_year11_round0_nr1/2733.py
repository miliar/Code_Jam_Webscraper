#include <iostream>
#include <vector>
using namespace std;
int main(void){
	int t;
	cin >> t;
	for(int test_case = 1; test_case <= t; ++test_case){
		int N;
		cin >> N;
		int O_loc = 1, B_loc = 1;
		char color_order[N];
		vector<int> O_order;
		vector<int> B_order;
		for(int i = 0; i < N; ++i){
			cin >> color_order[i];
			int num;
			cin >> num;
			if(color_order[i] == 'O'){
				O_order.push_back(num);
			}else{
				B_order.push_back(num);
			}
		}
		int O_index = 0, B_index = 0;
		int time = 0;
		int button = 0;
		while(button < N){
			bool btn_pressed = false;
			if(O_index < O_order.size()){
				if(O_loc == O_order[O_index] and color_order[button] == 'O'){
					O_index++;
					btn_pressed = true;
				}else if(O_loc < O_order[O_index]){
					O_loc++;
				}else if(O_loc > O_order[O_index]){
					O_loc--;
				}
			}
			if(B_index < B_order.size()){
				if(B_loc == B_order[B_index] and color_order[button] == 'B'){
					B_index++;
					btn_pressed = true;
				}else if(B_loc < B_order[B_index]){
					B_loc++;
				}else if(B_loc > B_order[B_index]){
					B_loc--;
				}
			}
			if(btn_pressed){
				++button;
			}
			++time;
		}
		cout << "Case #" << test_case << ": " << time << endl;
	}
}
