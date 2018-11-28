#include<iostream>

using namespace std;

int main(){
	int cas;
	cin>>cas;
	int can[10000];
	
	for(int ca=1; ca<=cas; ++ca){
		int n;
		int allx=0;
		int min = 1<<30;
		int sum =0;
		cin>>n;
		for(int i=0; i<n; ++i){
			cin>>can[i];
			allx ^= can[i];
			min = min<can[i]?min:can[i];
			sum += can[i];
		}
		if(allx!=0){
			cout<<"Case #"<<ca<<": NO"<<endl;
			continue;
		} 
		else 
		cout<<"Case #"<<ca<<": "<<sum-min<<endl;
	}
}