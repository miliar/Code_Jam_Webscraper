#include<iostream>
#include<vector>
#include<string>
#include<sstream>
#include<algorithm>
#include<set>
#include<map>
#include<cstring>
using namespace std;

int main(){
	int n;
	cin >> n;
	for(int ii=0 ; ii<n ; ii++){
		map<char,int> mapc;
		string s;
		cin >> s;
		int cnt=0;
		mapc[s[0]]=1;
		for(int i=1 ; i<s.length() ; i++){
			map<char,int>::iterator it=mapc.find(s[i]);
			if(it==mapc.end()){
				//cout << s[i] << " "<<cnt<<endl;
				mapc[s[i]]=cnt;
				cnt++;
				if(cnt==1) cnt++;
			}
		}
		long long int res=0;
		int base=mapc.size() < 2 ?  2 : mapc.size(); 
		for(int i=0 ; i<s.length() ; i++){
			res=res*base + mapc[s[i]];
		}
		//if(res==1) res=0;
		cout <<"Case #"<<ii+1<<": "<<res<<endl;
	}
}