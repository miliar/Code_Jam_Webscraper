#include <iostream>
#include <vector>
using namespace std;

int main(void){
	int T;
	cin >> T;
	for(int test_case = 1; test_case <= T; ++test_case){
		int N, equal(0), minimum(0), total(0);
		cin >> N;
		for(int i = 0; i < N; ++i){
			int number;
			cin >> number;
			equal = equal xor number;
			if(minimum == 0 or minimum > number){
				minimum = number;
			}
			total += number;
		}
		if(equal != 0){
			cout << "Case #" << test_case << ": NO" << endl;
		}else{
			
			cout << "Case #" << test_case << ": " << total - minimum << endl;
		}
	}
}
