#include <iostream>
#include<string>
using namespace std;

int main(){
	int t, n;
	string s;
	char sub[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
	cin>>t;
	getline(cin, s, '\n');
	for(int i=1; i<=t; i++){
		getline(cin, s, '\n');
		cout<<"Case #"<<i<<": ";
		n= s.length();
		for(int j=0; j<n; j++)
			if(s[j]==' ')
				cout<<' ';
			else
				cout<<sub[s[j]-'a'];
		cout<<endl;
	}
	return 0;
}