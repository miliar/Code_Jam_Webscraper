#include<iostream>
#include<vector>
using namespace std;

void print(vector<int>& a){
	for(int i=0;i<a.size();i++) cout<<a[i]<<" ";
	cout<<endl;
}
int main(){
	int N,K,T;
	cin>>T;
	for(int kase=1;kase<=T;kase++){
		cin>>N>>K;
		int a = (1<<N);
		int m = K%a;
		if(m == a-1){
			printf("Case #%d: ON\n",kase);
		} else {
			printf("Case #%d: OFF\n",kase);
		}
	}
}
	
