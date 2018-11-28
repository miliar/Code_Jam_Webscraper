#include <iostream>
#include <fstream>
#include <string>
using namespace std;


int main()
{
	char change[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};
	int t;
	freopen("A-small-attempt7.in","r",stdin);
	freopen("A-small-attempt7.out","w",stdout);
	cin>>t;
	getchar();
	int cnt=0;
	for(int cnt=1;cnt<=t;cnt++)
	{
		string s;
		getline(cin,s);
		string ans;
		for(int i=0;i<s.length();i++)
		{
			if(s[i]<='z'&&s[i]>='a')
				ans+=change[int(s[i]-'a')];
			else 
				ans+=s[i];
		}
		cout<<"Case #"<<cnt<<":"<<" "<<ans;
		if(cnt!=t)
			cout<<endl;
	}
	return 0;
}
