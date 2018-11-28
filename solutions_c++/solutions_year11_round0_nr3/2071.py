#include<iostream>

using namespace std;

int main(){
	int tn;cin>>tn;
	for(int iii=0;iii<tn;iii++){
		int n;cin>>n;
		int mi=100000000;
		int total=0;
		int bittotal=0;
		for(int i=0;i<n;i++){
			int tmp;cin>>tmp;
			mi=min(mi,tmp);
			total+=tmp;
			bittotal^=tmp;
		}
		cout<<"Case #"<<(iii+1)<<": ";
		if(bittotal!=0){
			cout<<"NO"<<endl;
		}else{
			cout<<(total-mi)<<endl;
		}
	}
}
