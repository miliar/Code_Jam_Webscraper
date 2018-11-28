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
	for(int i=0 ; i<n ; i++){
		string s;
		cin >> s;
		if(next_permutation(s.begin(),s.end())==false){
			prev_permutation(s.begin(),s.end());
			s.insert(0,"0");
			next_permutation(s.begin(),s.end());
		}
		cout <<"Case #"<<i+1<<": "<<s<<endl;
	}
	
	return 0;
}