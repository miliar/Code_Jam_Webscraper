#include<iostream>
#include<set>
#include<string>
using namespace std;
string s[5000];
set<char> char_set[15];
int main(){
	int n,l,d;
	cin>>l>>d>>n;
	for(int i=0;i<d;++i)
		cin>>s[i];
	for(int i=0;i<n;++i){
		string t;
		cin>>t;
		int sum=d;
		for(int j=0,k=0;j<l;++j,++k){
			char_set[j].clear();
			if(t[k]!='('){
				char_set[j].insert(t[k]);
			}else{
				while(t[++k]!=')')
					char_set[j].insert(t[k]);
			}
		}
		for(int j=0;j<d;++j){
			for(int k=0;k<l;++k)
				if(char_set[k].find(s[j][k])==char_set[k].end()){
					--sum;
					break;
				}
		}
		cout<<"Case #"<<(i+1)<<": "<<sum<<endl;
	}
	return 0;
}
