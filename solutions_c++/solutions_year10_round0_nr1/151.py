#include <iostream>

using namespace std;

int main(){
	//freopen("result.out","w",stdout);
	int n,k,cn;
	cin>>cn;
	for(int i=1;i<=cn;i++){
		cin>>n>>k;
		if((k+1)%(1<<n)==0){
			cout<<"Case #"<<i<<": ON"<<endl;
		}
		else{
			cout<<"Case #"<<i<<": OFF"<<endl;
		}
	}
	return 0;
}