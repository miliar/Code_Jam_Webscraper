#include <iostream>
#include <string>
using namespace std;
string s[40];
//char m[26]={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
char m[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
int main(){
	int T;
	cin>>T;
	getline (cin,s[0]);
	for(int i=0;i<T;i++)
		getline (cin,s[i]);
	for(int i=0;i<T;i++)
		for(int j=0;j<s[i].length();j++)
			if(s[i][j]!=' ')s[i][j]=m[s[i][j]-'a'];
	for(int i=0;i<T;i++)
		cout<<"Case #"<<(i+1)<<": "<<s[i]<<endl;

}
