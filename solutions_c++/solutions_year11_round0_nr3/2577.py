#include <iostream>
#include <vector>
using namespace std;
int main(){
	int t ;
	cin >> t;
	for(int i_t = 0; i_t < t; i_t++){
		vector <int> candys;
		int candy_num = 0;
		cin >> candy_num;
		int candy_value;
		cin >> candy_value;
		long long int sum = candy_value;
		int xor_sum = candy_value;
		candys.push_back(candy_value);
		for(int i = 1; i < candy_num; i++){
			cin >> candy_value;
			sum += candy_value;
			xor_sum = xor_sum^candy_value; 
			candys.push_back(candy_value);
		}
		int my_min = 9999999;
		for(int i = 0; i < candy_num; i++){
			int split = xor_sum ^ candys[i];
			if(split == candys[i] && candys[i] < my_min) {
				my_min = candys[i];
				//cout << my_min << endl;
			}
		}
		cout << "Case #"<< i_t+1 <<": ";
		if(my_min == 9999999){
			cout << "NO" << endl;
		}
		else cout << (sum - my_min) << endl;
 	}
}