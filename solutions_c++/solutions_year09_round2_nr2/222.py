#include<iostream>
#include<algorithm>
using namespace std;
int main(){
	int t;
	cin>>t;
	for(int i=1;i<=t;++i){
		string s,t;
		cin>>s;
		t=s;
		cout<<"Case #"<<i<<": ";
		if(next_permutation(s.begin(),s.end())){
			cout<<s<<endl;
		}else{
			s="0"+t;
			next_permutation(s.begin(),s.end());
			cout<<s<<endl;
		}
	}
	return 0;
}
