#include<iostream>

using namespace std;

char T[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main()
{
	int n;
	string s;
	cin>>n;
	getline(cin,s);
	for(int q=1;q<=n;q++)
	{
		getline(cin,s);
		
		for(int i=0;i<s.size();i++)
		{
			if(s[i]!=' ')
				s[i]=T[s[i]-'a'];
		}		
		cout<<"Case #"<<q<<": "<<s<<endl;
	}
}
