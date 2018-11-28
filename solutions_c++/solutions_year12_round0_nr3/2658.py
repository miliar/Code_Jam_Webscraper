#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i = 1; i <= t;i++){
		int a,b;
		cin >> a >> b;
		int _a = a;
		int k = 10000000;
		while(k > a) k /= 10;
		int s = 0;
		while(_a < b){
			_a = _a/k+(_a%k)*10;
			while(_a != a){
				if(_a <= b && a < _a) s++;
				_a = _a/k+(_a%k)*10;
			}
			a++;
			_a++;
		}
		cout << "Case #"<<i<<": "<<s<<endl;
	}
}
