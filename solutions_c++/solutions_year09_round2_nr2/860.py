#include<algorithm>
#include<string>
#include<iostream>
using namespace std;

int main(){

	int n ;
	string s;
	cin>>n;
	for(int i=1;i<=n;i++){
		cin>>s;
		if(next_permutation(s.begin(),s.end()))
		cout<<"Case #"<<i<<": "<<s<<endl;
		else {
			sort(s.begin(),s.end());
			s="0"+s;
			int ii=1;
			while(s[ii]=='0' && ii<s.size())ii++;
			swap(s[0],s[ii]);
			cout<<"Case #"<<i<<": "<<s<<endl;
			
		}
	}
	return 0;
}
