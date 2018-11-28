#include<algorithm>
#include<iostream>
#include<string>

using namespace std;
string convert(string s){
  	string res = "";
	int c = 0;
	for(int i = 0 ; i < s.size() ; i++){
	  if(s[i] != '0')
		res+=s[i];
	  else
		c++;
	}
	string ceros = string(c+1,'0');
	res.insert(1,ceros);
	return res;
}
int main(){
  	int T;
	cin>>T;
	string s;
	
	for(int tt = 0; tt < T ; tt++){
	  	cin>>s;
		string temp = s;
		next_permutation(s.begin() , s.end());
		cout<<"Case #"<<tt+1<<": ";
		if(s <= temp){
		  s = convert(s);
		  cout<<s<<endl;
		}
		else
		  cout<<s<<endl;
	}
	return 0;
}