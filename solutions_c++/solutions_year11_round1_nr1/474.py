#include <iostream>
using namespace std;

int gcd (int a , int b){
	if (a == b) return a;
	else if (a > b) return gcd (b, a-b);
	else return gcd (a, b-a);
}

int main()
{
	int cases; cin >>cases;
	int pd,pg;
	long long n;
	for(int i = 0 ; i < cases; i++){
		cin >> n >> pd >> pg;
		if (pg == 100){
			if (pd == 100){
				cout << "Case #" << i+1<< ": "<< "Possible" <<endl; continue;
			}
			else{
				cout << "Case #" << i+1<< ": "<< "Broken" <<endl; continue;
			}
		}
		if (pg == 0){
			if (pd == 0){
				cout << "Case #" << i+1<< ": "<< "Possible" <<endl; continue;
			}
			else{
				cout << "Case #" << i+1<< ": "<< "Broken" <<endl; continue;
			}
		}
		else{
			long long min = (long long)(100 / gcd (100, pd));
			if (min > n) {
				cout << "Case #" << i+1<< ": "<< "Broken" <<endl; continue;
			}
			else{
				cout << "Case #" << i+1<< ": "<< "Possible" <<endl; continue;
			}
		}
	}
}
