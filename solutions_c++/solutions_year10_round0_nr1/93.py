//Marcin Baran

#include<iostream>
#include<sstream>
#include<vector>
#include<cmath>
#include<list>
#include<algorithm>

using namespace std;
typedef long long int lli;
lli z,N,K;

int main(){
	cin>>z;
	for(int ii=1;ii<=z;++ii){
		cin>>N>>K;
		int potrzeba = (1<<N);
		cout<<"Case #"<<ii<<": ";
		if(potrzeba - 1 > K){
			cout<<"OFF"<<endl;
			continue;
		}
		K = K - potrzeba + 1;
		if(K % potrzeba == 0){
			cout<<"ON"<<endl;
		}
		else cout<<"OFF"<<endl;
	}
	return 0;
}
