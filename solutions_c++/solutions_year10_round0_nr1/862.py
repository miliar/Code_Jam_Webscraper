#include<iostream>
using namespace std;

int n, k, t;

int main(){
	cin >> t;
	for(int i=0; i<t;i++){
		cin >> n >> k; 
		k %= (1<<n);
		cout << "Case #" << (i+1) << ": ";
		if( k == ((1<<n) - 1) )
			cout << "ON" << endl;
		else
			cout << "OFF" << endl;
	}
}
