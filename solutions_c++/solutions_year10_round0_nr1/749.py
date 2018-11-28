#include<iostream>
using namespace std;

int main(){
	int ncases; cin>>ncases;
	for (int ncase=1;ncase<=ncases;++ncase){
		int n,k; cin>>n>>k;
		int m=1<<n;
		cout<<"Case #"<<ncase<<": "<<(1+k%m==m?"ON":"OFF")<<endl;
	}
 	return 0;
}

