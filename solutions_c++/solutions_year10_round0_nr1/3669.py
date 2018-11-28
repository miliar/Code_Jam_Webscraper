#include<iostream>
using namespace std;
int main(){
	long long int n;
	long long int k;
	int cases,i=0;
	cin >> cases;
	while( i++<cases ){
		cin >> n >> k;
		cout << "Case #"<<i<<": ";
		(1+k)%(1<< (n) )  ? cout<< "OFF": cout<< "ON";
		cout  << endl;
	}

	return 0;
}
