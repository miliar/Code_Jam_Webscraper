#include <iostream>
using namespace std;
int main(){
	int T, N, K;
	cin>>T;
	for(int i=1;i<=T;++i){
		cin>>N>>K;
		bool on=true;
		for(int i=0;i<N;++i){
			if(!(K&(1<<i))){
				on=false;
				break;
			}
		}
		if(on){
			cout<<"Case #"<<i<<": ON"<<endl;
		}else{
			cout<<"Case #"<<i<<": OFF"<<endl;
		}
	}
	return 0;
}