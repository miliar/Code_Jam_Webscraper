#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
using namespace std;
string pre="yhesocvxduiglbkrztnwjpfmaq";
int main(){
	freopen ("1.out","w",stdout);
	freopen ("1.in","r",stdin);
	int t;
	scanf("%d\n",&t);
	for(int k=1;k<=t;k++){
		string s,res="";
		getline(cin,s);
		for(int i=0;i<s.length();i++){
			if(s[i]==' ')res+=' ';
			else {
				res+=pre[s[i]-'a'];
			}
		}
		cout<<"Case #"<<k<<": "<<res<<endl;
	}	
}
