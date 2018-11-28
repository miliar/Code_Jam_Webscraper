#include <iostream>

using namespace std;

int main(){
	int i=0, n, int_num, sum, buf;
	cin >> n;
	while(++i<=n){
		cin >> int_num;
		int it = 0;
		sum = 0;
		while(++it<=int_num){
			cin >> buf;
			if(buf != it){
				sum++;
			}
		}
		cout << "Case #" << i << ": " << sum << ".000000" << endl;
	}
	return 0;
}