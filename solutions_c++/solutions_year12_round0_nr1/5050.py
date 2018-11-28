#include <iostream>
#include <string>

using namespace std;

int main()
{
	char a[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	string s,ans;
	char tmp;
	cin>>t;
	getline(cin,s);
	for(int i1=0;i1<t;i1++){
		getline(cin,s);
		ans="";
		for(int i=0;i<s.size();i++){
			ans+=s[i]==' '?' ':a[s[i]-'a'];
		}
		cout<<"Case #"<<i1+1<<": "<<ans<<endl;
	}
	return 0;
}
	
