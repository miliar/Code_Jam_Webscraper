#include <iostream>
using namespace std;
int main(){
	int t,n,k;
	cin >> t;
	for(int z=1;z<=t;z++){
		cin >> n >> k;
		if(k%( 1<<n )==(1<<n)-1)
			cout << "Case #"<<z<<": ON"<<endl;
		else	
			cout << "Case #"<<z<<": OFF"<<endl;
	}
}
