#include<iostream>
using namespace std;
int main (){
	int tc = 0;
	int n , k;
	cin >>tc;
	for ( int caseno = 1 ;caseno <= tc ; caseno++ ){
		bool res = true ;
		cin >>n>> k;
		cout << "Case #" << caseno << ": " ;
		if ( (k&((1<<n)-1)) == ((1<<n)-1) )
			cout << "ON" << endl;
		else cout << "OFF" << endl;
	}
}
