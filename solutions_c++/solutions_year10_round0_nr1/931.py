#include <iostream>
using namespace std;

int main(){
	unsigned int t,test = 0;
	unsigned long long n,k;
	unsigned long long temp;
	bool on;
	cin >> t;
	while (test++<t){
		cin >> n >> k;
		cout << "Case #"<<test<<": ";
		temp = (1<<n) -1;
		on = (k & temp) == temp;
		if (on) cout << "ON";
		else cout << "OFF";
		
		if (test <t) cout << endl;
	}
}
