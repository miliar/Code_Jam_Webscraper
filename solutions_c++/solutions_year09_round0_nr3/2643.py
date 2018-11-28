#include <iostream>
#include <string>
#include<sstream>
using namespace std;
int res (string source, string pattern){
	//cout << source <<":"<< pattern << endl;
	if(pattern.length()==0 && source.length()>=0)
		return 1;
	if(pattern.length()>0 && source.length()==0)
		return 0;
	int ans=0;
	for(int k=0; k<source.length(); k++)
		if(pattern[0]==source[k]){ans+= res(source.substr(k+1), pattern.substr(1));}
	return ans;
}
int main(){
	string s = "welcome to code jam";
	int n;
	scanf("%d", &n);
	getchar();
	for(int i=1; i<=n; i++){
		string test;
		getline(cin, test);
		stringstream ss;
		int ans;	
		ans = res(test,s);
		ss << ans;
		string a = ss.str();
		while(a.length()<4){
			a="0"+a;
		}
		cout << "Case #"<<i<<": "<<a<<endl;
	}
	return 0;
}
